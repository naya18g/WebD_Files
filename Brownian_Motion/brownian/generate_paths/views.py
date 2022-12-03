from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import brownian
from . import geometric_brownian

# MatPlotLib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import math

req_vals = {}
def form(request):
 
    # logic of view will be implemented here
    
    return render(request, "form.html")

def index(request):
    req_vals = request.POST
    brownian.brownian_motion_path(req_vals['end_time1'], req_vals['num_path1'])
    s,mu,sgma,SS,t =geometric_brownian.geometric_brownian_motion(req_vals['init_val'],req_vals['end_time2'],req_vals['Mu'],req_vals['sigma'],req_vals['num_path2'])
    mean_t,mean_c,var_t,var_c,t = geometric_brownian.cal_mean_var(req_vals['init_val'],req_vals['Mu'],req_vals['sigma'],SS,req_vals['end_time2'])

    return render(request, "index.html" , {'mean_t': mean_t ,'mean_c': mean_c,'var_t': var_t,'var_c': var_c, 'time':t})