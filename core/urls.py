from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns=[
    path('',views.home,name="index"),
    path('register/',views.usrreg,name="register"),
    path('login/',v.LoginView.as_view(template_name="html/login.html"),name="login"),
    path('logout/',v.LogoutView.as_view(template_name="html/logout.html"),name="logout"),
    path('changePassword/',views.changepwd,name="changePassword"),
    path('profile/',views.pfle,name="profile"),
    path('profileUpdate/',views.pfupd,name="profileUpdate"),
    path('roleRequest/',views.rolereq,name="roleRequest"),
    path('gvper/',views.gveperm, name="gvpm"),
    path('gvup/<int:t>/',views.gvupd,name="gvup"),
    path('reqdel/<int:t>',views.reqdel,name="rd"),
    path('addproduct/',views.addproduct,name="pr"),
    path('delproduct/<int:m>/',views.delproduct,name="dp"),
    path('updtproduct/<int:m>/',views.updtproduct,name="up"),
    path('viewproduct/<int:m>/',views.viewproduct,name="vp"),
    path('products/',views.allproducts,name="ap"),
    path('cart/',views.cart,name="cart"),
    path('deletecart/<int:m>/',views.deletecart,name="dc"),
    path('aboutus/',views.about,name='ab'),
    path('contactus/',views.contact,name='ct'),
    path('TermsandConditions/',views.TermsandConditions,name='tc'),
    path('buynow/<int:m>',views.buynow,name='bu'),
    path('history/<int:m>',views.history,name='his'),
]
