from rest_framework import serializers

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField()

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    description = serializers.TimeField()
    image_preview = serializers.ImageField()
    animal = AnimalSerializer(many=True)
    #animal = serializers.ManyRelatedField() #вложенный серализатор, созд.ранее
    #AssertionError: `child_relation` is a required argument.
    top_product = serializers.IntegerField()


class BookSerializer(serializers.Serializer):
    name = serializers.CharField()



class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    book_set = BookSerializer(many=True)


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField()
    book = BookSerializer(many=True)



