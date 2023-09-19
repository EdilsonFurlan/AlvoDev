from django.db import models
from mat_prima.models import CategMatPrima

class ProdutoPadrao(models.Model):
    TIPO_CHOICES=(('NE','NECESSAIRE'),
                  ('BO','BOLSA'),
                  ('ES','ESTOJO'),
                  ('SA','SACOLA'))
    nome=models.CharField(max_length=50)
    tamanho=models.CharField(max_length=30)
    preco_venda=models.DecimalField(max_digits=5,decimal_places=2)
    tipo=models.CharField(max_length=2,choices=TIPO_CHOICES)
    categoria=models.ManyToManyField(CategMatPrima,through='ItensCategMatPrima')
    
    def __str__(self):
        return str(self.nome)
    
class ItensCategMatPrima(models.Model):
    quantidade=models.IntegerField()
    categmatprima=models.ForeignKey(CategMatPrima,on_delete=models.CASCADE)
    produtopadrao=models.ForeignKey(ProdutoPadrao,on_delete=models.CASCADE)