from django.db import models
from datetime import datetime

# Create your models here.
class Car(models.Model):
    state_choice = (
        ("Abia", "Abia"),
        ("Adamawa", "Adamawa"),
        ("Akwa Ibom", "Akwa Ibom"),
        ("Anambra", "Anambra"),
        ("Bauchi", "Bauchi"),
        ("Bayelsa", "Bayelsa"),
        ("Benue", "Benue"),
        ("Borno", "Borno"),
        ("Cross River", "Cross River"),
        ("Delta", "Cross River"),
        ("Ebonyi", "Ebonyi"),
        ("Edo", "Edo"),
        ("Ekiti", "Ekiti"),
        ("Enugu", "Enugu"),
        ("FCT", "FCT"),
        ("Gombe", "FCT"),
        ("Imo", "Imo"),
        ("Jigawa", "Jigawa"),
        ("Kaduna", "Kaduna"),
        ("Kano", "Kano"),
        ("Katsina", "Katsina"),
        ("Kebbi", "Kebbi"),
        ("Kogi", "Kogi"),
        ("Kwara", "Kwara"),
        ("Lagos", "Lagos"),
        ("Nasarawa", "Nasarawa"),
        ("Niger", "Niger"),
        ("Ogun", "Ogun"),
        ("Ondo", "Ondo"),
        ("Osun", "Osun"),
        ("Oyo", "Oyo"),
        ("Plateau", "Plateau"),
        ("Rivers", "Rivers"),
        ("Sokoto", "Sokoto"),
        ("Taraba", "Taraba"),
        ("Yobe", "Yobe"),
        ("Zamfara", "Zamfara"),
    )

    year_choice = [(r, r) for r in range(2000, (datetime.now().year + 1))]

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),)

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=255)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    features = models.CharField(('features'), choices=features_choices, max_length=100)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(('doors'), choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)