from rest_framework import routers
from api.chat.views import MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet, basename='messages')


urlpatterns = router.urls
