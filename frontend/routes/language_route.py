from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./templates")

router = APIRouter()


TASK_STRINGS = [
    "speech2text"
    "speech2speech"
    "auto_speech_recognition"
    "text2speech"
    "text2text"
]

TARGET_LANGUAGES = [
    "English",
    "Afrikaans",
    "Amharic",
    "Armenian",
    "Assamese",
    "Asturian",
    "Basque",
    "Belarusian",
    "Bengali",
    "Bosnian",
    "Bulgarian",
    "Burmese",
    "Cantonese",
    "Catalan",
    "Cebuano",
    "Central",
    "Colloquial Malay",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "Egyptian Arabic",
    "Estonian",
    "Finnish",
    "French",
    "Galician",
    "Ganda",
    "Georgian",
    "German",
    "Gujarati",
    "Halh Mongolian",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Icelandic",
    "Igbo",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Javanese",
    "Kabuverdianu",
    "Kamba",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Korean",
    "Kyrgyz",
    "Lao",
    "Lithuanian",
    "Luo",
    "Luxembourgish",
    "Macedonian",
    "Maithili",
    "Malayalam",
    "Maltese",
    "Mandarin Chinese",
    "Mandarin Chinese Hant",
    "Marathi",
    "Meitei",
    "Modern Standard Arabic",
    "Moroccan Arabic",
    "Nepali",
    "Nigerian Fulfulde",
    "North Azerbaijani",
    "Northern Uzbek",
    "Norwegian Bokmål",
    "Norwegian Nynorsk",
    "Nyanja",
    "Occitan",
    "Odia",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Romanian",
    "Russian",
    "Serbian",
    "Shona",
    "Sindhi",
    "Slovak",
    "Slovenian",
    "Somali",
    "Southern Pashto",
    "Spanish",
    "Standard Latvian",
    "Standard Malay",
    "Swahili",
    "Swedish",
    "Tagalog",
    "Tajik",
    "Tamil",
    "Telugu",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Vietnamese",
    "Welsh",
    "West Central Oromo",
    "Western Persian",
    "Xhosa",
    "Yoruba",
    "Zulu",
]

@router.get("/languages")
async def get_languages(request: Request):
    lines = []
    for option in TARGET_LANGUAGES:
        lines.append(f"<option value=\"{option}\">{option}</option>")
        
    return {"target_languages": "\n".join(lines)}

@router.get("/tasks")
async def get_task_string(request: Request):
    return {"task": task}