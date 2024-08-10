from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Car, Review
from rest_framework import viewsets
from .models import Car, Review
from .serializers import CarSerializer, ReviewSerializer


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/car_form.html'
    fields = ['brand', 'model', 'year', 'price', 'description', 'image']
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'cars/car_form.html'
    fields = ['brand', 'model', 'year', 'price', 'description', 'image']
    success_url = reverse_lazy('car_list')

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'cars/review_form.html'
    fields = ['user', 'car', 'rating', 'comment']
    success_url = reverse_lazy('car_detail')
# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer