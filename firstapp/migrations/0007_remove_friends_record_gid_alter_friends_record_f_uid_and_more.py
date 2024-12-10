# Generated by Django 5.0.1 on 2024-03-28 19:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_friends_record_f_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends_record',
            name='gid',
        ),
        migrations.AlterField(
            model_name='friends_record',
            name='f_uid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friend_releted_to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Group_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.group')),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]