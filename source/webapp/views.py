from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


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


@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('Deleted')
