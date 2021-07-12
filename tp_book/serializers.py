from rest_framework import serializers

from tp_book.models import Book


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=150)
#     name = serializers.CharField(max_length=50)
#     desc = serializers.TextField()
#     image = serializers.ImageField(upload_to='store_image',default='',null=True,blank=True)
#     fav = serializers.BooleanField(default=False)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id','author','name','desc','image','fav']

        extra_kwargs = {

            'id': {
                'read_only': True,
            },


        }
