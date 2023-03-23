from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer


class InvoiceAPITestCase(APITestCase):
     def test_get_all_invoices(self):
        url = reverse('invoice-list')
        response = self.client.get(url)
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


     



# Create your tests here.
