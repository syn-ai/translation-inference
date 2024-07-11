import numpy
import struct
import io
import json
from loguru import logger
from requests import Request, Response
from fastapi.templating import Jinja2Templates


AUDIO_SOURCE = "output/output.wav"


def numpy_to_bytes(speech_output):
    return speech_output.tobytes()


# If your output is a list of floats
def list_to_bytes(speech_output):
    return struct.pack(f'{len(speech_output)}f', *speech_output)


def process_audio_request(
    task_string: str,
    sourceLanguageOptions: str,
    targetLanguageOptions: str
):
    target_language = targetLanguageOptions.replace("\\", "").replace("\"", "")
    source_language = sourceLanguageOptions.replace("\\", "").replace("\"", "")
    return {
        "data": {
            "input": AUDIO_SOURCE,
            "task_string": task_string,
            "target_language": target_language,
            "source_language": source_language,
        }
    }
    
def process_audio_response(
    request: Request,
    response: Response,
    templates: Jinja2Templates    
):
    return templates.TemplateResponse(
        "components/audioOutput.html",
        {
            "request": request,
            "audio_url": response
        },
    )