# Generated by Django 3.2 on 2021-04-29 14:48

import covid.services
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('line_1', models.CharField(blank=True, max_length=128, null=True)),
                ('line_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('landmark', models.CharField(blank=True, max_length=64, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='covid-documents/%Y/%m/%d', validators=[covid.services.file_extension_validator])),
                ('like', models.PositiveIntegerField(blank=True, null=True)),
                ('dislike', models.PositiveIntegerField(blank=True, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='covid.address')),
                ('category', models.ManyToManyField(related_name='categories', to='covid.Category')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='covid.user')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('report', models.BooleanField(default=False)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='covid.post')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_feedback', to='covid.user')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
    ]
