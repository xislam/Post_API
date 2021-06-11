from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(date=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def post_update(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def like_add(request, pk):
    post = Post.objects.get(id=pk)
    post.vote_count += 1
    post.save()
    return Response(status=HTTP_200_OK)



@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('Deleted')


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request):
    serializer = CommentSerializer(date=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def comment_update(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()

    return Response('Deleted')
