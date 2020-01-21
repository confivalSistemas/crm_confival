# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now 

# importanto modelos
from genero.models import Genero
from municipio.models import Municipio
from perfil_asesor.models import Perfilasesor
from comisiones.models import Comisiones


class AsesoresDb(models.Model):
    cod_asesor = models.AutoField(primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey(Municipio, db_column='ciudad', blank=True, null=True, related_name='AsesoresDb.ciudad+', on_delete=models.PROTECT)
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey(Municipio, db_column='ciudad2', blank=True, null=True, related_name='AsesoresDb.ciudad2+', on_delete=models.PROTECT)
    celular = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    t_asesor = models.CharField(max_length=15, blank=True, null=True)
    comision = models.ForeignKey(Comisiones, db_column='comision', blank=True, null=True, on_delete=models.PROTECT)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    c_cedula = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    fecha_s = models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')
    perfil = models.ForeignKey(Perfilasesor, db_column='perfil', blank=True, null=True, on_delete=models.PROTECT)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey(Municipio, db_column='ciudadExpedicion', blank=True, null=True, related_name='AsesoresDb.ciudadexpedicion+', on_delete=models.PROTECT)  # Field name made lowercase.
    genero = models.ForeignKey(Genero, db_column='genero', on_delete=models.PROTECT)
    cod_ciudad = models.CharField(max_length=15, blank=True, null=True)
    municipio = models.CharField(max_length=27, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'asesores_db'
        verbose_name = 'Asesor'
        verbose_name_plural = 'Asesores' 
        ordering = ["cod_asesor"]

    def __str__(self):
        return self.nombre +" "+ self.apellido
    
