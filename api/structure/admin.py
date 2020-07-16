from django.contrib import admin
from api.structure.models import (
    Offer,
    Application,
    UserReview,
    OfferReview
)


admin.site.register(Offer)
admin.site.register(Application)
admin.site.register(UserReview)
admin.site.register(OfferReview)
