from django.shortcuts import render, redirect
from .models import Ticket, Comment
from django.http import HttpResponseRedirect


def tickets(request):
    tickets = Ticket.objects.order_by('title')
    comments = Comment.objects.get()
    return render(request, 'ticket/tickets.html', {'tickets': tickets}, {'comments': comments})


def delete(request, ticket_id):
    item = Ticket.objects.get(pk=ticket_id)
    item.delete()
    return redirect('/')


def show(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    comment = Comment.objects.get(pk=ticket_id)
    return render(request, 'single_ticket.html', {'ticket': ticket}, {'comment': comment})
