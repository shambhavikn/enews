# Generated by Django 4.2.11 on 2024-04-06 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deptEnews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='articles',
            field=models.ManyToManyField(related_name='related_newsletters', to='deptEnews.article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='newsletter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_articles', to='deptEnews.newsletter'),
        ),
    ]