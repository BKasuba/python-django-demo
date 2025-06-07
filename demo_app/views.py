from django.shortcuts import redirect, render
from demo_app.forms import CarsForm

def home(request):
    return render(request, "demo_app/home.html")

def database(request):
    form = CarsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("database")
    else:
        return render(request, "demo_app/databases.html", {"form":form})
