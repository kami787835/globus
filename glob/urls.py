"""
URL configuration for globus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from yasg import urlpatterns as yasg_urls
from django.conf.urls.static import static
from django.conf import settings
from register.views import QRCodeAPIView,RegisterView, LoginView,SendCodeView,VerifyPhoneView
from product.views import  ProductListAPIView,ProductDetailAPIView,CategoryListAPIView, DetailView
from histori.views import StoriesListCreateView,StoryVideosListCreateView,CardsListCreateView,CardsDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/qr_code/', QRCodeAPIView.as_view(), name='generate_qr_code'),
    path('register/register/', RegisterView.as_view(), name='register'),
    path('register/logins/', LoginView.as_view(), name='login'),
    path("register/send-code", SendCodeView.as_view(), name="send-code"),
    path("register/verify-phone", VerifyPhoneView.as_view(), name="verify-phone"),
    path('product/list', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('product/categories/', CategoryListAPIView.as_view(), name='product-categories'),
    path('product/list/<int:cat_id>/', DetailView.as_view(), name='product-list-by-category'),
    path('stor/stories/', StoriesListCreateView.as_view(), name='stories-list'),
    path('stor/stories/', StoryVideosListCreateView.as_view(), name='storyvideos-list'),
    path('cards/', CardsListCreateView.as_view(), name='cards-list'),
    path('cards/<int:pk>/', CardsDetailView.as_view(), name='cards-detail'),

]
urlpatterns += yasg_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)