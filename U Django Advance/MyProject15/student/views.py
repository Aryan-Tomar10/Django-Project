from django.shortcuts import render
from .forms import Studentform

# Create your views here.
def student_create(request):
    form = Studentform()
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student_success.html')
    return render(request, 'student_form.html', {'form':form})
        