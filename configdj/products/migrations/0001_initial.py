# Generated by Django 3.2.19 on 2023-05-24 03:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Firma nomi')),
            ],
            options={
                'verbose_name': 'Firma',
                'verbose_name_plural': '2. Firma',
            },
        ),
        migrations.CreateModel(
            name='Smartwatch',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('prosessor', models.CharField(max_length=255, verbose_name='Prosessor')),
                ('ram', models.PositiveSmallIntegerField(verbose_name='Operativ xotira GB')),
                ('memory', models.PositiveSmallIntegerField(verbose_name='Tashqi xotira GB')),
                ('battery', models.CharField(max_length=255, verbose_name='Batareyka')),
                ('image', models.ImageField(upload_to='smartwatch/')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Smartphone soni')),
                ('description', models.TextField(null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.firma', verbose_name='Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('prosessor', models.CharField(max_length=255, verbose_name='Prosessor')),
                ('ram', models.PositiveSmallIntegerField(verbose_name='Operativ xotira GB')),
                ('ram_type', models.CharField(choices=[('LPDDR3', 'LPDDR3'), ('LPDDR4', 'LPDDR4'), ('LPDDR4X', 'LPDDR4X'), ('LPDDR5', 'LPDDR5'), ('LPDDR5X', 'LPDDR5X')], max_length=20, verbose_name='Operativ xotira turi')),
                ('memory', models.PositiveSmallIntegerField(verbose_name='Tashqi xotira GB')),
                ('memory_type', models.CharField(choices=[('CD', 'CD'), ('SDHC', 'SDHC'), ('SDXC', 'SDXC'), ('SDUC', 'SDUC')], max_length=15, verbose_name='Tashqi xotira turi')),
                ('frot_camera', models.CharField(max_length=500, verbose_name='Old kamerasi')),
                ('back_camera', models.CharField(max_length=1000, verbose_name='Orqa kamerasi')),
                ('video_card', models.CharField(max_length=255, null=True, verbose_name='Video karta')),
                ('display', models.CharField(max_length=255, verbose_name='Display')),
                ('battery', models.CharField(max_length=255, verbose_name='Batareyka')),
                ('image', models.ImageField(upload_to='smartphone/')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Smartphone soni')),
                ('description', models.TextField(null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.firma', verbose_name='Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Otherproducts',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('image', models.ImageField(upload_to='other/')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Soni')),
                ('description', models.TextField(null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.firma', verbose_name='Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('prosessor', models.CharField(max_length=255, verbose_name='Prosessor')),
                ('ram', models.PositiveSmallIntegerField(verbose_name='Operativ xotira GB')),
                ('ram_type', models.CharField(choices=[('LPDDR3', 'LPDDR3'), ('LPDDR4', 'LPDDR4'), ('LPDDR5', 'LPDDR5'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=20, verbose_name='Operativ xotira turi')),
                ('memory', models.PositiveSmallIntegerField(verbose_name='Tashqi xotira GB')),
                ('memory_type', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD'), ('NVMe', 'NVMe')], max_length=15, verbose_name='Tashqi xotira turi')),
                ('video_card', models.CharField(max_length=255, null=True, verbose_name='Video karta')),
                ('display', models.CharField(max_length=255, verbose_name='Display')),
                ('image', models.ImageField(upload_to='computer/')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Kompyuter soni')),
                ('description', models.TextField(null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.firma', verbose_name='Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('image', models.ImageField(upload_to='accessory/')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Aksesuar soni')),
                ('description', models.TextField(null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.firma', verbose_name='Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_num', models.CharField(max_length=15, verbose_name='Telefon raqam')),
                ('telegram_id', models.CharField(max_length=15, verbose_name='Telegram id')),
                ('telegram_username', models.CharField(max_length=55, null=True, verbose_name='Telegram username')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin yoki foydalanuvchi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Foydalanuvchilar',
                'verbose_name_plural': '1. Foydalanuvchilar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
