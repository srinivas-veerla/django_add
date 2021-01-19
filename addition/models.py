from django.db import models

class History(models.Model):
    num1=models.IntegerField(null=False)
    num2=models.IntegerField(null=False)
    res=models.IntegerField(null=False)

    def __str__(self):
        return "Data {}".format(self.id)





