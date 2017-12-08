# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 11:07
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apli', '0004_person_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_add', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='last_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_edit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.Project'),
        ),
        migrations.AlterField(
            model_name='person',
            name='IBAN',
            field=models.CharField(blank=True, max_length=200, verbose_name='IBAN'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='person',
            name='agent',
            field=models.CharField(blank=True, max_length=200, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='person',
            name='agent_short',
            field=models.CharField(blank=True, max_length=100, verbose_name='Kurs Agentname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='bank_account',
            field=models.CharField(max_length=27, validators=[django.core.validators.RegexValidator(message="Bank account must be entered in the format: 'DE12 3456 7890 1234 5678 90'. Up to 27 digits allowed.", regex='^DE\\d{2}\\s?([0-9a-zA-Z]{4}\\s?){4}[0-9a-zA-Z]{2}$')], verbose_name='Konto'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='Geburstag'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='Stadt'),
        ),
        migrations.AlterField(
            model_name='person',
            name='client',
            field=models.BooleanField(default=False, verbose_name='Kunde'),
        ),
        migrations.AlterField(
            model_name='person',
            name='comment',
            field=models.TextField(blank=True, max_length=500, verbose_name='Kommentar'),
        ),
        migrations.AlterField(
            model_name='person',
            name='comment_other',
            field=models.CharField(blank=True, max_length=200, verbose_name='Kommentar von andere'),
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, max_length=200, verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='person',
            name='company_short',
            field=models.CharField(blank=True, max_length=100, verbose_name='Kurs firma Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=50, verbose_name='Land'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='person',
            name='make_up',
            field=models.BooleanField(default=False, verbose_name='Make-up'),
        ),
        migrations.AlterField(
            model_name='person',
            name='model',
            field=models.BooleanField(default=False, verbose_name='Modell'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name_short',
            field=models.CharField(blank=True, max_length=100, verbose_name='Kurs Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='other',
            field=models.BooleanField(default=False, verbose_name='Andere'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='photographe',
            field=models.BooleanField(default=False, verbose_name='Photograph'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sedcard_cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Kost'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sedcard_payed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sedcard'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sedcard_statut',
            field=models.BooleanField(default=False, verbose_name='Sedcard Status'),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='styling',
            field=models.BooleanField(default=False, verbose_name='Styling'),
        ),
        migrations.AlterField(
            model_name='person',
            name='website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='person',
            name='zip_code',
            field=models.CharField(blank=True, max_length=15, verbose_name='code'),
        ),
    ]