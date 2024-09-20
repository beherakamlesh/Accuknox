
import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")


if __name__ == "__main__":
    print(f"Main thread ID: {threading.get_ident()}")
    my_instance = MyModel(name="Test")
    my_instance.save()

#If the thread IDs printed in both the main thread and the signal handler are the same, this conclusively proves that Django signals run in the same thread as the caller.