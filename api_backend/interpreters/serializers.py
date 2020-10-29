from rest_framework import serializers
from interpreters.models import Interpreter

class InterpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpreter
        fields = '__all__'