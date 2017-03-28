from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Debt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(validators=[MaxValueValidator(4294967295), MinValueValidator(0)])
    borrower = models.ForeignKey('auth.User', related_name='debts_as_borrower',on_delete=models.CASCADE)
    lender = models.ForeignKey('auth.User', related_name='debts_as_lender', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Debt, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
