from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Ecom import views
from Ecom.views import Login, SearchResults
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:id>/', views.ProductDetail.as_view(), name='product_detail'),
    path("signup/", views.Signup.as_view(), name="signup/"),
    path("checkout_cart/", views.Checkoutcart.as_view(), name="checkout_cart"),
    path("create_card/", views.Payment.as_view(), name="card"),
    path("check_shipping/", views.Shipping.as_view(), name="shipping"),
    path('contact/', views.Contact, name='contact'),
    path('faq/', views.Faq, name='faq'),
    path('about_us/', views.AboutUs, name='about_us'),
    path('my_account/', views.MyAccount, name='my_account'),
    path('products/', views.Products, name='products'),
    path('search/', SearchResults.as_view(), name='search'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
