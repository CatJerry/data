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


class CoinData(models.Model):
    market = models.TextField()
    candle_date_time_utc = models.DateTimeField()
    candle_date_time_kst = models.DateTimeField()
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    timestamp = models.BigIntegerField()
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    unit = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'coin_data'
        # # 기본키 설정
        unique_together = (('market', 'candle_date_time_kst'),)


class CoinName(models.Model):
    index = models.BigIntegerField(primary_key=True)
    market = models.TextField()
    korean_name = models.TextField()
    english_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'coin_name'


class CoinVolume(models.Model):
    market = models.TextField()
    trade_date = models.TextField()
    trade_time = models.TextField()
    trade_date_kst = models.TextField()
    trade_time_kst = models.TextField()
    trade_timestamp = models.BigIntegerField()
    opening_price = models.BigIntegerField()
    high_price = models.BigIntegerField()
    low_price = models.BigIntegerField()
    trade_price = models.BigIntegerField()
    prev_closing_price = models.FloatField()
    change = models.TextField()
    change_price = models.FloatField()
    change_rate = models.FloatField()
    signed_change_price = models.FloatField()
    signed_change_rate = models.FloatField()
    trade_volume = models.FloatField()
    acc_trade_price = models.FloatField()
    acc_trade_price_24h = models.FloatField()
    acc_trade_volume = models.FloatField()
    acc_trade_volume_24h = models.FloatField()
    highest_52_week_price = models.FloatField()
    highest_52_week_date = models.TextField()
    lowest_52_week_price = models.FloatField()
    lowest_52_week_date = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'coin_volume'


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
