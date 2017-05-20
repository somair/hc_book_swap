from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from books import views
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^contact/', TemplateView.as_view(template_name='static_pages/contact.html'), name='contact'),
    url(r'^disclaimer/', TemplateView.as_view(template_name='static_pages/disclaimer.html'), name='disclaimer'),
    url(r'^', include('books.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = TemplateView.as_view(template_name='static_pages/404.html')