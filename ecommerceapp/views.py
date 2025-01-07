# from django.shortcuts import render
from rest_framework import status
from ecommerceapp.models import TourPackage
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ecommerceapp.serializer import UserRegisterSerializer,TourPackageSerializer,BookingpackageSerializer

# Create your views here.

#jwt based auth
class RegisterUser(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProtectedView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response({"message":"you are authenticated"})
    

#package creation
class TourpackageView(APIView):
    authentication_classes=[IsAuthenticated]
    def get(self,request):
        packages=TourPackage.objects.all()
        serializer=TourPackageSerializer(packages,many=True)
        return Response(serializer.data)
    
class TourpackagelistView(APIView):    
    def post(self,request):
        data=request.data
        serializer=TourPackageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        data=request.data
        obj=TourPackage.objects.get(id=id)
        serializer=TourPackageSerializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,id):
        data=request.data
        obj=TourPackage.objects.get(id=id)
        obj.delete()
        return Response({'mesage':'person deleted'})
            


class BookingpackagecreateView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=BookingpackageSerializer(data=request.data)
        if serializer.is_valid():
            booking=serializer.save(user=request.user)
            send_mail(
                subject=f"New Booking:{booking.package.name}",
                message=(
                    f"User: {booking.user.email}\n"
                    f"Package: {booking.package.name}\n"
                    f"Number of People: {booking.no_ofpeople}\n"
                    f"Travel Date: {booking.travel_date}\n"
                    f"Booking Date: {booking.book_date}"

                ),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



