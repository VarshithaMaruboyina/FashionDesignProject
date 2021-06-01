from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from .forms import dregisterform,dloginform,designsform
from .models import dregister,designs
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings
from payment.models import payment

from .utils import getplot,getgraph

def dregisterfunction(request):
	if request.method=='POST':
		form=dregisterform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			gmail=form.data['gmail']
			subject="welcome"
			email=EmailMessage(subject,"welecome to our digital fashion.I hope our app will be  helpfull to you     -f3 team",to=[gmail]) 
			email.send()
			return redirect("dlogin")
			
	else:
		form=dregisterform()
	return render(request,"dregister.html",{'form':form})

def dloginfunction(request):
	if request.method=='POST':
		form=dloginform(request.POST)
		if form.is_valid():
			gmail=form.data["gmail"]
			password=form.data["password"]
			check=dregister.objects.filter(Q(gmail=gmail)&Q(password=password))
			if check:
				request.session['gmail']=gmail
				return redirect("designerhome")
			else:
				return HttpResponse("login unsucessfull")
	else:
		form=dloginform()
	return render(request,"dlogin.html",{'form':form})
def designerhomefunction(request):
	gmail=request.session['gmail']
	designerdata=dregister.objects.filter(Q(gmail=gmail))
	designsdata=designs.objects.filter(Q(gmail=gmail))
	if request.method=='POST':
		form=designsform(request.POST,request.FILES)
		if form.is_valid():
			form1=form.save(commit=False)
			form1.gmail=gmail
			for d in designerdata:
				form1.name=	d.name
			form1.save()
			return redirect('designerhome')
	else:
		form=designsform()
	return render(request,"designerhome.html",{'data':designerdata,'form':form,'ddata':designsdata,})

def deleteimagefunction(request , sid):
	gmail=request.session['gmail']
	designs.objects.filter(id=sid).delete()
	return redirect('designerhome')

def logoutfunction(request):
	try:
		del request.session['gmail']
		return redirect('mainhome')
	except KeyError:
		pass

def ordersfunction(request):
	gmail=request.session['gmail']
	data=payment.objects.filter(Q(dgmail=gmail))
	return render(request,"orders.html",{'data':data,})



def graphs(request):

	data =  designs.objects.filter().all()

	y_data = [int(x.price) for x in data]

	x_data = [str(x.DesignName) for x in data]

	chart = getplot(x_data,y_data)


	return render(request, 'designer/graph.html', {'chart':chart})







