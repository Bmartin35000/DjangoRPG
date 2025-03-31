# Generated by Django 5.1.7 on 2025-03-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_character_arme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='classe',
        ),
        migrations.AddField(
            model_name='character',
            name='pv',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(blank=True, choices=[('Nain', 'Nain'), ('Elfe', 'Elfe'), ('Humain', 'Humain')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='niveau',
            field=models.IntegerField(default=1),
        ),
    ]
