from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bills.models import (Bill, BillEntry)


@login_required
def index(request):
    context = {'bills': request.user.bills.all}
    return render(request, 'bills/index.html', context)

@login_required
def new(request):
    bill = Bill(user=request.user)
    bill.save()
    context = {'bill': bill}
    return render(request, 'bills/edit.html', context)

@login_required
def detail(request, bill_id):
    return HttpResponse('This is bill %s detail page' % bill_id)