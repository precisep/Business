from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "affiliate"
urlpatterns = [
    path("", views.home, name = "home.html"),
    path('about/',views.about, name = "about.html"),
    path('contact/',views.contact, name = "contact.html"),
    path('entertainment/',views.entertainment, name = "entertainment.html"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
