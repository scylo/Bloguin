from rest_framework import serializers
from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Comment
      fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
   # mostra os comentários de cada post(não foi pedido no teste)
   # comments = CommentSerializer(many=True, read_only=True)

   class Meta:
      model = Post
      fields = ('__all__')
