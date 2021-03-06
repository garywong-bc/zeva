# Generated by Django 3.0.3 on 2020-07-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_auto_20200715_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='credit_class',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='api.CreditClass'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credittransaction',
            name='credit_class',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='api.CreditClass'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credittransaction',
            name='transaction_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='api.CreditTransactionType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='credit_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='api.CreditClass'),
        ),
    ]
