# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import os
from django.conf import settings


def core_biciness_path(instance, filename):
    image_name = '{0}/{1}'.format(instance.marca_cicla, filename)
    fullpath = os.path.join(settings.MEDIA_ROOT, image_name)

    if os.path.exists(fullpath):
        os.remove(fullpath)
    
    return image_name

class AccountEmailaddress(models.Model):
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
    
    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class DjangoSite(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)

class Catalogo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    id_registro = models.ForeignKey('AuthUser', models.CASCADE, db_column='ID_REGISTRO', blank=True, null=True)  # Field name made lowercase.
    monbre_producto = models.CharField(max_length = 25, db_column='MONBRE_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    nombre_vendedor = models.CharField(max_length = 25, db_column='NOMBRE_VENDEDOR', blank=True, null=True)  # Field name made lowercase.
    marca_clica = models.CharField(max_length = 25, db_column='MARCA_CLICA', blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='PRECIO', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ciudad = models.CharField(max_length = 25, db_column='CIUDAD', blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='CONTACTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATALOGO'


class Venta(models.Model):
    id_referencia_venta = models.IntegerField(db_column='ID_REFERENCIA_VENTA', primary_key=True, blank=False, null=False)  # Field name made lowercase. This field type is a guess.
    id_catalogo = models.ForeignKey(Catalogo, on_delete = models.CASCADE, db_column='ID_CATALOGO', blank=True, null=False)  # Field name made lowercase.
    ciudad = models.CharField(max_length = 25, db_column='CIUDAD', blank=True, null=True)  # Field name made lowercase.
    marca_cicla = models.CharField(max_length = 25, db_column='MARCA_CICLA', blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='PRECIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contacto = models.IntegerField(db_column='CONTACTO', blank=True, null=True)  # Field name made lowercase.
    imagen = models.ImageField(db_column='IMAGEN', blank=True, null=True, upload_to = core_biciness_path)  # Field name made lowercase.

    def __str__(self):
        return self.marca_cicla

    class Meta:
        managed = False
        db_table = 'VENTA'
        ordering = ['id_referencia_venta'] # Ascending by id

