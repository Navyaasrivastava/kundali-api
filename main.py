from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random

app = FastAPI(title="NUMs + Kundali API")

# ✅ CORS (very important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- ZODIAC ----------
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

traits = [
    "Naturally charming personality",
    "Strong and determined mindset",
    "Kind-hearted and caring nature",
    "Confident and fearless attitude",
    "Positive and inspiring presence",
    "Goal-oriented and focused",
    "Loyal and trustworthy",
]

quotes = [
    "You are born to shine brighter than others.",
    "Your energy attracts success naturally.",
    "Confidence is your hidden superpower.",
    "Great things are coming into your life."
]

# Root route
@app.get("/")
def home():
    return {"message": "NUMs + Kundali API is LIVE 🚀"}

# Health route
@app.get("/health")
def health():
    return {"status": "ok"}

# Fix favicon 404
@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon"}

# 🔥 MAIN KUNDALI ENDPOINT (FIXED COMPLETELY)
@app.api_route("/kundali", methods=["GET","POST"])
@app.api_route("//kundali", methods=["GET","POST"])  # accepts double slash
async def kundali(request: Request,
                  name: str = Query(None),
                  dob: str = Query(None),
                  place: str = Query("India")):

    # ✅ If POST → read JSON body
    if request.method == "POST":
        data = await request.json()
        name = data.get("name")
        dob = data.get("dob")
        place = data.get("place", "India")

    # Validate input
    if not name or not dob:
        return {"error": "Send name and dob"}

    try:
        date_obj = datetime.strptime(dob, "%d-%m-%Y")
    except:
        return {"error": "DOB must be DD-MM-YYYY"}

    zodiac = get_zodiac(date_obj.day, date_obj.month)

    return {
        "name": name,
        "place_of_birth": place,
        "zodiac_sign": zodiac,
        "personality_traits": random.sample(traits, 3),
        "message": random.choice(quotes)
    }
