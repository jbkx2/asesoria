# Generated by Django 2.2.6 on 2019-11-11 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0002_auto_20191021_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='novedad',
            options={'ordering': ['fecha_pub'], 'verbose_name_plural': 'noticias'},
        ),
        migrations.RemoveField(
            model_name='novedad',
            name='texto',
        ),
        migrations.AddField(
            model_name='novedad',
            name='contenido',
            field=models.TextField(default='', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='novedad',
            name='desc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='novedad',
            name='fecha_pub',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Ingrese Fecha de Publicacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='novedad',
            name='titulo',
            field=models.CharField(help_text='Obligatorio', max_length=60),
        ),
    ]
