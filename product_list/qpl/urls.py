from django.conf.urls import url
from qpl import views

app_name = 'qpl'

urlpatterns = [
	url(r'^$', views.BaseView.as_view(), name='base'),
	url(r'^login', views.login_user, name='login'),
	url(r'^register', views.RegisterView.as_view(), name='register'),
	url(r'^register', views.register_user, name='register_user'),
	url(r'^products', views.ProductsView.as_view(), name='products'),
	url(r'^product_added', views.ProductAddedView.as_view(), name='product_added'),

]