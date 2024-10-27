from rest_framework.serializers import ModelSerializer
from .models import Blog, Comment


class Commentserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields ="__all__"


# This is nested serializers (Commentserializer inside a blogserializer)
class Blogserializer(ModelSerializer):
    comments = Commentserializer(many = True, read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"        