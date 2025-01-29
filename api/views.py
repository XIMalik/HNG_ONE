from django.shortcuts import render
from rest_framework.generics import ListAPIView
import datetime
from dotenv import load_dotenv
import os
from rest_framework import status
from rest_framework.response import Response

load_dotenv()

email = os.getenv("EMAIL")
repo = os.getenv("REPO")

class GetMyInfo(ListAPIView):
    def get(self, request, *args, **kwargs):
        date = datetime.datetime.now()
        
        response = {
            "email": email,
            "current_datetime": date,
            "github_url": repo
            }
        
        return Response(response, status.HTTP_200_OK)
        
