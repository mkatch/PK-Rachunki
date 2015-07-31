# -*- coding: utf-8 -*-

from django.shortcuts import (render, redirect)
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
    print(bill.edit_token)
    return redirect('edit', bill_id=bill.id)

@login_required
def detail(request, bill_id):
    if request.method == "GET":
        return HttpResponse("This is bill %s detail page" % bill_id)
    elif request.method == "POST":
        return HttpResponse("This is bill %s detail page POST" % bill_id)

@login_required
def edit(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    context = {'bill': bill}
    return render(request, 'bills/edit.html', context)