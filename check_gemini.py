"""Quick check: does your Gemini key work, and which model names can it use?
Run:  python check_gemini.py
The key itself is never printed."""

import os
import sys

from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

print("Key found in .env:", bool(key), "| key length:", len(key) if key else 0)
print("Model the app uses:", model)
if not key:
    sys.exit("No key found. Check that .env is in this folder and saved.")

from google import genai

client = genai.Client(api_key=key)

print("\nTrying a test question...")
try:
    reply = client.models.generate_content(model=model, contents="Reply with the single word: OK")
    print("SUCCESS. Gemini said:", reply.text)
    print("\nThe key and model both work. Restart the app and try again.")
except Exception as e:
    print("FAILED:", type(e).__name__)
    print(str(e)[:700])
    print("\nModels your key can use:")
    try:
        names = []
        for m in client.models.list():
            actions = getattr(m, "supported_actions", None) or []
            if not actions or "generateContent" in actions:
                names.append(m.name.replace("models/", ""))
        flash = [n for n in names if "flash" in n]
        print("\n".join((flash or names)[:25]) or "(none listed)")
    except Exception as e2:
        print("Could not list models:", type(e2).__name__, str(e2)[:300])
