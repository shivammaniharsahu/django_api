from django.urls import path, include
from workshop import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', views.RegisterView)
urlpatterns = [
    path('', include(router.urls))
]
