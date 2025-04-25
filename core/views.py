from django.shortcuts import render, redirect
from .forms import Employee_Form
from .models import employee_data
from django.http import HttpResponse
from django.contrib import messages
import os

# Create your views here.
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
                return redirect('create_employee')
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

def show(request):
    return HttpResponse('Successful')