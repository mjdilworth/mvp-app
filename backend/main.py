from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
import random
import httpx
import os

app = FastAPI()

class Message(BaseModel):
    message: str

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the web developer go broke? Because he used up all his cache.",
    "Why do programmers hate nature? It has too many bugs.",
]

# Serve static files (e.g. /static/_next/...)
app.mount("/static", StaticFiles(directory="frontend/out", html=True), name="static")

# Fallback: serve index.html for any other route (for SPA routing)
@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    return FileResponse("frontend/out/index.html")

# Example API route
@app.post("/api/echo")
async def echo(payload: Message):
    user_message = payload.message.strip().lower()

    # Special case: user asked about astronauts
    if "who is in space" in user_message:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://api.open-notify.org/astros.json", timeout=5.0)
                response.raise_for_status()
                data = response.json()
                people = data.get("people", [])
                count = data.get("number", 0)

                names = "\n".join([f"- {p['name']} ({p['craft']})" for p in people])
                reply = f"🧑‍🚀 There are {count} people in space:\n{names}"
                return {"reply": reply}
        except Exception as e:
            return {"reply": f"❌ Failed to fetch astronaut data: {str(e)}"}
        
    elif "what time is it" in user_message:
        now = datetime.utcnow().strftime("%H:%M UTC on %Y-%m-%d")
        return {"reply": f"🕒 The current UTC time is {now}"}

    elif "tell me a joke" in user_message:
        return {"reply": f"😂 {random.choice(jokes)}"}
    
    elif "help" in user_message or "what can i ask" in user_message:
        reply = (
            "🤖 You can ask me things like:\n"
            "- Who is in space\n"
            "- What time is it\n"
            "- Tell me a joke\n"
            "- (Or just say anything and I'll echo it!)"
        )
        return {"reply": reply}
    else:
        return {"reply": f"You said: '{payload.message}'"}

    # Default echo behavior
    return {"reply": f"You said: '{payload.message}'"}