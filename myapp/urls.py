from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path("", views.main, name="shophome"),
    path("about/", views.about, name="aboutUs"),
    path("contact/", views.contact, name="Contactme"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("productview/", views.product, name="productview"),
    path("checkout/", views.checkout, name="checkout"),
]
