# Generated by Django 5.1.1 on 2024-10-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shegarland', '0009_shegarlandform_mallattoo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shegarlandform',
            name='balina_lafa',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shegarlandform',
            name='lakk_adda',
            field=models.IntegerField(default=0),
        ),
    ]
