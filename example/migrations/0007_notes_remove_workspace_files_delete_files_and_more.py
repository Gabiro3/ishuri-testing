# Generated by Django 4.2.7 on 2024-02-02 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_files_location_alter_files_workspace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='files',
        ),
        migrations.DeleteModel(
            name='Files',
        ),
        migrations.AddField(
            model_name='notes',
            name='workspace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workspace', to='base.workspace'),
        ),
        migrations.AddField(
            model_name='workspace',
            name='notes',
            field=models.ManyToManyField(related_name='related', to='base.notes'),
        ),
    ]
