# from django.shortcuts import render
from rest_framework import generics
from models import Contacts
from serializers import ContactsSerializer


class ContactsListViewAPI(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsRetrieveUpdateDestroyViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer



    