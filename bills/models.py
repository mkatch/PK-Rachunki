from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from decimal import Decimal

class Bill(models.Model):
    user = models.ForeignKey(User, related_name='bills')
    id = models.CharField(max_length=8, primary_key=True)
    client_name = models.CharField(max_length=127)
    client_address = models.CharField(max_length=255, blank=True)
    site = models.CharField(max_length=255, blank=True)
    issue_date = models.DateField(auto_now_add=True, editable=True, null=True, blank=True)
    begin_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tax = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('bills.views.detail', args=[self.id])

    def __unicode__(self):
        return self.id + ' ' + self.client_name


class BillEntry(models.Model):
    ITEM = 'item'
    HOUR = 'h'
    METER = 'm'
    SQUARE_METER = 'sqm'
    UNITS = (
        (ITEM, 'szt'),
        (HOUR, 'godz'),
        (METER, 'm'),
        (SQUARE_METER, 'mkw')
    )

    bill = models.ForeignKey(Bill, related_name='entries')
    description = models.TextField()
    unit = models.CharField(max_length=4, choices=UNITS, null=True)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    quantity_or_price = models.DecimalField(max_digits=11, decimal_places=2)

    @property
    def price(self):
        if self.unit is None:
            return self.quantity_or_price
        else:
            return (self.quantity_or_price * self.unit_price).quantize(Decimal('.01'))

    def __unicode__(self):
        return self.description.split('\n', 1)[0] + ' ' + str(self.price)