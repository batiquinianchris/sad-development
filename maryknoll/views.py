from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "maryknoll/index.html"

class Cash_Dashboard(generic.TemplateView):
    template_name = "maryknoll/cashier_dashboard.html"
    
class Cash_FinancialRec(generic.TemplateView):
    template_name = "maryknoll/cashier_financialrec.html"

class Cash_UserRec(generic.TemplateView):
    template_name = "maryknoll/cashier_userrec.html"

class Form_Promissory(generic.TemplateView):
    template_name = "maryknoll/form_promissory.html"

