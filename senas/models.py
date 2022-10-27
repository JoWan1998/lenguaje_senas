from tkinter import Image
from django.db import models

# Create your models here.
class Image():
    image = models.ImageField(upload_to='images')
