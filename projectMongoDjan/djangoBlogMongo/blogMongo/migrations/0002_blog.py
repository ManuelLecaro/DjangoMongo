# Generated by Django 2.1.5 on 2019-01-06 21:34

import blogMongo.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogMongo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', djongo.models.fields.EmbeddedModelField(model_container=blogMongo.models.Post, null=True)),
            ],
        ),
    ]