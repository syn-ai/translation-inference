import io
import base64
from loguru import logger
from requests import Request
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile, File, HTTPException
from pathlib import Path
from pydub.utils import mediainfo
from pydub import AudioSegment
import base64


async def process_audio_request(
    audioData: UploadFile,
    task_string: str,
    sourceLanguageOptions: str,
    targetLanguageOptions: str
):
    logger.debug("Processing Audio Request")
    request_audio_path = "static/audio/audio_request.wav"
    content = AudioSegment.from_file(io.BytesIO(await audioData.read()), format="webm")
    content.export(request_audio_path, format="wav")
    with open(request_audio_path, "rb") as f:
        audio_data = f.read()
    base64audio = base64.b64encode(audio_data).decode("utf-8")
    target_language = targetLanguageOptions.replace("\\", "").replace("\"", "")
    source_language = sourceLanguageOptions.replace("\\", "").replace("\"", "")
    return {
        "data": {
            "input": base64audio,
            "task_string": task_string,
            "target_language": target_language,
            "source_language": source_language,
        }
    }


def process_audio_response(
    response: str,
    request: Request,
    templates: Jinja2Templates    
):
    logger.info("Processing Audio Response")
    logger.debug(f"response: {response}")
    audio_path = "static/audio/audio_request.wav"
    content = base64.b64decode(response.text.encode("utf-8"))
    audio = AudioSegment.from_file(io.BytesIO(content), format="wav")
    audio.export(audio_path, format="wav")
        
    return templates.TemplateResponse(
        "components/audioOutput.html",
        {
            "request": request,
            "audio_url": audio_path
        },
    )