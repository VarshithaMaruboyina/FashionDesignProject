from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from .forms import uregisterform,uloginform
from .models import uregister
from designer.models import designs,dregister
from bag.models import bag
from bag.forms import bagform
from payment.models import payment
from payment.forms import paymentform
from django.db.models import Q

# Create your views here.
def uregisterfunction(request):
	if request.method=='POST':
		form=uregisterform(request.POST)
		if form.is_valid():
			form.save()
			return redirect("ulogin")
	else:
		form=uregisterform()
	return render(request,"uregister.html",{'form':form})

def uloginfunction(request):
	if request.method=='POST':
		form=uloginform(request.POST)
		if form.is_valid():
			gmail=form.data["gmail"]
			password=form.data["password"]
			check=uregister.objects.filter(Q(gmail=gmail)&Q(password=password))
			if check:
				request.session['gmail']=gmail
				return redirect("userhome")
			else:
				return HttpResponse("login unsucessfull")
	else:
		form=uloginform()
	return render(request,"ulogin.html",{'form':form})

def userhomefunction(request):
	return render(request,"userhome.html")

def partywearfunction(request):
	designsdata=designs.objects.filter(Q(designtype='partywear'))
	return render(request,"partywear.html",{'data':designsdata,})

def traditionalfunction(request):
	designsdata=designs.objects.filter(Q(designtype='traditional'))
	return render(request,"traditional.html",{'data':designsdata,})

def dlogoutfunction(request):
	try:
		del request.session['gmail']
		return redirect('mainhome')
	except KeyError:
		pass

def designersfunction(request):
	data=dregister.objects.all();
	return render(request,"designers.html",{'data':data,})

def viewfunction(request,iid):
	u=designs.objects.filter(Q(id=iid))
	if request.method=='POST':
		form=bagform(request.POST)
		if form.is_valid():
			gmail=request.session['gmail']
			for g in u:
				pid=g.id
			form1=form.save(commit=False)
			form1.gmail=gmail
			form1.pid=pid
			form1.save()
			return redirect("cart")
	else:
		form=bagform(request.POST)
	return render(request,"view.html",{'data':u,'formdata':form,})

def cartfunction(request):
	gmail=request.session["gmail"]
	data=bag.objects.filter(Q(gmail=gmail))
	ddata=[]
	for d in data:
		ddata+=designs.objects.filter(Q(id=d.pid))
	sum=0;
	for i in ddata:
		sum=sum+i.price;
	mylist=zip(data,ddata)
	return render(request,"cart.html",{'list':mylist,'sum':sum,})

def cartdeletefunction(request,cid):
	bag.objects.filter(id=cid).delete()
	return redirect('cart')
def paymentfunction(request):
	gmail=request.session["gmail"]
	data=bag.objects.filter(Q(gmail=gmail))
	"""obj=[]
	for i in data:
		obj+=designs.objects.filter(Q(id=i.pid))"""
	if request.method=='POST':
		form=paymentform(request.POST)
		if form.is_valid():
			form1=form.save(commit=False)
			for i in data:
				form1.ugmail=i.gmail
				form1.pid=i.pid
				form1.size=i.size
				form1.chestsize=i.chestsize
				form1.waistsize=i.waistsize
				form1.sleevelength=i.sleevelength
				form1.shoulderlength=i.shoulderlength
				form1.neckdepth=i.neckdepth
				obj=designs.objects.filter(Q(id=i.pid))
				for o in obj:
					form1.price=o.price
					form1.dgmail=o.gmail
				form1.save()
			return HttpResponse("<h1>Payment Sucessfull</h1>")
	else:
		form=paymentform()
	return render(request,'payment.html',{'form':form})







