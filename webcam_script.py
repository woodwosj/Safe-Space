import cv2
import time
import requests
import base64

def capture_and_process_image(camera_id):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            # Encode the image as base64
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')

            # Prepare the data to send to the Flask app
            data = {
                'camera_id': camera_id,
                'image_data': jpg_as_text
            }

            # Send the data to the Flask app
            try:
                response = requests.post('http://localhost:5000/threat_detection', json=data)
                response.raise_for_status()
                response_data = response.json()
                print(f"Weapon detected: {response_data['weapon_detected']}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send data to server: {e}")

        time.sleep(60)
    cap.release()

if __name__ == "__main__":
    capture_and_process_image('cam1')
