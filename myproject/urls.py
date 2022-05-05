from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/',views.profile , name='profile'),
    path('items/', views.items, name='items'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('<int:food_id>', views.item, name='item'),
    path('qr_mobile/<mobile>/<amount>/qr.png', views.get_qr, name='qr'),
    path('qr_nid/<nid>/<amount>/', views.get_qr, name='qr'),
	path('payment/', views.payment, name="payment"),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
