from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"Password reset request for {self.user.email}"

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True, null=True)

    def _str_(self):
        return self.email

    class Meta:
        permissions = (('can_view_user', 'Can view user'),)
        unique_together = (('email',),)
        ordering = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class ShegarLandForm(models.Model):
    magaalaa_choices = [
        ('SU', 'SU'), ('MA', 'MA'), ('LXLD', 'LXLD'),
        ('KJ', 'KJ'), ('KF', 'KF'), ('GLN', 'GLN'),
        ('FU', 'FU'), ('GGUD', 'GGUD'), ('SAB', 'SAB'),
        ('MN', 'MN'), ('GGUJ', 'GGUJ'), ('BU', 'BU')
    ]
    madda_lafa_choices = [
        ('ISA Digame', 'ISA Digame'), 
        ('Waligalten kan cite', 'Waligalten kan cite'),
        ('Lafa motumma', 'Lafa motumma'),
        ('Lafa walini', 'Lafa walini'),
        ('Lafa benyan itti kaffalame', 'Lafa benyan itti kaffalame'),
        ('Lafa seran ala qabame bankitti debi\'e', 'Lafa seran ala qabame bankitti debi\'e'),
        ('kan biroo', 'kan biroo')
    ]
    haala_beenya_choices = [
        ('Bilisaa', 'Bilisaa'), 
        ('Beenyaa kan qabu', 'Beenyaa kan qabu')
    ]

    gosa_tajajila_choices = [
        ('Mana Jireenyaa', 'Mana Jireenyaa'),
        ('Daldala','Daldala'),
        ('Tajajilaa Bulchiinsaa','Tajajilaa Bulchiinsaa'),
        ('Tajajilaa Haw.','Tajajilaa Haw.'),
        ('Industirii/Investimenti/','Industirii/Investimenti/'),
        ('Iddoo Bashannanaa','Iddoo Bashannanaa'),
        ('Magarisumma','Magarisumma'),
        ('Lafa Bosona','Lafa Bosona'),
        ('Duwwaa/Open-Space/','Duwwaa/Open-Space/'),
        ('Qonnaa','Qonnaa'
),('Dhedicha','Dhedicha'),('Iddo ISAn Digame','Iddo ISAn Digame'),
('Lafa Albudaa/Quarry Site/','Lafa Albudaa/Quarry Site/'),('Kan biroo','Kan biroo')

    ]

    tajajila_qophaef_choices = [
        ('Bankii Lafa', 'Bankii Lafa'),
        ('Mana jirenya','Mana jirenya'),
        ('Daldala','Daldala'),
        ('Tajajilaa Bulchi','Tajajilaa Bulchi'),
        ('Tajajilaa Haw.','Tajajilaa Haw.'),
        ('Investimenti','Investimenti'),
        ('IMX','IMX'),
        ('Magarisumma','Magarisumma'),
        ('Innishetivif','Innishetivif'),
        ('Tajajila babalifanna', 'Tajajila babalifanna'),
        ('Qonnaa','Qonnaa'
),('Tajajila yeroof ','Tajajila yeroof '), 
  ('Tajaajila  Babal','Tajaajila  Babal')


  ]




    magaalaa = models.CharField(max_length=5, choices=magaalaa_choices)
    aanaa = models.CharField(max_length=30, blank=True, null=True)
    iddo_adda = models.CharField(max_length=30, blank=True, null=True)
    lakk_adda = models.IntegerField(default=0)  # Set a default value
    gosa_tajajila = models.CharField(max_length=50, choices=gosa_tajajila_choices, blank=True, null=True)
    madda_lafa = models.CharField(max_length=50, choices=madda_lafa_choices)
    tajajila_iddo = models.CharField(max_length=50)
    haala_beenya = models.CharField(max_length=20, choices=haala_beenya_choices)
    qamaa_qophaef = models.CharField(max_length=50, blank=True, null=True)
    tajajila_qophaef = models.CharField(max_length=50, choices= tajajila_qophaef_choices)
    balina_lafa = models.IntegerField(default=0)  # Set a default value
    kan_qophesse = models.CharField(max_length=40, blank=True, null=True)
    guyya_qophae = models.DateField()
    shapefile = models.FileField(upload_to='shapefiles/')
    suura_iddoo = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Optional field Mallattoo with blank=True, null=True
    Mallattoo = models.ImageField(upload_to='images/', blank=True, null=True)

    # Additional optional fields
    bal_lafa_bahi_tae = models.IntegerField(blank=True, null=True)  # Optional field
    bal_lafa_hafe = models.IntegerField(blank=True, null=True)  # Calculated field
    qaama_bahi_tahef = models.CharField(max_length=40, blank=True, null=True)  # Optional
    tajajila_bahi_tahef = models.CharField(max_length=40, blank=True, null=True)  # Optional
    kan_bahi_taasise = models.CharField(max_length=255, blank=True, null=True)  # Optional
    guyyaa_bahi_tae = models.DateField(blank=True, null=True)  # Optional with calendar

    def _str_(self):
        return f"{self.magaalaa} - {self.aanaa}"

    # Override save to calculate bal_lafa_hafe
    def save(self, *args, **kwargs):
        if self.bal_lafa_bahi_tae is not None:
            self.bal_lafa_hafe = self.balina_lafa - self.bal_lafa_bahi_tae
        super().save(*args, **kwargs)