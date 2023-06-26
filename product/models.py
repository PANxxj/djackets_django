from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()

    class Meta:
        ordering=('name',)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Product(models.Model):
    category=models.ForeignKey(Category,models.CASCADE)
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    description=models.TextField(null=True,blank=True)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('created_at',)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:9000'+self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:9000'+self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:9000'+self.thumbnail.url
            
    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)

        thumbnail=File(thumb_io,name=image.name)
        return thumbnail
    # jh
