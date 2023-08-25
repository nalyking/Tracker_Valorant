from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import Tracker_serializer

@csrf_exempt
@api_view(("GET",))
@permission_classes((AllowAny,))
def printar(request):
    response= {
      "code": 400,
      "printar": "Hello world",
      "name": "matias" 
    }
    serializer= Tracker_serializer(response)
    return Response(serializer.data)