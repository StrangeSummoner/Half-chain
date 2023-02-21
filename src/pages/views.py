from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def past_projects_view(request):
    return render(request, 'pages/past-projects.html')

def services_view(request):
    return render(request, 'pages/services.html')

def about_us_view(request):
    return render(request, 'pages/about-us.html')

def mission_view(request):
    return render(request, 'pages/mission.html')

def past_events_view(request):
    return render(request, 'pages/past-events.html')

def privacy_policy_view(request):
    return render(request, 'pages/pp.html')

def terms_conditions_view(request):
    return render(request, 'pages/t&c.html')
