from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Logs out user and sends browser to homepage."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index')) # there is no escaping the localhost:8000/users/ without reverse()
                                                       # reverse() gets the url pattern including the directory
                                                       # before it, '' , using the url name 'index'.

def register(request):
    """Register a new user."""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save() # returns a user object
            # Log the user in and then redirect to the homepage.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
    # if u dont put it in this syntax, it returns an error regarding the request variable when you
    # try to make a user with the same name as another user.
    # the if statement in the else statement exits and returns to the next steps, that's the reason why.