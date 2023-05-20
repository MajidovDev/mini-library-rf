from django.urls import path
from .views import BookApiView, BooksListApiView, BookCreateApiView, BookDeleteApiView, BookUpdateApiView, BookViewSet

# app_name = 'api'
# urlpatterns = [
#     path('books/<int:pk>/', BookApiView.as_view(), name="book"),
#     path('books/', BooksListApiView.as_view(), name="books"),
#     path('books/create/', BookCreateApiView.as_view(), name="create"),
#     path('books/delete/<int:pk>/', BookDeleteApiView.as_view(), name="delete"),
#     path('books/update/<int:pk>/', BookUpdateApiView.as_view(), name="update"),
#
#     # path('books/list-create/', BookListCreateApiView.as_view(), name="list-create"),
#     # path('books/detail-update-delete/<int:pk>/', BookDetailUpdateDeleteApiView.as_view(), name="detail-update-delete"),
#     # path('books/<int:pk>/detail/', BookDetailApiView.as_view(), name="detail"),
#     # path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name="delete"),
#     # path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name="update"),
#
# ]

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = router.urls

