from django.shortcuts import render, redirect
from .forms import ContactForm

def home_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    #else:
    #    form = ContactForm()
#
    #print(form.errors.as_data())
    context = {'form': form, 'form_errors': form.errors.as_data()}
    return render(request, 'pages/home.html', context)

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['full_name'])
        print(request.POST['email'])
        print(request.POST['phone_number'])
        print(request.POST['message'])
        if ContactForm(request.POST).is_valid():
            ContactForm(request.POST).save()
    else:
        print("No POST method")
    return render(request, "pages/contact.html")

def past_projects_view(request):
    return render(request, 'pages/past-projects.html')

def about_us_view(request):
    return render(request, 'pages/about-us.html')

def mission_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/mission/')
        
    return render(request, 'pages/mission.html')

def past_events_view(request):
    return render(request, 'pages/past-events.html')

def privacy_policy_view(request):
    return render(request, 'pages/pp.html')

def terms_conditions_view(request):
    return render(request, 'pages/t&c.html')

def roadmap(request):
    return render(request, 'pages/roadmap.html')
