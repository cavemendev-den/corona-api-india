from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
import pandas as pd
from . import bs
def get_head(request):
    head_info = bs.get_head_info()
    return JsonResponse(head_info,safe=False)

def get_total_state_info(request):
    states = request.GET.get("states")
    statewise_info = bs.get_statewise_info()
    if states == "all":
        statewise_info = statewise_info.T
    else:
        states = json.loads(states)
        statewise_info = statewise_info[statewise_info["id"].isin(states)]
        statewise_info = statewise_info.T
    statewise_info = statewise_info.to_dict()
    return JsonResponse(statewise_info,safe=False)


