# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bills.models import Bill
import json

@login_required
def clients(request):
    query = request.GET.get('q', '')
    matches = Bill.objects.filter(
        user=request.user,
        client_name__contains=query
    ).values_list(
        'client_name',
        flat=True
    )
    response = {'matches': list(matches)}
    return HttpResponse(json.dumps(response), content_type='application/json')