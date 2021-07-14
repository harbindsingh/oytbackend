from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, views, status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response

from .models import *
from .serializers import *

class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IdeaSubmissionView(generics.CreateAPIView):
    queryset = IdeaSubmission.objects.all()
    serializer_class = IdeaSubmissionSerializer
    permission_classes = [permissions.AllowAny]

class queryFormView(generics.CreateAPIView):
    queryset = queryForm.objects.all()
    serializer_class = QueryFormSerializer
    permission_classes = [permissions.AllowAny]

class jobOpeningView(generics.ListAPIView):
    queryset = jobOpening.objects.all()
    serializer_class = JobOpeningSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class JobApllicationView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = JobApplication.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        jASerializer = JobApplicationSerializer(data=request.data)

        if jASerializer.is_valid():
            jASerializer.save()
            return Response(jASerializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', jASerializer.errors)
            return Response(jASerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    