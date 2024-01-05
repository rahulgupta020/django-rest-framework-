from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)

    return Response({'status':200, 'payload':serializer.data})


@api_view(['POST'])
def createStudent(request):
    data = request.data

    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403, 'error':serializer.errors, 'message':'something went wrong'})    
    serializer.save()
    return Response({'status':200, 'payload':serializer.data, 'message':'Data Saved'})

@api_view(['PUT'])
def updateStudent(request, id):
    try:
        student_obj = Student.objects.get(id=id)

        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status':403, 'error':serializer.errors, 'message':'something went wrong'})    
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'Data Saved'})
    except Exception as e:
        return Response({'status':403, 'message':'Invalid ID'})


@api_view(['DELETE'])
def deleteStudent(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':200, 'message':'Data Deleted'})

    except Exception as e:
        return Response({'status':403, 'message':'Invalid ID'})
    






@api_view(['GET'])
def getBook(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    return Response({'status':200, 'payload':serializer.data})




class StudentAPI(APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({'status':200, 'payload':serializer.data})

    def post(self, request):
        data = request.data

        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'error':serializer.errors, 'message':'something went wrong'})    
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'Data Saved'})

    def put(self, request, id):
        try:
            student_obj = Student.objects.get(id=id)

            serializer = StudentSerializer(student_obj, data=request.data, partial=False)
            if not serializer.is_valid():
                return Response({'status':403, 'error':serializer.errors, 'message':'something went wrong'})    
            serializer.save()
            return Response({'status':200, 'payload':serializer.data, 'message':'Data Saved'})
        except Exception as e:
            return Response({'status':403, 'message':'Invalid ID'})
    
    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=id)

            serializer = StudentSerializer(student_obj, data=request.data, partial=False)
            if not serializer.is_valid():
                return Response({'status':403, 'error':serializer.errors, 'message':'something went wrong'})    
            serializer.save()
            return Response({'status':200, 'payload':serializer.data, 'message':'Data Saved'})
        except Exception as e:
            return Response({'status':403, 'message':'Invalid ID'})
    
    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status':200, 'message':'Data Deleted'})

        except Exception as e:
            return Response({'status':403, 'message':'Invalid ID'})
        









class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'error':serializer.errors, 'message':'something went wrong'})    
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        
        # token_obj, _ = Token.objects.get_or_create(user=user)
        # return Response({'status':200, 'payload':serializer.data, 'token': str(token_obj), 'message':'Data Saved'})

        refresh = RefreshToken.for_user(user)
        return Response({'status':200, 'payload':serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token), 'message':'Data Saved'})










from rest_framework import generics

class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGeneric1(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'