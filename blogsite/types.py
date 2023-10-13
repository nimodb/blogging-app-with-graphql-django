import graphene
from graphene_django import DjangoObjectType, DjangoListField
from blog.models import Author, Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "created_at")


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name", "biodata")

    posts = DjangoListField(PostType)

    def resolve_posts(self, info):
        return Post.objects.filter(author=self.id)

# Input Object Types for New Post


class PostInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    created_at = graphene.Date()
    author_id = graphene.String(required=True, name="author")

# Input Object Types for New Author


class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    biodata = graphene.String()
