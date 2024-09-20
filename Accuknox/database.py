from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

class AnotherModel(models.Model):
    description = models.CharField(max_length=100)


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    
    AnotherModel.objects.create(description="Created from signal")


if __name__ == "__main__":
    try:
        with transaction.atomic():
            my_instance = MyModel(name="Test")
            my_instance.save()
            
            
            raise ValueError("Intentional error to rollback transaction")

    except ValueError:
       
        if AnotherModel.objects.exists():
            print("Signal changes were committed.")
        else:
            print("Signal changes were rolled back with the transaction.")
