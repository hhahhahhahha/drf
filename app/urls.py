from django.urls import path
from app import views

urlpatterns = [

]

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'Snippts',views.SnipptModelviewsets,basename="Snippts")
urlpatterns += router.urls