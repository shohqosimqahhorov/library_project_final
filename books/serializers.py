from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {'status': False,
                 'message': "Kitobning sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                 }
            )

        # Check title and author from DB
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {'status': False,
                 'message': "Bu kitob ma'lumotlar omborida bor"
                 }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999:
            raise ValidationError(
                {'status': False,
                 'message': "Narx noto'g'ri"
                 }
            )
