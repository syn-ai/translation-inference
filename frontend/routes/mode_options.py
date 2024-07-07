from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/outputModeOptions")
async def get_outputContent(request: Request, outputModeOptions: str):
    if outputModeOptions == "text":
        return templates.TemplateResponse("components/textOutput.html", {"request": request})
    if outputModeOptions == "audio":
        return templates.TemplateResponse("components/audioOutput.html", {"request": request})
    
        

@router.get("/inputModeOptions")
async def inputModeOptions(request: Request, inputModeOptions: str):
    if inputModeOptions == "text":
        return templates.TemplateResponse("components/textInput.html", {"request": request})
    if inputModeOptions == "audio":
        return templates.TemplateResponse("components/audioInput.html", {"request": request})
    return templates.TemplateResponse("components/inputModeDropdown.html", {"request": request})