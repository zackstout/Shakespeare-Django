
from django.shortcuts import render

# from django.template import RequestContext
#
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

import pandas as pd

import os
from django.conf import settings

# file_path = os.path.join(settings.STATIC_ROOT, '../csvs/KingLear.csv')

# Ook we may have found it:
df = pd.read_csv('shakespeareapp/csvs/KingLear.csv', index_col=0)

# df = pd.read_csv("/Users/zackstout/Documents/Python/KingLear.csv")





def index(request):
    # return HttpResponse("<h2>ahoy</h2>")

    context = {
            'lear': df
        }

    return render(request, 'index.html', context)
