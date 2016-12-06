from rest_framework.serializers import ModelSerializer

from product.models import Product


class PostListSerializer(ModelSerializer):
    # url = post_detail_url
    # user = UserDetailSerializer(read_only=True)
    # image = SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'model',
            'ownername',
            'charge_perhour',
            'charge_perday',
            'charge_perweek',

        ]


class ProductCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'charge_perhour',
            'charge_perday',
            'charge_perweek',
        ]

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'charge_perhour',
            'charge_perday',
            'charge_perweek',
        ]

