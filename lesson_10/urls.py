from django.urls import include, path
from rest_framework import routers
from lesson_10 import views

router = routers.SimpleRouter()
router.register(r'view-set', views.ViewSetAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('function/', views.view_function, name='function_view'),
    path('class/', views.ClassAPIView.as_view(), name='class_view'),
    path('generic/', views.MyCreateAPIView.as_view(), name='generic'),
    path('retrieve/<int:pk>', views.MyRetrivierAPIView.as_view(), name='retrieve'),
    path('retrieve-update/<int:pk>', views.MyRetrevierUpdateAPIView.as_view(), name='retrieve_update'),
    path('api-login', views.user_login),
    path('create-user', views.CreateUser.as_view()),
]