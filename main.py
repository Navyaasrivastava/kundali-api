from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random

app = FastAPI(title="NUMs + Kundali API", version="1.0")

# ✅ CORS ENABLED
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change later to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- ZODIAC FUNCTION ----------
def get_zodiac(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini ♊"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio ♏"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius ♐"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius ♒"
    else:
        return "Pisces ♓"

traits_en = [
    "Naturally charming personality",
    "Strong and determined mindset",
    "Kind-hearted and caring nature",
    "Confident and fearless attitude",
    "Intelligent decision maker",
    "Positive and inspiring presence",
    "Goal-oriented and focused",
    "Loyal and trustworthy",
    "Attractive aura and energy",
    "Calm and balanced personality"
]

quotes_en = [
    "You are born to shine brighter than others.",
    "Your energy attracts success naturally.",
    "Confidence is your hidden superpower.",
    "Your future is full of success and happiness.",
    "Great things are coming into your life."
]

traits_hi = [
    "आकर्षक व्यक्तित्व",
    "मजबूत और दृढ़ सोच",
    "दयालु स्वभाव",
    "आत्मविश्वासी और निडर",
    "सकारात्मक ऊर्जा",
    "लक्ष्य पर केंद्रित",
    "विश्वसनीय और वफादार"
]

quotes_hi = [
    "आप सफलता के लिए जन्मे हैं।",
    "आपकी ऊर्जा सफलता को आकर्षित करती है।",
    "आपका भविष्य उज्ज्वल है।",
    "आपकी मेहनत रंग लाएगी।"
]

# ✅ ROOT ROUTE (No 404)
@app.get("/")
def home():
    return {"message": "NUMs + Kundali API is LIVE 🚀"}

# ✅ HEALTH CHECK (Render)
@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ FIX FAVICON 404
@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon"}

# 🔮 KUNDALI API
@app.get("/kundali")
def kundali(
    name: str,
    dob: str = Query(..., description="DD-MM-YYYY"),
    place: str = "India",
    lang: str = "en"
):
    try:
        date_obj = datetime.strptime(dob, "%d-%m-%Y")
    except:
        return {"error": "Use DOB format DD-MM-YYYY"}

    zodiac = get_zodiac(date_obj.day, date_obj.month)

    if lang == "hi":
        return {
            "नाम": name,
            "जन्म स्थान": place,
            "राशि": zodiac,
            "व्यक्तित्व": random.sample(traits_hi, 3),
            "संदेश": random.choice(quotes_hi)
        }

    return {
        "name": name,
        "place_of_birth": place,
        "zodiac_sign": zodiac,
        "personality_traits": random.sample(traits_en, 3),
        "message": random.choice(quotes_en)
    }

