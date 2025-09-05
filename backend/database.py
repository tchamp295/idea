import firebase_admin
from firebase_admin import credentials, firestore
import os

cred = credentials.Certificate("credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
