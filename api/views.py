from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PesronModelSerializer
from . models import Person
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


# ////////////////////// VIEWSETS /////////



class PersonViewsets(viewsets.ViewSet):


    def list(self,request):
        data = Person.objects.all()
        serializer=PesronModelSerializer(data,many=True)
        return Response(serializer.data)
    


    def retrive(self,req,pk=None):
        id=pk
        if pk is not None:
            data=Person.objects.get(id=id)
            serializer=PesronModelSerializer(data,many=True)
            return Response(serializer.data)
    
    

    def create(self,req):
        data =req.data
        serializer=PesronModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg:":"data added","data":serializer.data},status=status.HTTP_200_OK)
        return Response('not added',status=status.HTTP_404_NOT_FOUND)
        


    def update(self,req,pk= None):
            id=pk
            if id is not None:
                obj=Person.objects.get(id=id)
                serializer=PesronModelSerializer(obj,data=req.data,partial=False)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)



    def partial_update(self,request,pk=None):

        if pk is not None:
                obj=Person.objects.get(id=pk)
                serializer=PesronModelSerializer(obj,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)




    def delete(self,request,pk=None):
        if pk is not None: 
            obj=Person.objects.get(id=pk)
            obj.delete()

            return Response({'msg':'data deleted'})