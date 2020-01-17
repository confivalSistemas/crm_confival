# Generated by Django 2.2.6 on 2020-01-17 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genero', '0001_initial'),
        ('origen_contacto', '0001_initial'),
        ('asesores', '0001_initial'),
        ('municipio', '0001_initial'),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbAbogados',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=51)),
                ('apellidos', models.CharField(blank=True, max_length=45, null=True)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('tarjeta_p', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=154, null=True)),
                ('ciudadnombre', models.CharField(blank=True, db_column='ciudadNombre', max_length=27, null=True)),
                ('departamento', models.CharField(blank=True, max_length=18, null=True)),
                ('direccion2', models.CharField(blank=True, max_length=154, null=True)),
                ('empresa', models.CharField(blank=True, max_length=56, null=True)),
                ('celular2', models.CharField(blank=True, max_length=15, null=True)),
                ('celular1', models.CharField(blank=True, max_length=15, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('fijo2', models.CharField(blank=True, max_length=15, null=True)),
                ('fijo1', models.CharField(blank=True, max_length=15, null=True)),
                ('fijo', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('e_mail1', models.CharField(blank=True, max_length=67, null=True)),
                ('e_mail2', models.CharField(blank=True, max_length=67, null=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True, verbose_name='fecha de actualización')),
                ('observaciones', models.CharField(blank=True, max_length=150, null=True)),
                ('fechaexpedicion', models.DateField(blank=True, db_column='fechaExpedicion', null=True)),
                ('actualizacion', models.ForeignKey(blank=True, db_column='actualizacion', null=True, on_delete=django.db.models.deletion.PROTECT, to='asesores.AsesoresDb')),
                ('ciudad', models.ForeignKey(blank=True, db_column='ciudad', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DbAbogados.ciudad+', to='municipio.Municipio')),
                ('ciudad2', models.ForeignKey(blank=True, db_column='ciudad2', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DbAbogados.ciudad2+', to='municipio.Municipio')),
                ('ciudadexpedicion', models.ForeignKey(blank=True, db_column='ciudadExpedicion', null=True, on_delete=django.db.models.deletion.PROTECT, to='municipio.Municipio')),
                ('contacto', models.ForeignKey(blank=True, db_column='contacto', null=True, on_delete=django.db.models.deletion.PROTECT, to='origen_contacto.OrigenContacto')),
                ('genero', models.ForeignKey(db_column='genero', on_delete=django.db.models.deletion.DO_NOTHING, to='genero.Genero')),
                ('perfil', models.ForeignKey(blank=True, db_column='perfil', null=True, on_delete=django.db.models.deletion.PROTECT, to='perfil.Perfil')),
            ],
            options={
                'verbose_name': 'Abogado',
                'verbose_name_plural': 'Informe de DB_ABOGADOS',
                'db_table': 'db_abogados',
                'ordering': ['codigo'],
                'managed': True,
            },
        ),
    ]
