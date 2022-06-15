# Generated by Django 4.0.3 on 2022-05-03 14:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('question', ckeditor.fields.RichTextField(max_length=600)),
                ('answer1', models.CharField(max_length=200)),
                ('answer2', models.CharField(max_length=200)),
                ('answer3', models.CharField(max_length=200)),
                ('answer4', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('Answer1', 'Answer1'), ('Answer2', 'Answer2'), ('Answer3', 'Answer3'), ('Answer4', 'Answer4')], max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory')),
            ],
        ),
    ]