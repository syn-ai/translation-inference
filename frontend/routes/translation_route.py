import base64
import json
import binascii
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
import requests

from frontend.routes.audio_route import AUDIO_SOURCE

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.post("/translate")
async def get_translate(
    request: Request, 
    textInputArea: str = Form(default=''),
    inputModeOptions: str = Form(default=''),
    outputModeOptions: str = Form(default=''),
    sourceLanguageOptions: str = Form(default=''),
    targetLanguageOptions: str = Form(default='')
):
    print(f"Received form data: textInputArea={textInputArea}, inputModeOptions={inputModeOptions}, outputModeOptions={outputModeOptions}, sourceLanguageOptions={sourceLanguageOptions}, targetLanguageOptions={targetLanguageOptions}")
    task_string = ""
    if textInputArea == "":
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    if inputModeOptions == "audio":
        if outputModeOptions == "audio":
            task_string = "speech2speech"
        elif outputModeOptions == "text":
            task_string = "speech2text"
    elif inputModeOptions == "text":
        if outputModeOptions == "text":
            task_string = "text2text"
        elif outputModeOptions == "audio":
            task_string = "text2speech"
    else:
        task_string = "text2text"  # Default fallback

    url = "https://miner-cellium.ngrok.app/modules/translation/process"
    translation_request = {
        "data": {
            "input": textInputArea,
            "task_string": task_string,
            "target_language": targetLanguageOptions.replace("\\", "").replace("\"", ""),
            "source_language": sourceLanguageOptions.replace("\\", "").replace("\"", ""),
        }
    }
    
    print(f"Sending request: {translation_request}")
    
    try:
        response = requests.post(url, json=translation_request, timeout=30)
        response.raise_for_status()
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text[:1000]}")  # Print first 1000 characters of response
        
        if task_string.endswith("text"):
            return templates.TemplateResponse(
                "components/textOutput.html",
                {
                    "request": request,
                    "text": json.loads(response.text)["output"].replace("[CString(", "").replace(")]", "").replace("'", "").strip(),
                }
            )
        else:
            try:
                audio_data = base64.b64decode(response.text)
                with open(AUDIO_SOURCE, "wb") as f:
                    f.write(audio_data)
                return templates.TemplateResponse(
                    "components/audioOutput.html",
                    {
                        "request": request,
                        "audio_url": AUDIO_SOURCE
                    },
                )
            except binascii.Error:
                print("Failed to decode base64 audio data")
                return templates.TemplateResponse(
                    "components/textOutput.html",
                    {
                        "request": request,
                        "text": f"Error: Received invalid audio data. Raw response: {response.text[:1000]}",
                    }
                )
    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Translation service error: {str(e)}")