from rest_framework import serializers

from .models import user,product


class reisterserializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=user
        fields=['email','password','is_approved','is_admin']
        read_only_fields=['is_approved','is_admin']

    def create(self,validates_data):
        user=user.objects.create_user(
            email=validates_data['email'],
            password=validates_data['password']
        )
        return user    


class userSerialzer(serializers.ModelSerializer):

    
    class Meta:
        model=user
        fields=['id','username','email','is_approved','is_admin']

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['id','name','description','price','user']

        