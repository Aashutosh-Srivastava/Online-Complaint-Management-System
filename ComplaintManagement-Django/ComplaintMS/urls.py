"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns=[
   re_path(r'^$',views.index,name='index'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^signin/$',auth_views.LoginView.as_view(template_name='ComplaintMS/signin.html'), name='signin'),
    re_path('logout/', auth_views.LogoutView.as_view(template_name='ComplaintMS/logout.html'), name='logout'),
    re_path(r'^password/$', views.change_password, name='change_password'),
    re_path(r'^passwords/$', views.change_password_g, name='change_password_g'),
    re_path(r'^counter/$', views.counter, name='counter'),
    re_path(r'^solved/$', views.solved, name='solved'),



    re_path(r'^login/$',views.login,name='login'),
    re_path(r'^list/$',views.list,name='list'),
    re_path(r'^pdf/$',views.pdf_view,name='view'),
    re_path(r'^pdf_g/$',views.pdf_viewer,name='view'),
    re_path(r'^aboutus/$',views.aboutus,name='aboutus'),

    re_path(r'^login_redirect/$',views.login_redirect,name='login_redirect'),
    re_path(r'^slist/$',views.slist,),




    #url(r'^login2/$',views.login2,name='login2'),

    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),
    re_path(r'^complaints/$', views.complaints, name='complaints'),
    re_path(r'^allcomplaints/$', views.allcomplaints, name='allcomplaints'),


       re_path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='ComplaintMS/password_reset.html'
         ),
         name='password_reset'),
    re_path(r'^password-reset-done/$',
         auth_views.PasswordResetDoneView.as_view(
             template_name='ComplaintMS/password_reset_done.html'
         ),
         name='password_reset_done'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='ComplaintMS/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    re_path(r'^password-reset-complete/$',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='ComplaintMS/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
   ]
