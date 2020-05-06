from django.db import models
# from ckeditor.fields import RichTextUploadingField
# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=100, default="")
    # content = models.TextField(default="")
    heading1 = models.CharField(max_length=50 , default="")
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")

    heading2 = models.CharField(max_length=50, default="")
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")

    heading3 = models.CharField(max_length=50 , default="")
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")

    heading4 = models.CharField(max_length=50, default="")
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50, default="")
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50, default="")
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")

    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title


class leg(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


class chest1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


class back(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title



class fullbody1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title



class bicep1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


class tricep1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


class shoulder1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


class forearm1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


class abs1(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog/images', default="")
    content1 = models.TextField(default="")


    heading2 = models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='blog/images', default="")
    content2 = models.TextField(default="")


    heading3 = models.CharField(max_length=50)
    image3 = models.ImageField(upload_to='blog/images', default="")
    content3 = models.TextField(default="")


    heading4 = models.CharField(max_length=50)
    image4 = models.ImageField(upload_to='blog/images', default="")
    content4 = models.TextField(default="")

    heading5 = models.CharField(max_length=50)
    image5 = models.ImageField(upload_to='blog/images', default="")
    content5 = models.TextField(default="")

    heading6 = models.CharField(max_length=50)
    image6 = models.ImageField(upload_to='blog/images', default="")
    content6 = models.TextField(default="")



    def __str__(self):
        return self.title


# important !!!!
# seven
# 7gym1000.