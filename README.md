# School Safety Alert System

## Project Overview
This project implements a real-time school safety alert system using Flask, WebSockets, and a static map interface. The system monitors camera feeds for potential threats and provides immediate alerts to both authorities and students.

## Features
1. **Static Map Interface**: Displays camera locations and threat alerts on a custom school map.
2. **Real-time Threat Detection**: Processes camera images every 60 seconds to detect potential weapons.
3. **Instant Alerts**: Notifies authorities and updates the map in real-time when a threat is detected.
4. **Safe Area Marking**: Allows authorities to mark safe or evacuation areas on the map.
5. **Threat Image Display**: Users can view the image that triggered an alert by clicking on the camera icon.
6. **Alarm Management**: Authorities can disable alarms after reviewing the threat.

## Setup and Installation
1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the application: `python run.py`
4. Access the web interface at `http://localhost:5000`
