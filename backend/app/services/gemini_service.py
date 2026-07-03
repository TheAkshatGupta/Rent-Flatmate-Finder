import os
import json
import google.generativeai as genai

from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_compatibility(profile, listing):

    prompt = f"""
You are an AI compatibility engine.

Tenant Profile:

Budget: {profile.budget}
Food Preference: {profile.food_preference}
Smoking: {profile.smoking}
Cleanliness: {profile.cleanliness}
Bio: {profile.bio}

Room Listing:

City: {listing.city}
Rent: {listing.rent}
Description: {listing.description}

Return ONLY valid JSON.

Example:

{{
"score":92,
"explanation":"Excellent match because budget and location align."
}}
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        result = json.loads(text)

        return result

    except Exception:

        return None