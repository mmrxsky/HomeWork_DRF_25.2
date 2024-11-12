from django.urls import path
from rest_framework.routers import SimpleRouter


from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentCreateAPIView, UserModelViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', UserModelViewSet)
urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("create/payment/", PaymentCreateAPIView.as_view(), name="create_payment"),
] + router.urls