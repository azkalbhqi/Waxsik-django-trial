from django.db import models

# Define the Car model
class Car(models.Model):
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'
    CATEGORY_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (BIG, 'Big'),
    ]
    id_car = models.AutoField(primary_key=True)
    car_model = models.CharField(max_length=50)
    category = models.CharField(
        max_length=6,
        choices=CATEGORY_CHOICES,
        default=SMALL,
    )

    def __str__(self):
        return f'{self.car_model} ({self.get_category_display()})'

# Define the Service model
class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50)
    price_small = models.BigIntegerField(default=0)  # Default value for price_small
    price_medium = models.BigIntegerField(default=0)  # Default value for price_medium
    price_big = models.BigIntegerField(default=0)  # Default value for price_big

    def __str__(self):
        return self.service_name

    def get_price_by_category(self, category):
        if category == 'small':
            return self.price_small
        elif category == 'medium':
            return self.price_medium
        elif category == 'big':
            return self.price_big
        return None


class CarService(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_date = models.DateField()  

    def __str__(self):
        return f"{self.car.car_model} - {self.service.service_name} on {self.service_date}"
