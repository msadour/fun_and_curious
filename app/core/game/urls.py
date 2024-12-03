from rest_framework.routers import DefaultRouter

from .views import (
    RandomQuestionsEmailViewSet,
    RandomQuestionsPDFViewSet,
    RandomQuestionsViewSet,
)

router: DefaultRouter = DefaultRouter()
router.register(r"random", RandomQuestionsViewSet, basename="random")
router.register(r"random/email", RandomQuestionsEmailViewSet, basename="random_email")
router.register(r"random/pdf", RandomQuestionsPDFViewSet, basename="random_pdf")

urlpatterns: list = router.urls
