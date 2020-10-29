from interpreters.models import Interpreter
from rest_framework import viewsets, permissions
from .serializers import InterpreterSerializer

class InterpreterViewSet(viewsets.ModelViewSet):
    queryset=Interpreter.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = InterpreterSerializer