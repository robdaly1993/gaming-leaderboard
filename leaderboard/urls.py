"""
URL configuration for leaderboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect
from leaderboard_app.views import home, leaderboard  # Import the home and leaderboard views




urlpatterns = [
    # Redirect the root URL to leaderboard_app
    path("", lambda request: HttpResponseRedirect("leaderboard_app/")),
    
    # Admin interface
    path("admin/", admin.site.urls),
    
    path("leaderboard/", leaderboard, name="leaderboard"),

    
    # Include URLs from leaderboard_app
    path("leaderboard_app/", include("leaderboard_app.urls")),
]

