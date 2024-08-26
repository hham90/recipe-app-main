from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
   error_message = None
   #form object with username and password fields
   form = AuthenticationForm()


   #when user hits "login" button, then POST request is generated
   if request.method == 'POST':
       #read the data sent by the form via POST request
       form =AuthenticationForm(data=request.POST)

       #check if form is valid
       if form.is_valid():
           username = form.cleaned_data.get('username')      #read username
           password = form.cleaned_data.get('password')    #read password

           #use Django authenticate function to validate the user
           user=authenticate(username=username, password=password)
           if user is not None:                    #if user is authenticated
          #then use pre-defined Django function to login
               login(request, user)
               return redirect('Recipes:list')
       else:
           error_message ='ooops.. something went wrong'   #print error message

   #prepare data to send from view to template
   context ={
       'form': form,                                 #send the form data
       'error_message': error_message                     #and the error_message
   }
   #load the login page using "context" information
   return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request) # django function to logout
    return render(request, 'auth/success.html') # redirects to success.html after logging out