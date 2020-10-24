from django.db import models


class PriceGroup(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class PriceSubGroup(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class PriceItem(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)

    group = models.ForeignKey(PriceGroup, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(PriceSubGroup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.group}, {self.sub_group} - {self.name}'

