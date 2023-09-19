from django.db import models

class CategMatPrima(models.Model):
    UNIDADE_CHOICE=(('MT','METRO'),('PÇ','PEÇA'))
    nome=models.CharField(max_length=50)
    preco_unit=models.DecimalField(max_digits=7,decimal_places=2)
    unidade=models.CharField(max_length=2,choices=UNIDADE_CHOICE)

    def __str__(self):
        return str(self.nome)
    
class MatPrima(models.Model):
    nome=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategMatPrima,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)
