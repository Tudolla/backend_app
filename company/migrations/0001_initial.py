# Generated by Django 5.0.7 on 2024-09-22 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('founding_date', models.CharField(max_length=50)),
                ('ceo', models.CharField(max_length=50)),
                ('father_company', models.CharField(max_length=255)),
                ('amount_staff', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logo/')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('application_deadline', models.DateField()),
                ('job_type', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('CT', 'Contract')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_openings', to='company.companyinfo')),
            ],
            options={
                'db_table': 'job_opening',
            },
        ),
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='leadership_photos/')),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leadership', to='company.companyinfo')),
            ],
            options={
                'db_table': 'company_leadership',
            },
        ),
        migrations.CreateModel(
            name='MissionVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mission_vision', to='company.companyinfo')),
            ],
            options={
                'db_table': 'company_mission',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('client', models.CharField(max_length=255)),
                ('technologies_used', models.CharField(max_length=255)),
                ('project_link', models.URLField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='company.companyinfo')),
            ],
            options={
                'db_table': 'company_project',
            },
        ),
    ]
