from fastapi import FastAPI, UploadFile, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import db
from models import IdeaSubmission
from utils.file_upload import save_file
from auth import authenticate

app = FastAPI()

# CORS setup (to connect Vue frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Submit idea
@app.post("/submit-idea")
async def submit_idea(
    title: str = Form(...),
    description: str = Form(...),
    file: UploadFile = None
):
    file_url = None
    if file:
        file_url = save_file(file)

    idea = {
        "title": title,
        "description": description,
        "file_url": file_url,
    }
    db.collection("ideas").add(idea)
    return {"message": "Idea submitted successfully", "data": idea}

# Admin login
@app.post("/admin-login")
async def admin_login(username: str = Form(...), password: str = Form(...)):
    authenticate(username, password)
    return {"message": "Login successful"}

# Get all ideas (admin only)
@app.get("/ideas")
async def get_ideas(username: str, password: str):
    authenticate(username, password)
    ideas = db.collection("ideas").stream()
    return [i.to_dict() for i in ideas]
