from rest_framework import serializers

from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.category:
            representation['category'] = instance.category.title
        representation['likes'] = instance.likes.all().count()

        action = self.context.get('action')
        if action == 'retrieve':
            # детализация
            representation['comment'] = CommentSerializer(instance.comments.all(), many=True).data
        else:
            representation['comment'] = instance.comments.all().count()
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('product', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        return representation
