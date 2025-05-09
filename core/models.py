from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.
class employee_data(models.Model):
    gender = [
        ('male', 'male'),
        ('female', 'female')
    ]
    department = [
        ('medical', 'Medical'),
        ('nursing', 'Nursing'),
        ('pharmacy', 'Pharmacy'),
        ('laboratory', 'Laboratory'),
        ('radiology', 'Radiology'),
        ('administration', 'Administration'),
        ('maintenance', 'Maintenance'),
        ('it', 'IT'),
        ('finance', 'Finance'),
        ('hr', 'Human Resources'),
    ]
    
    employment_type = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('intern', 'Intern'),
    ]

    supervisor_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    # Personal information
    emp_ID = models.UUIDField(primary_key=True, editable=False, unique=True, max_length=12, default=uuid.uuid4)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField(
        validators=[
            MinValueValidator(date(1900, 1, 1)),
            MaxValueValidator(date.today())
        ],
        help_text="Format: YYYY-MM-DD"
    )
    gender = models.CharField(max_length=10, choices=gender, default="")
    passport_img = models.ImageField(upload_to='employee_passports/', blank=True, null=True)
    badge_num =models.CharField(max_length=15, default="")
    
    # Contact information
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)
    address = models.TextField(max_length=255, default="")
    
    # employement detail
    department = models.CharField(max_length=70, choices=department, default="")
    job_title = models.CharField(max_length=30)
    date_of_hire = models.DateField()
    employment_types = models.CharField(max_length=50, choices=employment_type, default="")
    supervisor_manager = models.CharField(
        max_length=3,
        choices=supervisor_choices,
        default='no',
        help_text="Is this employee a supervisor or manager?"
    )
    monthly_salary = models.CharField(max_length=13)
    
    # Professional Information
    highest_qualification = models.CharField(max_length=60)
    specialization = models.CharField(max_length=60)
    years_of_experience = models.IntegerField()
    licenses = models.TextField(max_length=255)
    

 
