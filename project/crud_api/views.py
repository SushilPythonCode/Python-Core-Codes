from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class Personlist(APIView):

    def get(self, request, *args, **kwargs):
    # #    id = request.query_params.get('id')
       queryset = Person.objects.all()
       serializer=PersonSerializer(queryset, many=True)
       return Response(serializer.data)
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get(self, request, format=None, *args, **kwargs):
    #    id = request.query_params.get('id')
    #    queryset = Person.objects.get(id = id)
    #    serializer=PersonSerializer(queryset, many=False)
    #    return Response(serializer.data)
   


    def post(self, request, *args, **kwargs):
       serializer=PersonSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'data created'})
    #    return Response(serializer.data)
   
    def put(self, request, *args, **kwargs):
       id = request.query_params.get('id')
       p=Person.objects.get(id=id)
       serializer=PersonSerializer(p,data=request.data)
       if serializer. is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
   


    def delete(self, request, pk=None, *args, **kwargs):
       id = request.query_params.get('id')
       p=Person.objects.get(id=id)
       p.delete()
       return Response({'msg':'data deleted'})
# Create your views here.
