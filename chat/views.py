from django.views.generic import TemplateView
from django.shortcuts import redirect

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RandomTokenView(APIView):
    def get(self, request, *args, **kwargs):
        random_token = secrets.token_urlsafe(32)  # Generate a random token
        return Response({'token': random_token}, status=status.HTTP_200_OK)


class HomePageView(TemplateView):
    template_name = "chat/homePage.html"

class ChatPageView(TemplateView):
    template_name = "chat/chatPage.html"

    """
    def dispatch(self, request, *args, **kwargs):
        # Check if the user has followed the expected sequence
        if not request.session.get('from_homepage', False):
            return redirect('home-page')  # Redirect to homepage if the sequence is not followed
        return super().dispatch(request, *args, **kwargs)
    """


