# School Safety Alert System

## Project Overview
This project implements a real-time school safety alert system using Flask, WebSockets, and a static map interface. The system monitors camera feeds for potential threats and provides immediate alerts to both authorities and students.

## Features
- **Static Map Interface**: Displays camera locations and threat alerts on a custom school map.
- **Real-time Threat Detection**: Processes camera images every 60 seconds to detect potential weapons.
- **Instant Alerts**: Notifies authorities and updates the map in real-time when a threat is detected.
- **Safe Area Marking**: Allows authorities to mark safe or evacuation areas on the map.
- **Threat Image Display**: Users can view the image that triggered an alert by clicking on the camera icon.
- **Alarm Management**: Authorities can disable alarms after reviewing the threat.

## Setup and Installation
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   ```

2. **Install required packages**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set the OpenAI API Key**:
   The system requires an OpenAI API key to work with the threat detection model. Set the `OPENAI_API_KEY` environment variable before running the application:
   ```sh
   export OPENAI_API_KEY=your_openai_api_key_here
   ```
   Alternatively, you can modify the code to use a different large language model (LLM) by updating the relevant API calls in the Flask application.

4. **Run the application**:
   ```sh
   python run.py
   ```

5. **Access the web interface**:
   Open a web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the system.

## Notes
- To switch to a different LLM, replace the OpenAI API integration in the code with the desired model's API. Ensure you update any associated authentication methods and API endpoints.

