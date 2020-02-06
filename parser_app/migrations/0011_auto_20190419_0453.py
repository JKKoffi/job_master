# Generated by Django 2.1.4 on 2019-04-19 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parser_app', '0010_resume_competencies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competency', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Competency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurableResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurable_result', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Competency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_nos', models.IntegerField(blank=True, null=True, verbose_name='Experience')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField(blank=True, null=True, verbose_name='Mobile Number')),
                ('skills', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Skills')),
                ('years_of_exp', models.IntegerField(blank=True, null=True, verbose_name='Experience')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='uploaded_on',
            new_name='last_uploaded_on',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='competencies',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='name',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skills',
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumedetails',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser_app.Resume'),
        ),
    ]