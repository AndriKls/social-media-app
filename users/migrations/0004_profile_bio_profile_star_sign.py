# Generated by Django 5.1.1 on 2024-12-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Bio'),
        ),
        migrations.AddField(
            model_name='profile',
            name='star_sign',
            field=models.CharField(blank=True, choices=[('aries', 'Jäär'), ('taurus', 'Sõnn'), ('gemini', 'Kaksikud'), ('cancer', 'Vähk'), ('leo', 'Lõvi'), ('virgo', 'Neitsi'), ('libra', 'Kaalud'), ('scorpio', 'Skorpion'), ('sagittarius', 'Ambur'), ('capricorn', 'Kaljukits'), ('aquarius', 'Veevalaja'), ('pisces', 'Kalad')], max_length=20),
        ),
    ]