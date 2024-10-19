import os
import openai
import base64
import json
from dotenv import load_dotenv

# Load environment variables for API keys
load_dotenv()

###'OPENAIAPIKEY' HERE
OPENAI_API_KEY =
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key provided. Please set the OPENAI_API_KEY in the .env file.")

openai.api_key = OPENAI_API_KEY

def analyze_image(image_data):
    """
    Analyze the given image data to detect if there's a firearm present.
    
    :param image_data: Base64 encoded image string
    :return: Boolean value indicating the presence of a firearm (True if detected, False otherwise)
    """
    prompt = "Analyze the image and respond with a JSON object. If you see a gun or firearm in the image, set the 'weapon_detected' key to true, otherwise set it to false."
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that responds in JSON format."},
                {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                ]}
            ],
            response_format={"type": "json_object"}
        )
        
        # Parse the JSON response
        response_content = response.choices[0].message.content
        response_json = json.loads(response_content)
        return response_json.get('weapon_detected', False)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return False
    except Exception as e:
        print(f"Error in OpenAI API call: {e}")
        return False


def capture_and_process_image(camera_id):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            # Encode the image as base64
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')

            # Analyze the image with OpenAI API
            try:
                firearm_detected = analyze_image(jpg_as_text)
                data = {
                    'camera_id': camera_id,
                    'weapon_detected': firearm_detected
                }

                # Send the data to the Flask app
                response = requests.post('http://localhost:5000/threat_detection', json=data)
                response.raise_for_status()
                print(f"Sent data to server. Weapon detected: {firearm_detected}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send data to server: {e}")
            except Exception as e:
                print(f"Error analyzing image: {e}")

        time.sleep(60)
    cap.release()

if __name__ == "__main__":
    capture_and_process_image('cam1')