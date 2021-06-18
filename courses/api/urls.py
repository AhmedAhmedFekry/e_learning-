from django.urls import path, include
from . import views
from rest_framework import routers
app_name = 'courses'
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),
        path('courses/<pk>/enroll/',
             views.CourseEnrollView.as_view(),
             name='course_enroll'),
    path('', include(router.urls)),
]