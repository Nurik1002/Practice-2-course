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
        ('LPDDR', 'LPDDR'),
        ('LPDDR2', 'LPDDR2'),
        ('LPDDR3', 'LPDDR3'),
        ('LPDDR4', 'LPDDR4'),
        ('LPDDR5', 'LPDDR5'),

        ('DDR', 'DDR'),
        ('DDR2', 'DDR2'),
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
    description = models.TextField(verbose_name = 'Qo\'shimcha ma\'lumot')

    
    
    
