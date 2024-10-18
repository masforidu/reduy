# Generated by Django 5.1.1 on 2024-10-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shegarland', '0010_alter_shegarlandform_balina_lafa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shegarlandform',
            name='gosa_tajajila',
            field=models.CharField(blank=True, choices=[('Mana Jireenyaa', 'Mana Jireenyaa'), ('Daldala', 'Daldala'), ('Tajajilaa Bulchiinsaa', 'Tajajilaa Bulchiinsaa'), ('Tajajilaa Haw.', 'Tajajilaa Haw.'), ('Industirii/Investimenti/', 'Industirii/Investimenti/'), ('Iddoo Bashannanaa', 'Iddoo Bashannanaa'), ('Magarisumma', 'Magarisumma'), ('Lafa Bosona', 'Lafa Bosona'), ('Duwwaa/Open-Space/', 'Duwwaa/Open-Space/'), ('Qonnaa', 'Qonnaa'), ('Dhedicha', 'Dhedicha'), ('Iddo ISAn Digame', 'Iddo ISAn Digame'), ('Lafa Albudaa/Quarry Site/', 'Lafa Albudaa/Quarry Site/'), ('Kan biroo', 'Kan biroo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shegarlandform',
            name='qamaa_qophaef',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shegarlandform',
            name='tajajila_qophaef',
            field=models.CharField(choices=[('Bankii Lafa', 'Bankii Lafa'), ('Mana jirenya', 'Mana jirenya'), ('Daldala', 'Daldala'), ('Tajajilaa Bulchi', 'Tajajilaa Bulchi'), ('Tajajilaa Haw.', 'Tajajilaa Haw.'), ('Investimenti', 'Investimenti'), ('IMX', 'IMX'), ('Magarisumma', 'Magarisumma'), ('Innishetivif', 'Innishetivif'), ('Tajajila babalifanna', 'Tajajila babalifanna'), ('Qonnaa', 'Qonnaa'), ('Tajajila yeroof ', 'Tajajila yeroof '), ('Tajaajila  Babal', 'Tajaajila  Babal')], max_length=50),
        ),
    ]
