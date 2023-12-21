from rest_framework.routers import DefaultRouter

from .views import RandomQuestionsViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"random", RandomQuestionsViewSet, basename="random")

urlpatterns: list = router.urls
