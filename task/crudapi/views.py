from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets,permissions,status,generics
from.serialzers import userSerialzer,productSerializer,reisterserializer
from.models import user,product
from rest_framework.authtoken.views import ObtainAuthToken

class registerview(generics.CreateAPIView):
    serializer_class=reisterserializer


class UserViewSet(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class=userSerialzer
    permission_classes=[permissions.IsAdminUser]


    def create(self,request,*args,**kwargs):
        serialzers=self.get_serializer(data=request.data)
        serialzers.is_valid(raise_exception=True)
        self.perform_create(serialzers)
        headers=self.get_success_headers(serialzers.data)
        return Response(serialzers.data,status=status.HTTP_201_CREATED,headers=headers)
    
    def Perform_create(self,serializer):
        serializer.save(user=self.request.user)
    



class Productviewset(viewsets.ModelViewSet):
    serializer_class=productSerializer


    def get_queryset(self):
        if self.request.user.is_admin:
            return product.objects.all()
        return product.objects.filter(user=self.request.user)
    
    def Perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer,instance):
        if instance.user==self.request.user or self.request.user.is_admin:
            serializer.save()
        else:
            raise permissions.DjangoObjectPermissions()    

    def Perform_delete(self,instance):
        if instance.user==self.request.user or self.request.user.is_admin:
            instance.delete()
        else:
            raise permissions.DjangoObjectPermissions()        



