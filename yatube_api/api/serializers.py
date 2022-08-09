from rest_framework import serializers

from posts.models import Post, Group, User, Comment


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    model = User

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=False, required=False)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    post = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Post.objects.all(),
        required=True
    )
    post = Post.objects.prefetch_related('comments')

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'created', 'id')
