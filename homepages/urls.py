from django.urls import path
from .views import indexPageView, dashboardPageView, infoPageView, dataRender, typePageView, loginPageView, registrationPageView, addFoodPageView, addWaterPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("visualization", dashboardPageView, name='visualization'),
    path("info", infoPageView, name='info'),
    path("test", dataRender, name='test'),
    path("type", typePageView, name='type'),
    path("login", loginPageView, name = 'login'),
    path("register", registrationPageView, name = 'register'),
    path("addFood", addFoodPageView, name ='addFood'),
    path("addWater", addWaterPageView, name = 'addWater')
]