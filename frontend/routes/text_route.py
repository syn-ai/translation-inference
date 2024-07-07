import json
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/text-output")
async def chat_history(request: Request):
    check = is_older_than_3_minutes()
    if check is True:
        with open("static/text/translation_history.txt", "w", encoding="utf-8") as f:
            f.write("[]")
    with open("static/text/translation_history.txt", "r", encoding="utf-8") as f:
        history = f.read()
    if not history or not history.strip():
        history = []
    history.append(request.query_params.get("message", ""))
    if len(history) > 5:
        history = history[-5:]
    with open ("static/text/translation_history.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(history))
    return templates.TemplateResponse("components/textOutput.html", {"request": {}, "history": history})

@router.post("/upload-text")
async def upload_text(file: UploadFile = File(...)):
    # Here you would typically save and process the text file
    # For this example, we'll just return a success message
    content = await file.read()
    return {"message": f"Text file '{file.filename}' uploaded and processed. Content length: {len(content)} bytes"}


def is_older_than_3_minutes():
    nowtime = datetime.now().timestamp()
    if not os.path.exists("static/time.json"):
        with open("static/time.json", "w", encoding="utf-8") as f:
            f.write(json.dumps({"timestamp": nowtime}))
    with open("static/time.json", "r", encoding="utf-8") as f:
        timestamp = json.loads(f.read())["timestamp"]
    if timestamp - nowtime > 180:
        with open("static/time.json", "w", encoding="utf-8") as f:
            f.write(json.dumps({"timestamp": nowtime}))
        return True
    return False