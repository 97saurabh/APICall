from django.shortcuts import render
from . import forms, models
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.views.generic import CreateView

# Homepage
def home(request):

    return render(request, "myapp/base.html", {})

# Api Call for displaying data
class ArticalAPIView(APIView):
    def get(self, request):
        articles = models.UserData.objects.all()
        serializer = UserSerializer(articles, many=True)
        data_member = {"ok": "true", "members": serializer.data}
        return Response(data_member)

# For Adding data to user model
class UserCreateView(CreateView):

    form_class = forms.UserForm
    model = models.UserData

# for adding data to user model
class ActivityCreateView(CreateView):

    form_class = forms.ActivityForm
    model = models.Activity
