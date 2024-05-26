# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bloque(models.Model):
    blo_id = models.AutoField(primary_key=True)
    blo_nombre = models.CharField(max_length=30)
    blo_fac = models.ForeignKey('Facultad', models.DO_NOTHING, blank=True, null=True)
    blo_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bloque'


class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=30)
    cat_tipobien = models.CharField(db_column='cat_tipoBien', max_length=30)  # Field name made lowercase.
    cat_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'categoria'


class Categoriadetalle(models.Model):
    det_cat_id = models.AutoField(primary_key=True)
    det_cat_nombre = models.CharField(max_length=30)
    det_cat_cat = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    det_cat_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'categoriadetalle'


class Componente(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_serie = models.CharField(max_length=30)
    com_codigo_bien = models.CharField(max_length=30, blank=True, null=True)
    com_codigo_uta = models.CharField(max_length=255)
    com_det_cat = models.ForeignKey(Categoriadetalle, models.DO_NOTHING)
    com_modelo = models.CharField(max_length=30, blank=True, null=True)
    com_marca = models.CharField(max_length=30, blank=True, null=True)
    com_caracteristica = models.CharField(max_length=30)
    com_dep = models.ForeignKey('Dependencia', models.DO_NOTHING, blank=True, null=True)
    com_anio_ingreso = models.TextField(blank=True, null=True)  # This field type is a guess.
    com_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'componente'


class Dependencia(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_nombre = models.CharField(max_length=30, blank=True, null=True)
    dep_descripcion = models.CharField(max_length=30, blank=True, null=True)
    dep_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dependencia'


class DetalleTecnologico(models.Model):
    det_tec_id = models.AutoField(primary_key=True)
    det_tec_tec = models.ForeignKey('Tecnologico', models.DO_NOTHING)
    det_tec_com_adquirido = models.ForeignKey(Componente, models.DO_NOTHING, blank=True, null=True)
    det_tec_com_uso = models.ForeignKey(Componente, models.DO_NOTHING, related_name='detalletecnologico_det_tec_com_uso_set', blank=True, null=True)
    det_tec_descripcion_repotencia = models.CharField(max_length=30, blank=True, null=True)
    det_tec_estado_repotencia = models.IntegerField(blank=True, null=True)
    det_tec_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'detalle_tecnologico'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Facultad(models.Model):
    fac_id = models.AutoField(primary_key=True)
    fac_nombre = models.CharField(max_length=30)
    fac_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'facultad'


class Inmobiliario(models.Model):
    inm_id = models.AutoField(primary_key=True)
    inm_codigo = models.CharField(unique=True, max_length=30)
    inm_categoria = models.CharField(max_length=30)
    inm_dep = models.ForeignKey(Dependencia, models.DO_NOTHING, blank=True, null=True)
    inm_serie = models.CharField(max_length=30, blank=True, null=True)
    inm_modelo = models.CharField(max_length=30, blank=True, null=True)
    inm_marca = models.CharField(max_length=30, blank=True, null=True)
    inm_encargado = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    inm_anio_ingreso = models.TextField(blank=True, null=True)  # This field type is a guess.
    inm_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'inmobiliario'


class Localizacion(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_nombre = models.CharField(max_length=30)
    loc_ubi = models.ForeignKey('Ubicacion', models.DO_NOTHING)
    loc_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'localizacion'


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=30)
    rol_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rol'


class Software(models.Model):
    sof_id = models.AutoField(primary_key=True)
    sof_nombre = models.CharField(max_length=30)
    sof_version = models.CharField(max_length=30)
    sof_tipo = models.CharField(max_length=30)
    sof_duracion = models.CharField(max_length=30)
    sof_descripcion = models.CharField(max_length=200)
    sof_tip_ubi = models.ForeignKey('TipoUbicacion', models.DO_NOTHING)
    sof_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'software'


class Tecnologico(models.Model):
    tec_id = models.AutoField(primary_key=True)
    tec_codigo = models.CharField(unique=True, max_length=30)
    tec_serie = models.CharField(max_length=30, blank=True, null=True)
    tec_modelo = models.CharField(max_length=30, blank=True, null=True)
    tec_marca = models.CharField(max_length=30, blank=True, null=True)
    tec_ip = models.CharField(max_length=30, blank=True, null=True)
    tec_anio_ingreso = models.TextField(blank=True, null=True)  # This field type is a guess.
    tec_encargado = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    tec_loc = models.ForeignKey(Localizacion, models.DO_NOTHING, blank=True, null=True)
    tec_cat = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    tec_dep = models.ForeignKey(Dependencia, models.DO_NOTHING, blank=True, null=True)
    tec_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tecnologico'


class TipoUbicacion(models.Model):
    tip_ubi_id = models.AutoField(primary_key=True)
    tip_ubi_nombre = models.CharField(max_length=30)
    tip_ubi_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_ubicacion'


class Ubicacion(models.Model):
    ubi_id = models.AutoField(primary_key=True)
    ubi_nombre = models.CharField(max_length=30)
    ubi_blo = models.ForeignKey(Bloque, models.DO_NOTHING)
    ubi_tip_ubi = models.ForeignKey(TipoUbicacion, models.DO_NOTHING)
    ubi_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_correo = models.CharField(max_length=30)
    usu_contrasenia = models.CharField(max_length=30)
    usu_cedula = models.CharField(max_length=10)
    usu_nombres = models.CharField(max_length=30)
    usu_apellidos = models.CharField(max_length=30)
    usu_rol = models.ForeignKey(Rol, models.DO_NOTHING)
    usu_habilitado = models.CharField(max_length=20)
    usu_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usuario'
