from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django .http import HttpResponse, HttpResponseRedirect
from . models import Product


class BaseView(TemplateView):
	template_name = 'base.html'

class LoginView(TemplateView):
	template_name = 'login.html'


class RegisterView(TemplateView):
	template_name = 'register.html'


class ProductsView(View):
	template_name = 'products.html'

	def get(self, request):
		self.products = Product.objects.all()
		return render(request, 'products.html', {'products': self.products})

	def post(self, request):
		data = request.POST
		Product.objects.create(
			name=data['name'],
			description=data['description'],
			price=data['price']
		)
		return HttpResponseRedirect('/products')




class ProductAddedView(TemplateView):
	template_name = 'productAdded.html'

def register_user(request):
	data = request.POST
	User.objects.create_user(
		username=data['username'],
		email=data['email'],
		first_name=data['first_name'],
		last_name=data['last_name'],
		password=data['password']
	)

	return LoginView.login_user(request)

def login_user(request):
    data = request.POST
    username = data['username']
    password = data['password']
    user = authenticate(
    	username=username,
    	password=password
    )

    if user is not None:
    	login(request=request, user=user)
    else:
    	HttpResponseRedirect(redirect_to='/register')
    return HttpResponseRedirect(redirect_to='/products')


def logout_user(request):
	logout(request)
	return HttpResponseRedirect(redirect_to='/')
