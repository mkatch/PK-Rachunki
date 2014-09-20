from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {'bills': request.user.bills.all}
    return render(request, 'bills/index.html', context)

@login_required
def detail(request, bill_id):
    return HttpResponse('This is bill %s detail page' % bill_id)