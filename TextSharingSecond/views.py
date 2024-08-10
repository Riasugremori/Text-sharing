from django.shortcuts import render, redirect
from .models import EnteredText

def save_text(request):
    if request.method == "POST":
        entered_url = request.POST.get('entered_url')
        entered_text = EnteredText.objects.create(entered_url=entered_url)
        return redirect('view_text')
    return render(request, 'save_text.html')

def view_text(request):
    text_entry = EnteredText.objects.last()  
    return render(request, 'view_text.html', {'text_entry': text_entry})

def edit_text(request):
    text_entry = EnteredText.objects.last()  
    if request.method == "POST":
        text_entry.entered_url = request.POST.get('entered_url')
        text_entry.save()
        return redirect('view_text')
    return render(request, 'edit_text.html', {'text_entry': text_entry})
