from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core import serializers


class SignUpView(APIView):
    def post(self, request):
        serializer = serializers.UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully", "user": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
