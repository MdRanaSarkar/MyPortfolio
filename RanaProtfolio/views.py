from django.shortcuts import render,HttpResponseRedirect,redirect
from RanaProtfolio.models import Specialization, Service, WorkingCategory, WorkingProtfolio, Item, Working_Experience, ContacttForm, Contact
from django.contrib import messages

import datetime
today = datetime.date.today()
# Create your views here.


def Home(request):
	items = Specialization.objects.all()
	services = Service.objects.all()
	working_prot = WorkingProtfolio.objects.all()
	youtube = Item.objects.all().order_by('-id')[:6]
	experience_w = Working_Experience.objects.all().order_by('-id')[:6]
	client_says=Contact.objects.filter(status='True')
	if request.method == 'POST':
		form = ContacttForm(request.POST or None)
		if form.is_valid():
			data=form.save(commit=False)
			"""
			data = Contact()
			data.name = form.cleaned_data['name']
			data.email = form.cleaned_data['email']
			data.subject = form.cleaned_data['subject']
			data.comment = form.cleaned_data['message']
			data.ip = request.META.get('REMOTE_ADDR')
			"""
			data.save()
			messages.success(request, 'Your message has been sent')
			return redirect('home')
	form = ContacttForm()
	context={
	'items':items,
	'services':services,
	'working_prot':working_prot,
	'youtube':youtube,
	'experience_w':experience_w,
	'client_says':client_says,
	'form':form,

	}
	return render(request,'home.html',context)



def Specialized(request):
	items=Specialization.objects.all()
	context={'items':items}
	return render(request,'specialization.html',context)



 
def services_individual(request,id):
	services= Service.objects.get(id=id)
	context={'services':services}
	return render(request,'service-single.html',context)


def WorkingProtfolio_individual(request,id):
	protfolio= WorkingProtfolio.objects.get(id=id)
	context={'protfolio':protfolio}
	return render(request,'portfolio-single.html',context)

def Youtubev(request):
	items=Item.objects.all()
	context={'items':items}
	return render(request,'service-single.html',context)


# this is the for working experience class

def WrokingEx(request):
	items=Working_Experience.objects.all()
	context={'items':items}
	return render(request,'working_experience.html',context)
