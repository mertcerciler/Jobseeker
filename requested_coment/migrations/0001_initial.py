# Generated by Django 2.2.1 on 2019-05-20 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requested_Coment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coment.Comment')),
                ('work_experience', models.CharField(max_length=10000)),
                ('interview_process', models.CharField(max_length=10000)),
                ('company_pros', models.CharField(max_length=10000)),
                ('company_cons', models.CharField(max_length=10000)),
                ('cmp_name', models.CharField(max_length=64)),
            ],
            bases=('coment.comment',),
        ),
    ]
