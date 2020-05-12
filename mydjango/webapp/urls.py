from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emp',views.EmployeeViewSet,'emp')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path ('generic/emp/', views.EmployeeGenericAPIView.as_view()),
    path ('generic/emp/<int:id>/', views.EmployeeGenericAPIView.as_view())
    #path ('emp/<int:id>/', views.EmployeeDetailAPIView.as_view())
    # path ('emp/', views.EmployeeAPIView.as_view()),
    # path ('emp/<int:id>/', views.EmployeeDetailAPIView.as_view())
    # path('emp/',views.employee_list_view),
    # path('emp/<int:pk>/',views.employee_detail)
]