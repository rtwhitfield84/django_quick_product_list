from django.conf.urls import url
from qpl import views

app_name = 'qpl'

urlpatterns = [
	url(r'^$', views.ProductsView.as_view(), name='products'),
	url(r'^product_added', views.ProductAddedView.as_view(), name='product_added'),
]