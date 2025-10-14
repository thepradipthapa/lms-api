from coupon.models import Coupon
from rest_framework.serializers import ModelSerializer

class CouponSerializer(ModelSerializer):
    # serializer for the Coupon model
    class Meta:
        model = Coupon
        fields = '__all__'