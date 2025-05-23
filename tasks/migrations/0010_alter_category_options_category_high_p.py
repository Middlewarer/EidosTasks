# Generated by Django 4.2.11 on 2025-05-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_category_user_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['high_p', 'title']},
        ),
        migrations.AddField(
            model_name='category',
            name='high_p',
            field=models.BooleanField(default=False),
        ),
    ]
