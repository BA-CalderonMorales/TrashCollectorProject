
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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weekly_pickup_day', models.CharField(max_length=10, null=True)),
                ('onetime_pickup', models.CharField(max_length=10, null=True)),
                ('start_suspension', models.CharField(max_length=10, null=True)),
                ('end_suspension', models.CharField(max_length=10, null=True)),
                ('balance', models.IntegerField(default=0, max_length=10)),
                ('zip_code', models.CharField(max_length=5, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
