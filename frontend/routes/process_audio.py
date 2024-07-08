import base64
import numpy
import struct
import io
import base64
import json
import torch
from loguru import logger
from requests import Request, Response
from fastapi.templating import Jinja2Templates


AUDIO_SOURCE = "static/audio/output.wav"


def numpy_to_bytes(speech_output):
    return speech_output.tobytes()


# If your output is a list of floats
def list_to_bytes(speech_output):
    return struct.pack(f'{len(speech_output)}f', *speech_output)


def process_audio_request(
    audioData: str,
    task_string: str,
    sourceLanguageOptions: str,
    targetLanguageOptions: str
):
    target_language = targetLanguageOptions.replace("\\", "").replace("\"", "")
    source_language = sourceLanguageOptions.replace("\\", "").replace("\"", "")
    logger.debug(f"Audio data: {audioData}")
    audio_data = speech_output_to_base64(speech_output_to_base64=audioData)
    logger.info(f"Audio data: {audio_data}")
    return {
        "data": {
            "input": audio_data,
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
    print(response.text)
    with open(AUDIO_SOURCE, "wb") as f:
        f.write(base64.decodebytes(response.text.encode('utf-8')))
    return templates.TemplateResponse(
        "components/audioOutput.html",
        {
            "request": request,
            "audio_url": AUDIO_SOURCE
        },
    )
    
    
def speech_output_to_base64(speech_output) -> str:
    # Convert audio tensors to bytes
    audio_bytes_list = []
    for audio_wav in speech_output.audio_wavs:
        buffer = io.BytesIO()
        torch.save(audio_wav, buffer)
        audio_bytes_list.append(buffer.getvalue())

    # Create a dictionary with all the data
    data_dict = {
        "units": speech_output.units,
        "audio_wavs": audio_bytes_list,
        "sample_rate": speech_output.sample_rate
    }

    # Convert the dictionary to JSON
    json_data = json.dumps(data_dict)

    # Encode the JSON string to bytes and then to base64
    base64_encoded = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')

    return base64_encoded
