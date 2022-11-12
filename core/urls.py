
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path("alltires/",views.alltires,name='alltires'),
    path("productDetails/<int:id>",views.productDetails,name='productDetails'),
    path("learn/",views.learn,name='learn'),
    path("search/",views.search,name='search'),
    path("login/",views.loginUser,name='login'),
    path("register/",views.registerUser,name='register'),
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('address/',views.address,name="address"),
    path('map/',views.map,name="map"),
    path('cart/', views.cart, name='cart'),
    path('showcart/', views.showcart, name='showcart'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('minuscart/', views.minuscart, name='minuscart'),
    path('removecart/', views.removecart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    path('contact/', views.contact, name='contact'),
    path("postComment",views.postComment,name="postComment"),
    path("filters/<str:filter>",views.filters,name="filters"),
    path("tiresize/",views.TireSize,name="TireSize"),
    path("vehicle/",views.Vehicle,name="Vehicle"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)