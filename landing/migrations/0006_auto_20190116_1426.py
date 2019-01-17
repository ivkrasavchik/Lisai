# Generated by Django 2.1.4 on 2019-01-16 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verbose_name', models.CharField(max_length=64, verbose_name='Ваше имя')),
                ('short_description', models.TextField(blank=True, default=None, max_length=600, null=True, verbose_name='Задайте свой вопрос')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.ProductCategory')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Zvonki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verbose_name', models.CharField(max_length=64, verbose_name='Ваше имя')),
                ('phone', models.CharField(default='+375', max_length=15, verbose_name='Телефон')),
                ('short_description', models.TextField(blank=True, default=None, max_length=128, null=True, verbose_name='Дополнительная информация')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.ProductCategory')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.Status')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
            },
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Сервис', 'verbose_name_plural': 'Сервисы'},
        ),
        migrations.AddField(
            model_name='questions',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.Status'),
        ),
    ]
