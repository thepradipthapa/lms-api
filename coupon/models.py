from django.db import models
from course.models import Course
import uuid
import shortuuid



def random_coupon_code():
    return shortuuid.ShortUUID().random(length=10).upper()


# Create your models here.
class Coupon(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=10, unique=True, null=False, default=random_coupon_code)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='coupons'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.code
    

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"