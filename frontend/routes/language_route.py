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
    "--Select Language--",
    "English",
    "Cantonese",
    "French",
    "German",
    "Hindi",
    "Italian",
    "Japanese",
    "Korean",
    "Mandarin Chinese",
    "Russian",
    "Spanish",
    "---",
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
    "Galician",
    "Ganda",
    "Georgian",
    "Gujarati",
    "Halh Mongolian",
    "Hebrew",
    "Hungarian",
    "Icelandic",
    "Igbo",
    "Indonesian",
    "Irish",
    "Javanese",
    "Kabuverdianu",
    "Kamba",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Kyrgyz",
    "Lao",
    "Lithuanian",
    "Luo",
    "Luxembourgish",
    "Macedonian",
    "Maithili",
    "Malayalam",
    "Maltese",
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
    "Serbian",
    "Shona",
    "Sindhi",
    "Slovak",
    "Slovenian",
    "Somali",
    "Southern Pashto",
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
        lines.append(f'<option class="block bg-cyan-200 hover:bg-cyan-400 dark:hover:bg-cyan-700 dark:bg-cyan-600 px-4 py-2 rounded-t whitespace-no-wrap" value=\"{option}\">{option}</option>')
        
    return {"target_languages": "\n".join(lines)}