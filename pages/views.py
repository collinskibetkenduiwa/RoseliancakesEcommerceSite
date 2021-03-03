from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User_Contacts

def contact(request): 
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Phone = request.POST["phone"]
        Subject = request.POST["subject"]
        Message = request.POST["message"]
        
        user_query = User_Contacts(Name=Name,Email=Email,Phone=Phone,Subject=Subject,Message=Message)
        user_query.save()
        messages.success(request, 'Message Sent,We will communicate soon') 
        return redirect('/contact#success')            
    return render(request,'contact.html',)

def home_redirect(request):
    
    return redirect('/home/')
