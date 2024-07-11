from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydub import AudioSegment
import io
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/output", StaticFiles(directory="output"), name="output")


@app.get("/")
async def index():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/upload-audio")
async def upload_audio(audio: UploadFile = File(...)):
    try:
        # Create a unique filename
        file_name = f"audio_{os.urandom(8).hex()}.wav"
        file_location = f"output/{file_name}"
        
        # Save the file
        content = AudioSegment.from_file(io.BytesIO(await audio.read()), format="webm")
        content.export(file_location, format="wav")
        
        # Check if file was saved and has content
        if os.path.exists(file_location) and os.path.getsize(file_location) > 0:
            return JSONResponse(content={"filename": file_name, "size": os.path.getsize(file_location)})
        else:
            return JSONResponse(status_code=500, content={"error": "File not saved correctly"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)