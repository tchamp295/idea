import firebase_admin
from firebase_admin import credentials, firestore
import os


class FirebaseService:
    def __init__(self):
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate("credentials/serviceAccountKey.json")
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.connected = True
        except Exception as e:
            print(f"Firebase connection error: {e}")
            self.connected = False
            self.db = None
    
    def add_idea(self, idea_data):
        if not self.connected:
            print("Firebase not connected, cannot add idea")
            return False
        try:
            self.db.collection("ideas").add(idea_data)
            return True
        except Exception as e:
            print(f"Error adding idea: {e}")
            return False
    
    def get_all_ideas(self):
        if not self.connected:
            print("Firebase not connected, returning empty list")
            return []
        try:
            ideas = self.db.collection("ideas").stream()
            return [doc.to_dict() for doc in ideas]
        except Exception as e:
            print(f"Error getting ideas: {e}")
            return []