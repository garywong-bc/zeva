# Generated by Django 3.0.3 on 2020-03-12 09:27

import db_comments.model_mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20200310_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditClass',
            fields=[
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('credit_class', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'credit_class',
            },
        ),
        migrations.CreateModel(
            name='CreditTransactionType',
            fields=[
                ('transaction_type', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'credit_transaction_type',
            },
        ),
        migrations.CreateModel(
            name='CreditTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittransaction_CREATE_USER', to='api.UserProfile')),
                ('credit_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='api.CreditClass')),
                ('credit_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='credit_transactions', to='api.Organization')),
                ('debit_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='debit_transactions', to='api.Organization')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='api.CreditTransactionType')),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittransaction_UPDATE_USER', to='api.UserProfile')),
            ],
            options={
                'db_table': 'credit_transaction',
            },
            bases=(models.Model, db_comments.model_mixins.DBComments),
        ),
    ]
