from django.shortcuts import render
from . import forms, models
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.views.generic import CreateView

# Create your views here.
def home(request):

    return render(request, "myapp/base.html", {})


class ArticalAPIView(APIView):
    def get(self, request):
        articles = models.UserData.objects.all()
        serializer = UserSerializer(articles, many=True)
        data_member = {"ok": "true", "members": serializer.data}
        return Response(data_member)


class UserCreateView(CreateView):

    form_class = forms.UserForm
    model = models.UserData


class ActivityCreateView(CreateView):

    form_class = forms.ActivityForm
    model = models.Activity
