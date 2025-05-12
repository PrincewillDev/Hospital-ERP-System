from django.shortcuts import render, redirect, get_object_or_404
from .forms import Employee_Form, Registerform
from .models import employee_data
from django.http import HttpResponse
from django.contrib import messages
import os
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_employee(request):
    if request.method == 'POST':
        form = Employee_Form(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Handle the file upload
                if 'passport_img' in request.FILES:
                    uploaded_file = request.FILES['passport_img']
                    # Validate file size (2MB max)
                    if uploaded_file.size > 2 * 1024 * 1024:
                        messages.error(request, 'Image file too large (max 2MB)')
                        return redirect('create_employee')
                    
                    # Validate file type
                    valid_extensions = ['.jpg', '.jpeg', '.png']
                    ext = os.path.splitext(uploaded_file.name)[1].lower()
                    if ext not in valid_extensions:
                        messages.error(request, 'Invalid file type. Please upload a JPG or PNG image.')
                        return redirect('create_employee')

                # Save the form
                form.save()
                messages.success(request, 'Employee record created successfully!')
                return redirect("displaypage")
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                return redirect('create_employee')
        else:
            # Display form errors to the user
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return redirect('create_employee')
    else:
        form = Employee_Form()
    
    return render(request, 'index.html', {'form': form})

@login_required
def data_page(request):
    employee_info = employee_data.objects.all()
    return render(request, 'data_page.html',{'employee_info': employee_info})

@login_required
def update_form(request, emp_ID):
    employee_instance = get_object_or_404(employee_data, emp_ID=emp_ID)
    
    if request.method == 'POST':
        form = Employee_Form(request.POST, request.FILES, instance=employee_instance)
        if form.is_valid():
            try:
                # Handle file validation if a new file is uploaded
                if 'passport_img' in request.FILES:
                    uploaded_file = request.FILES['passport_img']
                    # Validate file size (2MB max)
                    if uploaded_file.size > 2 * 1024 * 1024:
                        messages.error(request, 'Image file too large (max 2MB)')
                        return redirect('update', emp_ID=emp_ID)
                    
                    # Validate file type
                    valid_extensions = ['.jpg', '.jpeg', '.png']
                    ext = os.path.splitext(uploaded_file.name)[1].lower()
                    if ext not in valid_extensions:
                        messages.error(request, 'Invalid file type. Please upload a JPG or PNG image.')
                        return redirect('update', emp_ID=emp_ID)
                
                # Save the form
                form.save()
                messages.success(request, 'Employee record updated successfully!')
                return redirect('displaypage')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                return redirect('update', emp_ID=emp_ID)
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = Employee_Form(instance=employee_instance)
    
    return render(request, 'update.html', {'form': form, 'emp_ID': emp_ID})

@login_required
def delete_data(request, emp_ID):
    try:
        employee_to_delete = get_object_or_404(employee_data, emp_ID=emp_ID)
        employee_to_delete.delete()
        messages.success(request, 'Employee record deleted successfully!')
    except Exception as e:
        messages.error(request, f'Could not delete employee: {str(e)}')
    
    return redirect("displaypage")


def register(request):
    if request.method == 'POST':
        form  = Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully!')
            return redirect('displaypage')
    else:
        form = Registerform()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
            