AUTH_USER_MODEL = 'products.Users'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Praktika',
        'USER': 'root',
        'PASSWORD': 'nurik0210',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.db import models
from django.contrib.auth.models import AbstractUser

# ------------------ Foydalanuvchilar bazasi -------------------------------

# CREATE TABLE IF NOT EXISTS `Telegramshop`.`user` (
#   `user_id` INT NOT NULL,
#   `last_name` VARCHAR(55) NOT NULL,
#   `first_name` VARCHAR(55) NOT NULL,
#   `email` VARCHAR(45) NOT NULL,
#   `phone_num` VARCHAR(45) NOT NULL,
#   `telegram_id` VARCHAR(45) NOT NULL,
#   `telegram_username` VARCHAR(45) NOT NULL,
#   `is_admin` INT NOT NULL,
#   PRIMARY KEY (`user_id`))



class Users(AbstractUser):
    phone_num = models.CharField(verbose_name = 'Telefon raqam', max_length = 15, null = False)
    telegram_id = models.CharField(verbose_name = 'Telegram id', max_length = 15 , null = False)
    telegram_username = models.CharField(verbose_name = 'Telegram username', max_length = 55, null = True)
    is_admin = models.BooleanField(verbose_name = 'Admin yoki foydalanuvchi', default=False)

    def __str__():
        return f"{id} : {last_name} {first_name} "
    
    class Meta:
        verbose_name = 'Foydalanuvchilar'
        verbose_name_plural = '1. Foydalanuvchilar'
    

# ----------------------- Firmalar bazasi --------------------------------

# CREATE TABLE IF NOT EXISTS `firma` (
#   `id` INT NOT NULL,
#   `name` VARCHAR(255) NOT NULL,

class Firma(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(verbose_name = 'Firma nomi', max_length = 255)

    def __str__():
        return f"{name}"
    
    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = '2. Firma'
    

# --------------------- Kompyuterlar bazasi --------------------------------

# CREATE TABLE IF NOT EXISTS `Telegramshop`.`computer` (
#   `product_id` INT NOT NULL,
#   `name` VARCHAR(255) NOT NULL,
#   `firma_id` INT NOT NULL,
#   `price` REAL NOT NULL,
#   `prosessor` VARCHAR(45) NOT NULL,
#   `ram` INT NOT NULL,
#   `ram_type` VARCHAR(45) NOT NULL,
#   `memory` VARCHAR(45) NOT NULL,
#   `memory_type` VARCHAR(45) NOT NULL,
#   `video_karta` VARCHAR(45) NOT NULL,
#   `display` VARCHAR(255) NULL,
#   `image_path` VARCHAR(255) NOT NULL,
#   `quantity` INT NULL,
#   `description` TEXT NULL,


class Computer(models.Model):

    TASHQI_XOTIRA_TURLARI = (
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
        ('NVMe', 'NVMe'),
    )

    RAM_TURLARI = (
        ('LPDDR3', 'LPDDR3'),
        ('LPDDR4', 'LPDDR4'),
        ('LPDDR5', 'LPDDR5'),
        
        ('DDR3', 'DDR3'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
        
    )

    id = models.PositiveBigIntegerField(primary_key = True)
    name = models.CharField(verbose_name = 'Nomi', max_length = 255)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, verbose_name = 'Firma')
    price = models.PositiveIntegerField(verbose_name = 'Narxi')
    prosessor = models.CharField(verbose_name = 'Prosessor', max_length = 255)
    ram = models.PositiveSmallIntegerField(verbose_name = 'Operativ xotira GB')
    ram_type = models.CharField(verbose_name = 'Operativ xotira turi', max_length = 20, choices=RAM_TURLARI)
    memory = models.PositiveSmallIntegerField(verbose_name = 'Tashqi xotira GB')
    memory_type = models.CharField(verbose_name = 'Tashqi xotira turi', max_length=15, choices=TASHQI_XOTIRA_TURLARI)
    video_card = models.CharField(verbose_name = 'Video karta', max_length=255, null=True)
    display = models.CharField(verbose_name = 'Display', max_length=255)
    image = models.ImageField(upload_to='computer/')
    quantity = models.PositiveSmallIntegerField(verbose_name = 'Kompyuter soni')
    description = models.TextField(verbose_name = 'Qo\'shimcha ma\'lumot', null = True)



# ----------------------- Smartphone bazasi

# CREATE TABLE IF NOT EXISTS `Telegramshop`.`smart_phone` (
#   `product_id` INT NOT NULL,
#   `name` VARCHAR(255) NOT NULL,
#   `firma_id` INT NOT NULL,
#   `price` REAL NOT NULL,
#   `prosessor` VARCHAR(45) NOT NULL,
#   `ram` INT NOT NULL,
#   `ram_type` VARCHAR(45) NOT NULL,
#   `memory` VARCHAR(45) NOT NULL,
#   `memory_type` VARCHAR(45) NOT NULL,
#   `front_camera` VARCHAR(255) NOT NULL,
#   `back_camera` VARCHAR(255) NOT NULL,
#   `video_karta` VARCHAR(45) NOT NULL,
#   `image_path` VARCHAR(255) NOT NULL,
#   `quantity` INT NULL,
#   `description` TEXT NULL,

class Smartphone(models.Model):
    TASHQI_XOTIRA_TURLARI = (
        ('CD', 'CD'),
        ('SDHC', 'SDHC'),
        ('SDXC', 'SDXC'),
        ('SDUC', 'SDUC'),
    )

    RAM_TURLARI = (
        ('LPDDR3', 'LPDDR3'),
        ('LPDDR4', 'LPDDR4'),
        ('LPDDR4X', 'LPDDR4X'),
        ('LPDDR5', 'LPDDR5'),  
        ('LPDDR5X', 'LPDDR5X'),        
    )

    id = models.PositiveBigIntegerField(primary_key = True)
    name = models.CharField(verbose_name = 'Nomi', max_length = 255)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, verbose_name = 'Firma')
    price = models.PositiveIntegerField(verbose_name = 'Narxi')
    prosessor = models.CharField(verbose_name = 'Prosessor', max_length = 255)
    ram = models.PositiveSmallIntegerField(verbose_name = 'Operativ xotira GB')
    ram_type = models.CharField(verbose_name = 'Operativ xotira turi', max_length = 20, choices=RAM_TURLARI)
    memory = models.PositiveSmallIntegerField(verbose_name = 'Tashqi xotira GB')
    memory_type = models.CharField(verbose_name = 'Tashqi xotira turi', max_length=15, choices=TASHQI_XOTIRA_TURLARI)
    frot_camera = models.CharField(verbose_name = 'Old kamerasi', max_length = 500)
    back_camera = models.CharField(verbose_name = 'Orqa kamerasi', max_length = 1000)
    video_card = models.CharField(verbose_name = 'Video karta', max_length = 255, null=True)
    display = models.CharField(verbose_name = 'Display', max_length = 255)
    battery = models.CharField(verbose_name = 'Batareyka', max_length = 255)
    image = models.ImageField(upload_to='smartphone/')
    quantity = models.PositiveSmallIntegerField(verbose_name = 'Smartphone soni')
    description = models.TextField(verbose_name = 'Qo\'shimcha ma\'lumot', null = True)





# -------------------------- Smart Watch bazasi --------------------------

# CREATE TABLE IF NOT EXISTS `Telegramshop`.`smart_watch` (
#   `product_id` INT NOT NULL,
#   `name` VARCHAR(255) NOT NULL,
#   `firma_id` INT NOT NULL,
#   `price` REAL NOT NULL,
#   `prosessor` VARCHAR(45) NOT NULL,
#   `ram` INT NOT NULL,
#   `memory` VARCHAR(45) NOT NULL,
#   `image_path` VARCHAR(255) NOT NULL,
#   `quantity` INT NULL,
#   `description` TEXT NULL,

class Smartwatch(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    name = models.CharField(verbose_name = 'Nomi', max_length = 255)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, verbose_name = 'Firma')
    price = models.PositiveIntegerField(verbose_name = 'Narxi')
    prosessor = models.CharField(verbose_name = 'Prosessor', max_length = 255)
    ram = models.PositiveSmallIntegerField(verbose_name = 'Operativ xotira GB')
    memory = models.PositiveSmallIntegerField(verbose_name = 'Tashqi xotira GB')
    battery = models.CharField(verbose_name = 'Batareyka', max_length = 255)
    image = models.ImageField(upload_to='smartwatch/')
    quantity = models.PositiveSmallIntegerField(verbose_name = 'Smartphone soni')
    description = models.TextField(verbose_name = 'Qo\'shimcha ma\'lumot', null = True)


# -------------------- Aksesuarlar bazsi ------------------

# CREATE TABLE IF NOT EXISTS `Telegramshop`.`accessory` (
#   `id` INT NOT NULL,
#   `name` VARCHAR(255) NOT NULL,
#   `price` REAL NOT NULL,
#   `description` TEXT NULL,
#   `firma_id` INT NOT NULL,
#   `quantity` INT NULL,

class Accessory(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    name = models.CharField(verbose_name = 'Nomi', max_length = 255)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, verbose_name = 'Firma')
    price = models.PositiveIntegerField(verbose_name = 'Narxi')
    image = models.ImageField(upload_to='accessory/')
    quantity = models.PositiveSmallIntegerField(verbose_name = 'Aksesuar soni')
    description = models.TextField(verbose_name = 'Qo\'shimcha ma\'lumot', null = True)


# -------------------- Boshqa mahsulotlar bazasi --------------------
# CREATE TABLE IF NOT EXISTS `Telegramshop`.`other_products` (
#   `id` INT NOT NULL,
#   `name` VARCHAR(255) NOT NULL,
#   `price` REAL NOT NULL,
#   `description` TEXT NULL,
#   `firma_id` INT NOT NULL,
#   `quantity` INT NULL,

class Otherproducts(models.Model):
    id = models.PositiveBigIntegerField(primary_key = True)
    name = models.CharField(verbose_name = 'Nomi', max_length = 255)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, verbose_name = 'Firma')
    price = models.PositiveIntegerField(verbose_name = 'Narxi')
    image = models.ImageField(upload_to='other/')
    quantity = models.PositiveSmallIntegerField(verbose_name = 'Soni')
    description = models.TextField(verbose_name = 'Qo\'shimcha ma\'lumot', null = True)


