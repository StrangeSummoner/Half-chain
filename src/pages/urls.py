from django.urls import path
from . import views

app_name = 'pages-app'
urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('contact/', views.contact_view, name='contact-view'),
    path('past-projects/', views.past_projects_view, name='past-projects-view'),
    path('services/', views.services_view, name='services-view'),
    path('about-us/', views.about_us_view, name='about-us-view'),
    path('mission/', views.mission_view, name='mission-view'),
    path('past-events/', views.past_events_view, name='past-events-view'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy-policy-view'),
    path('terms-conditions/', views.terms_conditions_view, name='terms-conditions-view'),
]