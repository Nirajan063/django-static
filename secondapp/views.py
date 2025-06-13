from django.shortcuts import render
from secondapp.forms import ContactForms
from secondapp.models import contact 
# Create your views here.

def contact_form(request):
    cf= ContactForms()
    context={
        "title": "Day 5: Contact Form",
        "form": cf
    }
    if request.method == "post":
        """pass"""
        req_first_name= request.post.get('first_name')
        req_last_name=request.post.get('last_name')
        req_email= request.post.get('email')
        req_phone_no= request.poat.get('phone_no')
        req_address= request.post.get('address')
        req_message= request.post.get('message')
        c = contact()
        c.first_name = req_first_name
        c.last_name = req_first_name
        c.phone_no = req_phone_no
        c.address = req_address
        c.email  = req_email
        c.message = req_message
        c.save()
    data = contact.objects.all()   #fetch all data from contct
    context.setdefault("data", data)
    return render(request, "contact_form.html", context)
