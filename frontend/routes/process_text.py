from requests import Request, Response
from fastapi.templating import Jinja2Templates
import requests


def process_text_request(
    textInputArea: str,
    task_string: str,
    targetLanguageOptions: str,
    sourceLanguageOptions: str,
):    
    target_language = targetLanguageOptions.replace("\\", "").replace("\"", "")
    source_language = sourceLanguageOptions.replace("\\", "").replace("\"", "")
    return {
        "data": {
            "input": textInputArea,
            "task_string": task_string,
            "target_language": target_language,
            "source_language": source_language,
        }
    }
    

def process_text_response(
    text_response: str,
    request: Request,
    templates: Jinja2Templates
):  
    url = f"https://miner-cellium.ngrok.app/static/out/{text_response}"
    response = requests.get(url, timeout=60)
    data = response.text.replace("[CString(", "").replace(")]", "").replace("'", "").strip()
    return templates.TemplateResponse(
        "components/textOutput.html",
        {
            "request": request,
            "text": data,
        }
    )