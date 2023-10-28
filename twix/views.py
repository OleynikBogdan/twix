from django.shortcuts import render
from .forms import RecordForm
from .models import Record

# Create your views here.
def index(request):
    all_records = Record.objects.all()
    
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
    return render(request, "twix/index.html", {"form": form, 'all_records': all_records})
