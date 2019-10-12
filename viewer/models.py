from django.db import models
from hashlib import sha256

import os


def hash_upload(instance, filename):
    instance.file_field.open()
    file_hash = sha256(instance.file_field.read()).hexdigest()
    _, ext = os.path.splitext(filename)
    return f'{file_hash}{ext}'


class Media(models.Model):
    file_field = models.FileField(upload_to=hash_upload, )
    source = models.CharField(max_length=64, default='Unknown')
    url = models.CharField(max_length=512, default='Unknown')

    def __str__(self):
        return self.file_field.name


class Tag(models.Model):
    Image_id = models.ForeignKey(Media, on_delete=models.CASCADE)
    tag = models.CharField(max_length=64)

