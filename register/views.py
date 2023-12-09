from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
            user = User.objects.get(username=uname)
            shop_group = Group.objects.get(name='ShopMember')
            user.groups.add(shop_group)
            user.save()
            return redirect('login')

        return redirect("index.html")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

