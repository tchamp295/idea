import firebase_admin
from firebase_admin import credentials, firestore
import os


class FirebaseService:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    
    def add_idea(self, idea_data):
        self.db.collection("ideas").add(idea_data)
    
    def get_all_ideas(self):
        ideas = self.db.collection("ideas").stream()
        return [doc.to_dict() for doc in ideas]