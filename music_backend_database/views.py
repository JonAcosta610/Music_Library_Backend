from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from .models import Music
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)