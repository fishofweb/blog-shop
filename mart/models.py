from django.db import models

# Create your models here.
class newarrival(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    thumbnail_desc = models.TextField(default="")
    price = models.IntegerField()
    full_desc = models.TextField(default="")
    image1 = models.ImageField(upload_to='mart/images', default="")
    image2 = models.ImageField(upload_to='mart/images', default="")

    image3 = models.ImageField(upload_to='mart/images', default="")
    category = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    vendor_price = models.IntegerField()

    def __str__(self):
        return self.product_name


class womenshirt(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    thumbnail_desc = models.TextField(default="")
    price = models.IntegerField()
    full_desc = models.TextField(default="")
    image1 = models.ImageField(upload_to='mart/images', default="")
    image2 = models.ImageField(upload_to='mart/images', default="")

    image3 = models.ImageField(upload_to='mart/images', default="")
    category = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    vendor_price = models.IntegerField()

    def __str__(self):
        return self.product_name

class menshirt(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    thumbnail_desc = models.TextField(default="")
    price = models.IntegerField()
    full_desc = models.TextField(default="")
    image1 = models.ImageField(upload_to='mart/images', default="")
    image2 = models.ImageField(upload_to='mart/images', default="")

    image3 = models.ImageField(upload_to='mart/images', default="")
    category = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    vendor_price = models.IntegerField()

    def __str__(self):
        return self.product_name


class womentrouser(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    thumbnail_desc = models.TextField(default="")
    price = models.IntegerField()
    full_desc = models.TextField(default="")
    image1 = models.ImageField(upload_to='mart/images', default="")
    image2 = models.ImageField(upload_to='mart/images', default="")

    image3 = models.ImageField(upload_to='mart/images', default="")
    category = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    vendor_price = models.IntegerField()

    def __str__(self):
        return self.product_name

class mentrouser(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    thumbnail_desc = models.TextField(default="")
    price = models.IntegerField()
    full_desc = models.TextField(default="")
    image1 = models.ImageField(upload_to='mart/images', default="")
    image2 = models.ImageField(upload_to='mart/images', default="")

    image3 = models.ImageField(upload_to='mart/images', default="")
    category = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    vendor_price = models.IntegerField()

    def __str__(self):
        return self.product_name


class equipment(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    thumbnail_desc = models.TextField(default="")
    price = models.IntegerField()
    full_desc = models.TextField(default="")
    image1 = models.ImageField(upload_to='mart/images', default="")
    image2 = models.ImageField(upload_to='mart/images', default="")

    image3 = models.ImageField(upload_to='mart/images', default="")
    category = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    vendor_price = models.IntegerField()

    def __str__(self):
        return self.product_name


class contactForm(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    message =models.TextField(max_length=1000)

    def __str__(self):
        return self.name + " " + str(self.msg_id)


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)

    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    message =models.TextField(max_length=1000)
    items =models.TextField(max_length=10000)
    total_items = models.CharField(max_length=1000)
    def __str__(self):
        return self.name + " " + str(self.order_id)
