# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from decimal import Decimal

class Bill(models.Model):
    DRAFT = 'd'
    ISSUED = 'i'
    PAID = 'p'
    CANCELLED = 'c'
    STATES = (
        (DRAFT, 'wersja robocza'),
        (ISSUED, 'wystawiony'),
        (PAID, 'zapłacony'),
        (CANCELLED, 'anulowany')
    )

    user = models.ForeignKey(User, related_name='bills')
    client_name = models.CharField(max_length=127, blank=True)
    client_address = models.CharField(max_length=255, blank=True)
    site = models.CharField(max_length=255, blank=True)
    issue_date = models.DateField(auto_now_add=True, blank=True, null=True)
    issue_number = models.IntegerField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    tax = models.DecimalField(max_digits=4, decimal_places=2, blank=True,
                              null=True)
    state = models.CharField(max_length=1, choices=STATES)

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
    unit = models.CharField(max_length=4, choices=UNITS, blank=True)
    quantity = models.DecimalField(max_digits=11, decimal_places=2, blank=True,
                                   null=True)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2,
                                     blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True,
                                null=True)

    @property
    def total_price(self):
        if self.unit is not None and self.unit_price is not None:
            return (self.unit * self.unit_price).quantize(Decimal('.01'))
        else:
            return self.price

    def __unicode__(self):
        return self.description.split('\n', 1)[0] + ' ' + str(self.total_price)