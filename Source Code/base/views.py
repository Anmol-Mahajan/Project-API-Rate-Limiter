"""
Implements a response upon user requesting API functionality
"""

from django.shortcuts import render, redirect, reverse
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import RateLimits
import datetime
from django.utils import timezone
"""
@user: Authenticated user fetched from the database 
@url: API(dev/org) exposed to user
@return: JSON object representing present state
"""
def HomePage(request):
	return render(request,'home.html')
def RateLimitChecker(user, url):

    rateLimitObj = RateLimits.objects.filter(user = user, url = url) #fetches all the rows from RateLimits table satisfying user, url constraint

    count = 1 #Initialization of API Hits

    if(len(rateLimitObj) == 0): #user not found

        maxrate = 10 #Default limit for org API

        if(url == "dev"):  
            maxrate = 5 #Default limit for dev API

        rateLimitObj = RateLimits.objects.create(user = user, url = url, count = 1, maxrate = maxrate) #Adds a new user entry to RateLimits table

    else:
        rateLimitObj = rateLimitObj[0] #fetches already present user from rateLimitObj

        #We are working with a window size of 40 seconds for illustration purposes
        if(timezone.now() - rateLimitObj.lastupdated  < datetime.timedelta(seconds = 40)): #Allows requests per 40 seconds

            if(rateLimitObj.count >= rateLimitObj.maxrate):
                response_data = {
                    "success":False,
                    "message":"Rate exceeded"
                }
                return response_data

            else:
                count = rateLimitObj.count + 1
                rateLimitObj.count = count
                #rateLimitObj.lastupdated = datetime.datetime.now()
                rateLimitObj.save()

        else:
            #Reset upon window expiration
            count = 1
            rateLimitObj.count = 1
            rateLimitObj.lastupdated = datetime.datetime.now()
            rateLimitObj.save()

    response_data = {
        "success":True,
        "message":"Success",
        "count":count
    }
    return response_data


class ApiFirst(APIView):

    def post(self,request,format = None):
        response_data = RateLimitChecker(request.user, "dev")
        return Response(response_data,status=status.HTTP_200_OK)

class ApiSecond(APIView):

    def post(self,request,format = None):
        response_data = RateLimitChecker(request.user, "org")
        return Response(response_data, status = status.HTTP_200_OK)
