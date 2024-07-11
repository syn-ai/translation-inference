import io
import os
import shutil
import requests
from requests import Request
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile, File, HTTPException
from pathlib import Path
from pydub.utils import mediainfo
from pydub import AudioSegment
import base64


def process_audio_request(
    audio_data: bytes,
    task_string: str,
    sourceLanguageOptions: str,
    targetLanguageOptions: str
):
    request_audio_path = "static/audio/audio_request.wav"
    audio_data = AudioSegment.from_file(io.BytesIO(audio_data))
    audio_data.export(request_audio_path, format="wav")    
    
    target_language = targetLanguageOptions.replace("\\", "").replace("\"", "")
    source_language = sourceLanguageOptions.replace("\\", "").replace("\"", "")
    return {
        "data": {
            "input": request_audio_path,
            "task_string": task_string,
            "target_language": target_language,
            "source_language": source_language,
        }
    }


def process_audio_response(
    audio_endpoint: str,
    request: Request,
    templates: Jinja2Templates    
):
    audio_path = "static/audio/audio_request.wav" 
    get_audio_path = "https://miner-cellium.ngrok.app/static/out/audio_request.wav"
    audio_data = requests.get(get_audio_path, timeout=30).content
    content = AudioSegment.from_file(io.BytesIO(audio_data), format="webm")
    content.export(audio_path, format="wav")
        
    return templates.TemplateResponse(
        "components/audioOutput.html",
        {
            "request": request,
            "audio_url": audio_path
        },
    )