from django.urls import path
from .import views


urlpatterns = [
    path('', views.adminsite, name='adminsite'),
    path('base', views.base, name='base'),
    path('nav',views.navbar, name='navbar'),
    path('footer', views.footer, name='footer'),
    path('doc_registration',views.doc_registration , name='doc_registration'),
]