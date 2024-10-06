from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import cash_entry_form
# Create your views here
def app_view(request):
     form = cash_entry_form(request.POST)
     if form.is_valid():
         data = form.save(commit=False)
         data.save()
         return redirect('cash_entry')
     else:
         form = cash_entry_form()
     return render(request, 'index.html', {'form':form})
 
 