# Generated by Django 2.2.7 on 2019-12-02 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpersgo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='telefono',
            name='tipotelefono',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='helpersgo.TipoTelefono'),
            preserve_default=False,
        ),
    ]
