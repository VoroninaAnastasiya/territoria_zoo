from rest_framework import serializers

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField()

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    description = serializers.TimeField()
    image_preview = serializers.ImageField()
    #animal = serializers.ManyRelatedField() #вложенный серализатор, созд.ранее, сделаем опциональным required=False
    #AssertionError: `child_relation` is a required argument.
    top_product = serializers.IntegerField()

