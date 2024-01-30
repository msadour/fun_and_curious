from rest_framework.routers import DefaultRouter

from .views import ManageProfileViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"manage", ManageProfileViewSet, basename="manage_profile")

urlpatterns: list = router.urls