from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class IdeaSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaSubmission
        fields = "__all__"

class QueryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = queryForm
        fields = "__all__"

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobOpening
        fields = "__all__"

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"