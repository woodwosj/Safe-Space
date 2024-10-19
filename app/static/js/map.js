let map;
let markers = {};

const cameraLocations = [
    {id: 'cam1', x: 100, y: 100, name: "Camera 1"},
    {id: 'cam2', x: 200, y: 200, name: "Camera 2"},
    // Update the coordinates as needed for the new map
];

function initMap() {
    map = document.getElementById('static-map');

    // Add markers for each camera
    cameraLocations.forEach(camera => {
        const marker = document.createElement('div');
        marker.className = 'camera-marker';
        marker.style.left = `${camera.x}px`;
        marker.style.top = `${camera.y}px`;
        marker.title = camera.name;
        marker.onclick = () => showCameraInfo(camera.id);
        map.appendChild(marker);
        markers[camera.id] = marker;
    });

    // Connect to the Flask-SocketIO server
    const socket = io();

    // Listen for real-time updates
    socket.on('threat_update', function(data) {
        updateThreatStatus(data.camera_id, data.alarm, data.image_data);
    });

    // Listen for safe area updates
    socket.on('safe_area_update', function(data) {
        updateSafeArea(data);
    });
}

function updateThreatStatus(cameraId, isActive, imageData) {
    const marker = markers[cameraId];
    if (marker) {
        if (isActive) {
            marker.classList.add('alarm-active');
            marker.onclick = () => showThreatInfo(cameraId, imageData);
        } else {
            marker.classList.remove('alarm-active');
            marker.onclick = () => showCameraInfo(cameraId);
        }
    }
}

function showThreatInfo(cameraId, imageData) {
    const infoBox = document.getElementById('info-box');
    infoBox.innerHTML = `
        <h3>THREAT DETECTED</h3>
        <p>Camera: ${cameraId}</p>
        <p>Time: ${new Date().toLocaleString()}</p>
        <img src="data:image/jpeg;base64,${imageData}" alt="Threat Image" style="max-width: 100%;">
    `;
    infoBox.style.display = 'block';
}

function showCameraInfo(cameraId) {
    const infoBox = document.getElementById('info-box');
    infoBox.innerHTML = `
        <h3>Camera Information</h3>
        <p>Camera ID: ${cameraId}</p>
        <p>Status: Normal</p>
    `;
    infoBox.style.display = 'block';
}

function updateSafeArea(data) {
    const safeArea = document.createElement('div');
    safeArea.className = 'safe-area';
    safeArea.style.left = `${data.x}px`;
    safeArea.style.top = `${data.y}px`;
    safeArea.title = "Safe Area";
    safeArea.onclick = () => showSafeAreaInfo(data);
    map.appendChild(safeArea);
}

function showSafeAreaInfo(data) {
    const infoBox = document.getElementById('info-box');
    infoBox.innerHTML = `
        <h3>Safe Area</h3>
        <p>${data.info}</p>
    `;
    infoBox.style.display = 'block';
}

// Initialize the map when the page loads
window.onload = initMap;