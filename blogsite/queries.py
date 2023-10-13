import graphene
from .types import AuthorType, PostType
from blog.models import Author, Post


class Query(graphene.ObjectType):
    feed = graphene.List(PostType)
    post = graphene.Field(PostType, postId=graphene.String())
    all_authors = graphene.Field(AuthorType)
    author = graphene.Field(AuthorType, authorId=graphene.String())

    # Resolver for feed field
    def resolve_feed(parent, info):
        return Post.objects.all().order_by('created_at')

    # Resolver for post field
    def resolve_post(parent, info, postId):
        return Post.objects.get(id=postId)

    # Resolver for all_authors field
    def resolve_all_authors(parent, info, postId):
        return Author.objects.all()

    # Resolver for author field
    def resolve_author(parent, info, authorId):
        return Author.objects.get(id=authorId)
