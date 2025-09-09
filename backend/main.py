from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import db
from models import IdeaSubmission
from utils.file_upload import save_file
from auth import authenticate
from datetime import datetime

app = FastAPI()

# CORS setup (to connect Vue frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Submit idea (matches frontend: /api/submit-idea/)
@app.post("/api/submit-idea/")
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
        "created_at": datetime.now().isoformat(),
    }
    
    doc_ref = db.collection("ideas").add(idea)
    idea["id"] = doc_ref[1].id
    
    return {"message": "Idea submitted successfully", "data": idea}

# Admin login (matches frontend: /api/admin-login/)
@app.post("/api/admin-login/")
async def admin_login(username: str = Form(...), password: str = Form(...)):
    authenticate(username, password)
    return {"message": "Login successful"}

# Get all ideas (admin only, matches frontend: /api/ideas/)
@app.get("/api/ideas/")
async def get_ideas(username: str, password: str):
    authenticate(username, password)
    try:
        ideas_stream = db.collection("ideas").stream()
        ideas = []
        for doc in ideas_stream:
            idea_data = doc.to_dict()
            idea_data["id"] = doc.id
            ideas.append(idea_data)
        return ideas
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch ideas")
