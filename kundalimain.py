from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ---------- Zodiac Finder ----------
def get_zodiac(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Aries ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taurus ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gemini ♊"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Leo ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Virgo ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Libra ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpio ♏"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittarius ♐"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19): return "Capricorn ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Aquarius ♒"
    else: return "Pisces ♓"

# ---------- Personality Traits & Quotes ----------
traits = [
    "✨ Naturally charming personality", "💪 Strong and determined mindset",
    "🌸 Kind-hearted and caring nature", "🔥 Confident and fearless attitude",
    "🧠 Intelligent decision maker", "🌈 Positive and inspiring presence",
    "🎯 Goal-oriented and focused", "💖 Loyal and trustworthy",
    "🌟 Attractive aura and energy", "🕊 Calm and balanced personality"
]

quotes = [
    "You are born to shine brighter than others.",
    "Your energy attracts success naturally.",
    "Confidence is your hidden superpower.",
    "You carry a unique charm that people admire.",
    "Your presence creates positivity everywhere.",
    "You are stronger than you believe.",
    "Your future is full of success and happiness.",
    "You inspire people without even trying.",
    "Your personality makes you unforgettable.",
    "Great things are coming into your life."
]

# ---------- Root route ----------
@app.route('/')
def home():
    return jsonify({
        "message": "🚀 Kundali API is running!",
        "instructions": {
            "POST /kundali": {
                "name": "Your name",
                "dob": "DD-MM-YYYY",
                "place": "Birthplace"
            }
        }
    })

# ---------- Kundali route ----------
@app.route('/kundali', methods=['POST'])
def kundali():
    data = request.json
    name = data.get("name")
    dob = data.get("dob")
    place = data.get("place")
    
    if not all([name, dob, place]):
        return jsonify({"error": "Please provide name, dob, and place"}), 400
    
    try:
        date_obj = datetime.strptime(dob, "%d-%m-%Y")
        day = date_obj.day
        month = date_obj.month
    except ValueError:
        return jsonify({"error": "Invalid DOB format. Use DD-MM-YYYY"}), 400
    
    zodiac = get_zodiac(day, month)
    selected_traits = random.sample(traits, 3)
    selected_quote = random.choice(quotes)
    
    return jsonify({
        "name": name,
        "place": place,
        "zodiac": zodiac,
        "traits": selected_traits,
        "quote": selected_quote
    })

# ---------- Run locally ----------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
