from django.urls import path

from . import views

urlpatterns = [
    path('', views.labelView, name='index'),
    path('<int:content_id>/vote/<int:vote_key>', views.vote, name='vote'),

]