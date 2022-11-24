from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, ImageSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.contrib.auth.models import User
from .features import CustomPagination
from django.core.exceptions import PermissionDenied
from .models import Image


class Login(LoginView):
    template_name = 'main_page.html'
    next_page = '/'


class Logout(LogoutView):
    next_page = '/'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


#################################################################################


class UserAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    """API представление для получения списка пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request):
        """Получение данных с сервера"""
        return self.list(request)

    def post(self, request, format=None):
        """Передача данных на сервер. Создание объекта"""
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            return self.create(request)


class UserDetailAPI(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """API представление для получения детальной информации о пользователе,
    а также для его редактирования и удаления"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """Получение объекта"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Изменение объекта"""
        if request.user.id == kwargs['pk']:
            return self.update(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def delete(self, request, *args, **kwargs):
        """Удаление объекта"""
        if request.user.id == kwargs['pk']:
            return self.destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied


#################################################################################


class ImageAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    """API представление для получения списка изображений"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = CustomPagination

    def get(self, request):
        """Получение данных с сервера"""
        return self.list(request)

    def post(self, request, format=None):
        """Передача данных на сервер. Создание объекта"""
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            return self.create(request)


class ImageDetailAPI(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """API представление для получения детальной информации об изображении,
    а также для его редактирования и удаления"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        """Получение объекта"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Изменение объекта"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Удаление объекта"""
        return self.destroy(request, *args, **kwargs)


#################################################################################


class DeleteAll(View):
    """Удаление всех изображений (только для администратора)"""
    def get(self, request):
        if request.user.is_superuser:
            Image.objects.all().delete()
        return redirect('/')


class GetCurrentUser(View):
    """Переход к детальной api странице текущего пользователя"""
    def get(self, request):
        return redirect(f'/users/{request.user.id}')
