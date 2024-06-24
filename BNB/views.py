from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from BNB.models import Worker, Customer
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    return render(request, "index.html")




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        # Handle the form submission, e.g., save the data, send an email, etc.
        return HttpResponse("Thank you for your message.")
    return render(request, 'contact.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def SignupWorker(request):
    if request.method == 'POST':
        try:
            WId = request.POST['WorkersId']
            un = request.POST['user_name']
            ps = request.POST['password']
            fn = request.POST['first_name']
            sc = request.POST['sec_name']
        except KeyError:
            # Handle missing POST parameters
            return HttpResponse('Missing POST parameters.')

        # Save the new worker data
        data = Worker(WorkersId=WId, user_name=un, password=ps, first_name=fn, sec_name=sc)
        data.save()

        # Redirect to a success page or another view
        return redirect('signin')
    else:
        return render(request, "signupSignin.html")
    

def Signin(request):
    if request.method == 'POST':
        username = request.POST['user_name']

        if Worker.objects.filter(user_name=username).exists(): 
            request.session['user_primary_key'] = username
            return redirect('dashboard')
        else:
            dict = {
                'message' : 'No Username found'
            }
            return render(request, "signupSignin.html", dict) 
    return render(request, "signupSignin.html")


from django.shortcuts import render
from .models import Customer

def index(request):
    # Fetch all bookings (customers)
    bookings = Customer.objects.all()
    
    # Pass bookings to the template
    context = {
        'bookings': bookings
    }
    
    return render(request, 'index.html', context)




def booking_view(request):
    if request.method == 'POST':
        CustId = request.POST.get('CustId')
        name = request.POST.get('name')
        pax = request.POST.get('pax')
        date = request.POST.get('date')
        time = request.POST.get('time')
        activity = request.POST.get('activity')
        
        customer = Customer(
            CustId=CustId,
            name=name,
            pax=pax,
            date=date,
            time=time,
            activity=activity
        )
        customer.save()
        return redirect('success')  # Redirect to a success page
    return render(request, 'booking.html')



def dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard.html', {'customers': customers})

def update_status(request, cust_id):
    if request.method == 'POST':
        customer = Customer.objects.get(CustId=cust_id)
        new_status = request.POST.get('status')
        customer.status = new_status
        customer.save()
    return redirect('dashboard')

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home')