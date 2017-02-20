from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django .http import HttpResponseRedirect
from . models import Product


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
