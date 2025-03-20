from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import BookViewSet, BookCustomViewSet, ActionViewSet
from .views import PizzaCustomViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('custom_books', BookCustomViewSet, basename="custom_book")
router.register('common_elements', ActionViewSet, basename="common_elements")
router.register('pizza', PizzaCustomViewSet, basename='pizza')

urlpatterns = [
    # path("", views.home, name="home"),
    # path("second", views.second, name="second"),
    # path("get_data", views.get_data, name="get_data"),
    # path("api/books", views.get_books, name="get_books"),
    # path("books", views.get_books_page, name="books_page")
    # path("pizza", views.get_pizza_type, name="pizza")
    path("", include(router.urls))
]

