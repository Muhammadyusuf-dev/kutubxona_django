from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length = 100)
    guruh = models.CharField(max_length=100)
    kurs = models.CharField(max_length=100)
    kitob_soni = models.IntegerField()

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabar"

    def __str__(self):
        return f"{self.ism}"

class Muallif(models.Model):

    class Jins(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    ism = models.CharField(max_length = 100)
    jins = models.CharField(max_length = 100, choices=Jins.choices)
    tugilgan_sana = models.DateField()
    kitob_soni = models.IntegerField()
    tirik = models.BooleanField()

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"

    def __str__(self):
        return f"{self.ism}"

class Kitob(models.Model):
    nom = models.CharField(max_length = 100)
    janr = models.CharField(max_length = 100)
    sahifa = models.IntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return f"{self.nom}"

class Admin(models.Model):
    ism = models.CharField(max_length = 100)
    ish_vaqti = models.IntegerField()

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Adminlar"

    def __str__(self):
        return f"{self.ism}"

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sanasi = models.DateField()

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Recordlar"

    def __str__(self):
        return f"{self.talaba} {self.kitob}"