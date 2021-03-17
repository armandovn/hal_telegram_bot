# Generated by Django 3.1.7 on 2021-03-17 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='NextQuestion', to='questions.question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='NextResponseQuestion', to='questions.question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='parent_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ParentResponseQuestion', to='questions.question'),
        ),
    ]
