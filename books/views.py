from .models import BookModel
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# class BookListApiView(generics.ListAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


# class BookListCreateApiView(generics.ListCreateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


class BookApiView(APIView):

    def get(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            serializer = BookSerializer(book).data
            data = {
                "status": "success",
                "data": serializer
            }
            return Response(data,
                            status=status.HTTP_200_OK
                            )
        except Exception:
            return Response(
                {
                    "status": "False",
                    "message": "Book is not found",
                 },
                status=status.HTTP_404_NOT_FOUND
            )


class BooksListApiView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True).data
        data = {
            "status": "success",
            "data": serializer
        }
        return Response(data)


class BookCreateApiView(APIView):
    def post(self, request):
        book = request.data
        serializer_data = BookSerializer(data=book)
        if serializer_data.is_valid():
            serializer_data.save()
            data = {
                "status": "success",
                "data": book
            }
            return Response(data)
        # else:
        #     msg = {
        #         "status": False,
        #         "message": "data is not valid."
        #     }
        #     return Response(msg)


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    "status":True,
                    "message": "Successfully deleted."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {
                    "status": "False",
                    "message": "Book is not found",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        books = BookModel.objects.all()
        book = generics.get_object_or_404(books, id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                "message": f"book id-{pk} updated to {book_saved}."
            }
        )


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#
# class BookDetailUpdateDeleteApiView(generics.RetrieveUpdateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


