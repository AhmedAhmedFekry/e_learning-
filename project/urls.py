"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include
from django.contrib.auth import views as auth_views
from courses import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.CourseListView.as_view(), name='course_list'),
     path('api/', include('courses.api.urls', namespace='api')),
    path('accounts/login/', auth_views.LoginView.as_view(),
    name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
    name='logout'),
    path('admin/', admin.site.urls),
      path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)