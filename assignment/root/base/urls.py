from django.contrib import admin
from django.urls import path,include
from base import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('invoiceDetail',views.InvoiceDetailModelViewSet,basename='invoiceDetail')

router.register('invoice',views.InvoiceModelViewSet,basename='invoice')


urlpatterns = [
    path('',include(router.urls)),
]
