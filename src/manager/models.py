from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
attach = models.FileField(
    upload_to='uploads/%Y/%m/%d/',
    verbose_name='Image File [png, jpg, gif] (No transparency)',
    validators=[FileExtensionValidator(['png', 'jpg', 'gif'])],
)
