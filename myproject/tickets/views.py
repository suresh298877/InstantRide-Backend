from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from . import models
# Create your views here.


class ApiListCreateTickets(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        ticket_id = request.query_params.get('ticket_id')

        # If both user_id and ticket_id are provided, retrieve the specific ticket for the user
        if user_id and ticket_id:
            ticket = get_object_or_404(
                models.Ticket, pk=ticket_id, user=user_id)
            serializer = serializers.ListCreateTicketsSerializer(
                ticket)  # Do not use many=True for a single object
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If only user_id is provided, retrieve all tickets for that user
        elif user_id:
            tickets = models.Ticket.objects.filter(
                user=user_id).order_by('-uploaded_at')
            serializer = serializers.ListCreateTicketsSerializer(
                tickets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If no user_id or ticket_id is provided, retrieve all tickets
        else:
            tickets = models.Ticket.objects.all().order_by('-uploaded_at')
            serializer = serializers.ListCreateTicketsSerializer(
                tickets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.ListCreateTicketsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
