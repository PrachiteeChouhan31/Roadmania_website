from django.db import models

# Create your models here.
class Destination(models.Model):
    """A travelled destination"""
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """return the name of destination"""
        return self.text

    
    
    
class Entry(models.Model):
    """Description of each destinations"""
    destination=models.ForeignKey(Destination, on_delete=models.CASCADE)
    text=models.TextField()
    
    date_added=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='entries'
    
    def __str__(self):
        """return the description"""
        return self.text[30]+"..."
    
   
class Tips(models.Model):
    """Thing should keep in mind"""
    text_tip=models.TextField()
    
class Image_Entry(models.Model):
    """This will store images to display and foreign key is Entry"""
    entry=models.ForeignKey(Entry, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo/')