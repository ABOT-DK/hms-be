from rest_framework.routers import DefaultRouter
from .views import LabResultViewSet


router = DefaultRouter()
router.register('', LabResultViewSet, basename='labresults')
urlpatterns = router.urls