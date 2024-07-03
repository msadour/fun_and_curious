from rest_framework.routers import DefaultRouter

from .views import GameProfileViewSet, ManageProfileViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"manage", ManageProfileViewSet, basename="manage_profile")
router.register(r"my_games", GameProfileViewSet, basename="my_games")

urlpatterns: list = router.urls
