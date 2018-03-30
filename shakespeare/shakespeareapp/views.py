
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import pandas as pd

# df = pd.read_csv('../KingLear.csv', index_col=0)

# df = pd.read_csv("/Users/zackstout/Documents/Python/KingLear.csv")





def index(request):
    # return HttpResponse("<h2>ahoy</h2>")

    context = {
            'lear': df
        }

    return render(request, 'index.html', context)
