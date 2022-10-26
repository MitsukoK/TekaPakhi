from django.urls import path
from .views import MobileRecharge

urlpatterns = [
    path("mobilebank/", MobileRecharge.as_view(), name="mobile_bank"),
    # path("bank/", admin.site.urls),
    # path("giftcard/", admin.site.urls),
    # path("recharge/", admin.site.urls),
]
