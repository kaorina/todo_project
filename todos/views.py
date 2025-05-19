from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def index(request):
    return render(request, 'todos/index.html')
