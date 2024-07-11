import json
from requests import Request, Response
from fastapi.templating import Jinja2Templates


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
    request: Request,
    response: Response,
    templates: Jinja2Templates
):  

    data = response.replace("[CString(", "").replace(")]", "").replace("'", "").strip()
    return templates.TemplateResponse(
        "components/textOutput.html",
        {
            "request": request,
            "text": data,
        }
    )