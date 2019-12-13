from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.MainLoginView, name='login'),
    path('signup/', TemplateView.as_view(template_name='signup.html')),
]
