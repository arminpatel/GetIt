from rest_framework.serializers import ModelSerializer

from .models import Product, ProductImage

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
        )

class ProductSerializer(ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'color',
            'size',
            'created_at',
            'updated_at',
            'product_images',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        filtered_images = instance.product_images.filter(product=instance)
        representation['product_images'] = ProductImageSerializer(filtered_images, many=True).data
        return representation
