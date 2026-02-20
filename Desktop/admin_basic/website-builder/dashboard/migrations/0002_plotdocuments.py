# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(max_length=500, upload_to='plot_documents/')),
                ('document_name', models.CharField(blank=True, help_text='Original filename or custom name', max_length=255)),
                ('document_type', models.CharField(blank=True, help_text='File type/extension', max_length=100)),
                ('file_size', models.PositiveIntegerField(default=0, help_text='File size in bytes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='dashboard.plots')),
            ],
            options={
                'verbose_name': 'Plot Document',
                'verbose_name_plural': 'Plot Documents',
                'ordering': ['-created_at'],
            },
        ),
    ]
