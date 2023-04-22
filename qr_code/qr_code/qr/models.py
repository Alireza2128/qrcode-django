from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

class Website(models.Model):
    link = models.CharField(max_length=500)
    qr_code = models.ImageField(upload_to="images/" , blank=True , null=True)

    def __str__(self):
        return self.link

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.link)
        canvas = Image.new('RGB' , (290 , 290) , 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.link}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer , 'PNG')
        self.qr_code.save(fname , File(buffer) , save=False)
        canvas.close()
        super().save(*args , **kwargs)
