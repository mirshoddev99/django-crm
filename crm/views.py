from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import SignUpForm, CustomerForm
from .models import Customer


class LandingPageView(View):
    def get(self, request):
        return render(request, 'crm/landing_page.html')


class RegisterView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'crm/register.html', {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('login')
        else:
            return render(request, 'crm/register.html', {'form': form})


class CustomLoginView(View):
    def get(self, request):
        return render(request, 'crm/custom_login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You Have Successfully Logged in!")
            return redirect('customer_list')
        else:
            return render(request, 'crm/custom_login.html')


class CustomLogOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You Have Successfully Logged Out!")
        return redirect('custom_login')


class CustomerListView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customers = Customer.objects.all()
            return render(request, 'crm/customer_list.html', {"customers": customers})
        messages.success(request, "You Have Successfully Logged Out!")
        return redirect('custom_login')


class CustomerRecordView(View):
    def get(self, request, id):
        customer_record = Customer.objects.get(id=id)
        return render(request, 'crm/customer.html', {"customer_record": customer_record})


class AddingCustomerView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'crm/add_customer.html', {"form": form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Successfully Added customer!")
            return redirect('customer_list')
        else:
            return render(request, 'crm/add_customer.html', {"form": form})


class UpdateCustomerView(View):
    def get(self, request, id):
        current_customer = Customer.objects.get(id=id)
        form = CustomerForm(request.POST or None, instance=current_customer)
        return render(request, 'crm/updating_customer.html', {"form": form})

    def post(self, request, id):
        current_customer = Customer.objects.get(id=id)
        form = CustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Successfully Updated customer!")
            return redirect('customer_list')
        else:
            return render(request, 'crm/updating_customer.html', {"form": form})


class DeleteCustomerView(View):
    def get(self, request, id):
        Customer.objects.get(id=id).delete()
        messages.success(request, "You Have Successfully deleted customer!")
        return redirect('customer_list')
