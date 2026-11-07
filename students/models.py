from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_university_id(value):
    value = str(value)
    if len(value) != 9 or not value.startswith(('1', '2')):
        raise ValidationError(
            'University ID must start with 1 or 2 and contain 9 digits.'
        )

def validate_national_id(value):
    value = str(value)
    if len(value) != 9 or not value.startswith(('9', '8', '4')):
        raise ValidationError(
            'ID Number must start with 9, 8, or 4 and contain 9 digits.'
        )

class Student(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\u0621-\u064A ]+$',
                message='Name must contain letters only.'
            )
        ]
    )

    university_id = models.IntegerField(
        unique=True,
        validators=[validate_university_id]
    )

    national_id = models.IntegerField(
        validators=[validate_national_id]
    )

    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^(059|056)[0-9]{7}$',
                message='Mobile number must start with 059 or 056 and contain 10 digits.'
            )
        ]
    )
    address = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    image = models.ImageField(
        upload_to='students/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'png']
            )
        ]
    )

    def __str__(self):
        return self.name