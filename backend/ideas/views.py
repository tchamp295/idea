from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Idea
from .serializers import IdeaSerializer
from .firebase_service import FirebaseService
from .file_service import save_file


firebase_service = FirebaseService()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


@api_view(['POST'])
def submit_idea(request):
    title = request.data.get('title')
    description = request.data.get('description')
    file = request.FILES.get('file')
    
    if not title or not description:
        return Response({'error': 'Title and description are required'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    file_url = None
    if file:
        file_url = save_file(file)
    
    idea_data = {
        'title': title,
        'description': description,
        'file_url': file_url,
    }
    
    firebase_service.add_idea(idea_data)
    
    return Response({
        'message': 'Idea submitted successfully',
        'data': idea_data
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return Response({'message': 'Login successful'})
    else:
        return Response({'error': 'Invalid credentials'}, 
                       status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_ideas(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        return Response({'error': 'Invalid credentials'}, 
                       status=status.HTTP_401_UNAUTHORIZED)
    
    ideas = firebase_service.get_all_ideas()
    return Response(ideas)