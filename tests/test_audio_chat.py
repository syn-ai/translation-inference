# tests/components/test_audio_chat.py

from fastapi.testclient import TestClient
from frontend.main import app

client = TestClient(app)

def test_audio_chat_page():
    response = client.get("/audio-chat")
    assert response.status_code == 200
    assert "Audio Chat Application" in response.text
    assert "Audio Player" in response.text
    assert "Microphone Input" in response.text
    assert "File Upload" in response.text
    assert "Chat History" in response.text

def test_upload_audio():
    with open("tests/test_files/test_audio.mp3", "rb") as f:
        response = client.post("/upload-audio", files={"file": ("test_audio.mp3", f, "audio/mpeg")})
    assert response.status_code == 200
    assert "Successfully uploaded test_audio.mp3" in response.json()["message"]

def test_send_audio():
    with open("tests/test_files/test_audio.wav", "rb") as f:
        audio_data = f.read()
    response = client.post("/send-audio", files={"audio_data": ("audio.wav", audio_data, "audio/wav")})
    assert response.status_code == 200
    assert "Audio received and processed" in response.json()["message"]

def test_chat_history():
    response = client.get("/chat-history")
    assert response.status_code == 200
    assert "You" in response.text
    assert "AI" in response.text