from django.db import models




class HomeReaload(models.Model):
    pic = models.ImageField('/meadi')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.title
    
    

class servicesDescript(models.Model):
    title = models.CharField(max_length=50)
    des  = models.TextField()
    
    def __str__(self) :
        return self.title


class About(models.Model):
    pic = models.ImageField('/media')
    des = models.TextField()
    
    
    
    
class OurService (models.Model):
    pic =  models.ImageField('/media')
    title = models.CharField(max_length=100)
    des = models.TextField()



class Why_Choose_Us(models.Model):
    pic = models.ImageField('/media')
    des = models.TextField()
    
    pic1 =  models.ImageField('/media')
    title1 = models.CharField(max_length=100)
    pic2 =  models.ImageField('/media')
    title2 = models.CharField(max_length=100)
    pic3 =  models.ImageField('/media')
    title3 = models.CharField(max_length=100)
    pic4 =  models.ImageField('/media')
    title4 = models.CharField(max_length=100)

    
    

class Project(models.Model):
    pic = models.ImageField('/media')
    titile = models.CharField(max_length=50)
    des = models.CharField(max_length=150)
    
    
    
class Tema (models.Model):
    pic = models.ImageField('/media')
    name = models.CharField(max_length=50)
    Expertise = models.CharField(max_length=50)
    



class Work_with_us(models.Model):
    name = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    adrrs = models.CharField(max_length=80)
    resuame =  models.ImageField('/media')
    
    def __str__(self) :
        return self.name

  
    
    

class products(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    OFFprice = models.CharField(max_length=20,null=True,blank=True)
    des = models.TextField()
    pic = models.ImageField('/media')



class item(models.Model):
    productId = models.ForeignKey(products,on_delete=models.CASCADE)
    
    
    
class Articl(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    pic = models.ImageField('/media',null=True,blank=True)
    pic = models.ImageField('/media',null=True,blank=True)
    pic = models.ImageField('/media',null=True,blank=True)
    











