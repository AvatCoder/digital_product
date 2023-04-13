from django.db import models



class category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title=models.CharField('Title',max_length=50)
    description = models.TextField('Description', blank=True)
    avatar = models.ImageField('Avatar',blank=True)
    is_enable = models.BooleanField('is enable', default=True)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)
    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
class Product(models.Model):
    title=models.CharField('Title',max_length=50)
    description = models.TextField('Description', blank=True)
    avatar = models.ImageField('Avatar',blank=True,upload_to='products/')
    is_enable = models.BooleanField('is enable', default=True)
    categories = models.ManyToManyField('Category', verbose_name='categories', blank=True)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)
    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'   

class Files(models.Model):
    product = models.ForeignKey('Product',verbose_name='product', on_delete=models.CASCADE)
    title=models.CharField('Title',max_length=50)
    description = models.TextField('Description', blank=True)
    file = models.FileField('File',upload_to = 'files/%y/%m/%d/')
    is_enable = models.BooleanField('is enable', default=True)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)
    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'