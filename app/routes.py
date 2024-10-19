from flask import Blueprint, render_template, request, jsonify
from flask_socketio import emit
from app import socketio
from openai_api_integration import analyze_image

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/threat_detection', methods=['POST'])
def threat_detection():
    data = request.json
    camera_id = data.get('camera_id')
    image_data = data.get('image_data')

    weapon_detected = analyze_image(image_data)

    socketio.emit('threat_update', {
        'camera_id': camera_id,
        'alarm': weapon_detected,
        'image_data': image_data
    })

    return jsonify({"status": "processed", "weapon_detected": weapon_detected}), 200


def send_alert_to_authorities(camera_id):
    print(f"ALERT: Threat detected on camera {camera_id}.")
