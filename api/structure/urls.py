from rest_framework import routers
from api.structure.views import (
    OfferViewSet,
    ApplicationViewSet,
    UserReviewViewSet,
    OfferReviewViewSet
)

router = routers.DefaultRouter()
router.register('offers', OfferViewSet, basename='offers')
router.register('applications', ApplicationViewSet, basename='applications')
router.register('user/reviews', UserReviewViewSet, basename='users_reviews')
router.register('offer/reviews', OfferReviewViewSet, basename='offers_reviews')


urlpatterns = router.urls
