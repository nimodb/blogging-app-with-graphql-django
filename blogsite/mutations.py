import graphene
from .types import AuthorInput, AuthorType, PostInput, PostType
from blog.models import Post, Author


class AddPost(graphene.Mutation):
    class Arguments:
        input = PostInput(required=True)

    post = graphene.Field(PostType)

    def mutate(parent, info, input=None):
        if input is None:
            return AddPost(post=None)
        _post = Post.objects.create(**input)
        return AddPost(post=_post)


class AddAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    author = graphene.Field(AuthorType)

    def mutate(parent, info, input=None):
        if input is None:
            return AddAuthor(author=None)
        _author = Author.objects.create(**input)
        return AddAuthor(author=_author)


class Mutation(graphene.ObjectType):
    add_post = AddPost.Field()
    add_author = AddAuthor.Field()
