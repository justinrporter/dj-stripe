# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-29 00:41
from __future__ import absolute_import, division, print_function, unicode_literals

import django.core.validators
from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0019_purge_on_subscriber_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='webhook_message',
            field=djstripe.fields.StripeJSONField(help_text='data received at webhook. data should be considered to be garbage until validity check is run and valid flag is set'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='application_fee_percent',
            field=djstripe.fields.StripePercentField(decimal_places=2, help_text='A positive decimal that represents the fee percentage of the subscription invoice amount that will be transferred to the application owner’s Stripe account each billing period.', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]