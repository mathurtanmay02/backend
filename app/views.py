from django.shortcuts import render
from django.http import HttpResponse
# from .models import information

# Create your views here.

def index(request):
    return render(request, "app/index.html")

# def connection(request):
#     if request.method == "POST":
#         companyName = request.POST["companyName"]
#         personName = request.POST["companyName"]

#         if companyName is None and personName is None:
#             "details" : information.objects.all()
#         elif companyName is None:
#             "details" : information.objects.filter(companyName = companyName)
#         elif personName is None:
#             "details" : information.objects.filter(personName = personName)
#         else:
#             "details" : information.objects.filter(personName = personName).filter(companyName = companyName)

#         return render(request, "app/connection.html", {
#             "details"
#         })