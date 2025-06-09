from django.shortcuts import redirect, render
from demo_app.forms import CarsForm
from demo_app.models import Cars
from .forms import SignUpForm

def home(request):
    return render(request, "demo_app/home.html")

def database(request):
    #Filtering
    query = request.GET.get("search", "")
    form = CarsForm(request.POST or None) # this fetches the form from CarsForm
    cars = Cars.objects.all()
    cars_filtered = Cars.objects.filter(full_name__icontains=query) if query else None
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("database")
    else:
        return render(request, "demo_app/databases.html", {
            "form":form,
            "cars":cars,
            "search":query,
            "cars_filtered":cars_filtered}) # here the destination template is chosen and the context of the form and Cars model are passed in so data can be read 

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "demo_app/signup.html", {"form": form})
