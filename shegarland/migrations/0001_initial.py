# Generated by Django 5.1.1 on 2024-09-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShegarLandForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magaalaa', models.CharField(choices=[('SU', 'SU'), ('MA', 'MA'), ('LXLD', 'LXLD'), ('KJ', 'KJ'), ('KF', 'KF'), ('GLN', 'GLN'), ('FU', 'FU'), ('GGUD', 'GGUD'), ('SAB', 'SAB'), ('MN', 'MN'), ('GGUJ', 'GGUJ'), ('BU', 'BU')], max_length=5)),
                ('aanaa', models.CharField(max_length=30)),
                ('iddo_adda', models.CharField(max_length=30)),
                ('lakk_adda', models.IntegerField()),
                ('gosa_tajajila', models.CharField(max_length=40)),
                ('madda_lafa', models.CharField(choices=[('ISA Digame', 'ISA Digame'), ('Waligalten kan cite', 'Waligalten kan cite'), ('Lafa motumma', 'Lafa motumma'), ('Lafa walini', 'Lafa walini'), ('Lafa benyan itti kaffalame', 'Lafa benyan itti kaffalame'), ("Lafa seran ala qabame bankitti debi'e", "Lafa seran ala qabame bankitti debi'e"), ('kan biroo', 'kan biroo')], max_length=50)),
                ('tajajila_iddo', models.CharField(max_length=50)),
                ('haala_beenya', models.CharField(choices=[('Bilisaa', 'Bilisaa'), ('Beenyaa kan qabu', 'Beenyaa kan qabu')], max_length=20)),
                ('qamaa_qophaef', models.CharField(max_length=40)),
                ('tajajila_qophaef', models.CharField(max_length=40)),
                ('balina_lafa', models.IntegerField()),
                ('kan_qophesse', models.CharField(max_length=40)),
                ('guyya_qophae', models.DateTimeField()),
                ('shapefile', models.FileField(upload_to='shapefiles/')),
                ('suura_iddoo', models.FileField(upload_to='media/')),
            ],
        ),
    ]
