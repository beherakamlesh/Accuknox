import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    time.sleep(5) 
    print("Signal processing complete!")

my_instance = MyModel(name="Test")
my_instance.save()

print("Signal is processed.")