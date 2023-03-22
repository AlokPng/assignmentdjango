from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views he
class InvoiceDetailModelViewSet(viewsets.ModelViewSet) :
    queryset=InvoiceDetail.objects.all()
    serializer_class=InvoiceDetailSerializer
class InvoiceModelViewSet(viewsets.ModelViewSet) :
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
