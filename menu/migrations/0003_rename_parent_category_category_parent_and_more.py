# Generated by Django 4.1.7 on 2023-03-04 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_category_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent_category',
            new_name='parent',
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'slug')},
        ),
    ]
