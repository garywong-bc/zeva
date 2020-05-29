# Generated by Django 3.0.3 on 2020-05-21 19:56

from django.core.exceptions import FieldDoesNotExist
from django.db import migrations, models
from django.db.migrations import RunPython


def do_nothing(apps, schema_editor):
    """
    Don't worry about the columns as we're about to remove them anyway
    """
    pass


def convert_user_to_id(apps, schema_editor):
    """
    After restoring the create_user_id and update_user_id columns,
    repopulate them back based on the username
    """
    db_alias = schema_editor.connection.alias

    UserProfile = apps.get_model('api', 'UserProfile')

    model_list = [
        'CreditClass',
        'CreditTransaction',
        'CreditTransactionType',
        'IcbcRegistrationData',
        'IcbcVehicle',
        'ModelYear',
        'OrganizationAddress',
        'Organization',
        'Permission',
        'RecordOfSale',
        'RolePermission',
        'Role',
        'SalesSubmission',
        'UserCreationRequest',
        'UserProfile',
        'UserRole',
        'Vehicle',
        'VehicleChangeHistory',
        'ZevType'
    ]

    for item in model_list:
        model = apps.get_model('api', item)

        rows = model.objects.all()
        for row in rows:
            try:
                model._meta.get_field('create_user')
                if row.create_user and row.create_user != 'SYSTEM':
                    create_user = UserProfile.objects.get(
                        username=row.create_user
                    )
                    row.create_user_id = create_user.id

            except FieldDoesNotExist:
                pass

            try:
                model._meta.get_field('update_user')
                if row.update_user and row.update_user != 'SYSTEM':
                    update_user = UserProfile.objects.get(
                        username=row.update_user
                    )
                    row.update_user_id = update_user.id

            except FieldDoesNotExist:
                pass

            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_auto_20200521_1206'),
    ]

    operations = [
        migrations.RunPython(do_nothing, convert_user_to_id),
        migrations.RemoveField(
            model_name='creditclass',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='creditclass',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='credittransaction',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='credittransaction',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='credittransactiontype',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='credittransactiontype',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='icbcregistrationdata',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='icbcregistrationdata',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='icbcvehicle',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='icbcvehicle',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='modelyear',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='modelyear',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='organizationaddress',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='organizationaddress',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='recordofsale',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='recordofsale',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='rolepermission',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='rolepermission',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='salessubmission',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='salessubmission',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='usercreationrequest',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='usercreationrequest',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='update_user_id',
        ),
        migrations.RemoveField(
            model_name='vehiclechangehistory',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='zevtype',
            name='create_user_id',
        ),
        migrations.RemoveField(
            model_name='zevtype',
            name='update_user_id',
        ),
    ]