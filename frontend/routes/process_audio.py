import base64
from requests import Request, Response
from fastapi.templating import Jinja2Templates


AUDIO_SOURCE = "static/audio/output.wav"


def process_audio_request(
    audio_data: str,
    task_string: str,
    sourceLanguageOptions: str,
    targetLanguageOptions: str
):
    target_language = targetLanguageOptions.replace("\\", "").replace("\"", "")
    source_language = sourceLanguageOptions.replace("\\", "").replace("\"", "")
    b64audio = base64.b64encode(audio_data).decode("utf-8")
    return {
        "data": {
            "input": b64audio,
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
    audio_data = base64.b64decode(response.text).encode("utf-8")
    with open(AUDIO_SOURCE, "wb") as f:
        f.write(audio_data)
    return templates.TemplateResponse(
        "components/audioOutput.html",
        {
            "request": request,
            "audio_url": AUDIO_SOURCE
        },
    )