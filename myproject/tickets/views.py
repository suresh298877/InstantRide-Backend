from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import models
# Create your views here.


class ApiListCreateTickets(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tickets = models.Ticket.objects.all().order_by('-uploaded_at')
        serializer = serializers.ListCreateTicketsSerializer(
            tickets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ListCreateTicketsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
