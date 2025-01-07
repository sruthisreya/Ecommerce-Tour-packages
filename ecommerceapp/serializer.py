

from rest_framework import serializers
from .models import CustomUser,TourPackage,Bookingpackage
# from django.contrib.auth.models import User

#user serializer for creation
class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)


    class Meta:
        model=CustomUser
        fields=['id','username','password','email','phone_no']


    def create(self,validated_data):
        user=CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phone_no=validated_data['phone_no'],
            email=validated_data['email']
        )
        return user 

#package serializer
class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields='__all__'

class BookingpackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookingpackage
        fields='__all__'