# Developed by drox - drox gpt
# Instagram: rayan_71x
# Purpose: Professional FastAPI Temporary Email Service using 1secmail API

from fastapi import FastAPI, HTTPException, Query
import httpx

app = FastAPI(
    title="Drox Temp Mail API",
    description="A professional temporary email service developed by drox gpt",
    version="1.0.0"
)

BASE_URL = "https://www.1secmail.com/api/v1/"

def split_email(email: str):
    """Helper to split email into login and domain for 1secmail API."""
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email format")
    login, domain = email.split("@", 1)
    return login, domain

@app.get("/")
async def root():
    """Developer info and API status"""
    return {
        "developer": "drox",
        "instagram": "rayan_71x",
        "credit": "It was developed by drox gpt",
        "status": "active"
    }

@app.get("/generate")
async def generate_email():
    """Generates a new random temporary email address via 1secmail"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}?action=genEmailAddresses&count=1")
            response.raise_for_status()
            emails = response.json()
            return {"email": emails[0], "status": "success", "provider": "1secmail"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/messages")
async def get_messages(email: str = Query(..., description="The full temporary email address")):
    """Lists messages for the specified email address"""
    login, domain = split_email(email)
    async with httpx.AsyncClient() as client:
        try:
            url = f"{BASE_URL}?action=getMessages&login={login}&domain={domain}"
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/message")
async def get_message(
    email: str = Query(..., description="The full temporary email address"),
    id: int = Query(..., description="The specific message ID to fetch")
):
    """Fetches the content of a specific message by ID"""
    login, domain = split_email(email)
    async with httpx.AsyncClient() as client:
        try:
            url = f"{BASE_URL}?action=readMessage&login={login}&domain={domain}&id={id}"
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))