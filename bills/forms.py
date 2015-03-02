# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from bootstrap.widgets import (TextInput, TextArea, Select, DatePicker)
from bills.models import (Bill, BillEntry)

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = [
            'client_name',
            'client_address',
            'site',
            'issue_date',
            'begin_date',
            'end_date',
            'tax',
            'edit_token',
        ]
        widgets = {
            'client_name': TextInput(),
            'client_address': TextArea(attrs={'rows': 2}),
            'site': TextArea(attrs={'rows': 2}),
            'issue_date': DatePicker(),
            'begin_date': DatePicker(),
            'end_date': DatePicker(),
            'edit_token': HiddenInput(),
        }
        labels = {
            'client_name': _("Name"),
            'client_address': _("Address"),
            'site': _("Name/Address"),
            'issue_date': _("Issue date"),
            'begin_date': _("Begin date"),
            'end_date': _("End date"),
            'tax': _("Tax"),
        }

class BillEntryForm(ModelForm):
    class Meta:
        model = BillEntry
        fields = [
            'ord',
            'description',
            'quantity',
            'unit',
            'unit_price',
            'price'
        ]
        widgets = {
            'ord': HiddenInput(attrs={'class': 'entry-ord'}),
            'description': TextArea(attrs={'class': 'entry-description',
                                           'rows': 1}),
            'quantity': TextInput(attrs={'class': 'entry-quantity'}),
            'unit': Select(attrs={'class': 'entry-unit'}),
            'unit_price': TextInput(attrs={'class': 'entry-unit-price'}),
            'price': TextInput(attrs={'class': 'entry-price'}),
        }
        names = {
            'description': 'entry-description',
        }

    @classmethod
    def create(cls, entry):
        return cls(instance=entry, prefix=("entry%d" % entry.ord),
                   auto_id=None)


@login_required
def edit_bill(request, bill_id):
    bill = Bill.objects.get(user=request.user, id=bill_id)
    if request.method == 'GET':
        return edit_bill_get(request, bill)
    elif request.method == 'POST':
        return edit_bill_post(request, bill)


def edit_bill_get(request, bill):
    bill.increment_edit_token()
    context = {
        'bill_form': BillForm(instance=bill, auto_id='%s'),
        'entry_forms': [BillEntryForm.create(entry)
                        for entry in bill.entries.all()],
        'entry_template': BillEntryForm(auto_id=None, prefix="entry{{ord}}",
                                        initial={'ord': "{{ord}}"}),
    }
    return render(request, 'bills/edit_bill.html', context)


def edit_bill_post(request, bill):
    BillForm(data=request.POST, instance=bill).save()
    for entry in bill.entries.all():
        BillEntryForm(data=request.POST, instance=entry).save()
    return edit_bill_get(request, bill)