from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('ideas/', IdeaSubmissionView.as_view()),
    path('query/', queryFormView.as_view()),
    path('jobs/', jobOpeningView.as_view()),
    path('jobApply/', JobApllicationView.as_view()),
]
router = DefaultRouter()
router.register(r'', BlogViewset, "blogs")

urlpatterns += router.urls



 