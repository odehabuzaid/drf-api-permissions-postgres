# Generated by Django 3.2.9 on 2021-11-23 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlighted', models.TextField()),
                ('task', models.CharField(max_length=20)),
                ('label', models.CharField(choices=[('NoLabel', 'High'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'), ('OnHold', 'Hold')], default='NoLabel', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]