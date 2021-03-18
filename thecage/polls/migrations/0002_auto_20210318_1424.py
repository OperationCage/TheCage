# Generated by Django 3.1.7 on 2021-03-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('discovered_date', models.DateTimeField(verbose_name='date discovered')),
            ],
        ),
        migrations.RemoveField(
            model_name='discoverydate',
            name='name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_text',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.DeleteModel(
            name='DiscoveryDate',
        ),
        migrations.AddField(
            model_name='location',
            name='cryptids',
            field=models.ManyToManyField(related_name='monsters', to='polls.Cryptid'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.cryptid'),
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]