from django.urls import include,path
from clientapp import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.TweetViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path('tweets/', include(router.urls)),
    ]
