from rest_framework import serializers
from .models import BookModel
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        # title ni faqat harfdan iboratligini tekshirish
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Please, Enter only alphabetical chars for title!"
                }
            )
        if BookModel.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "You can not enter the same book!"
                }
            )
        return data