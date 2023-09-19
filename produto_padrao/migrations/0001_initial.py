# Generated by Django 4.2.3 on 2023-08-03 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mat_prima', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensCategMatPrima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('categmatprima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mat_prima.categmatprima')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoPadrao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tamanho', models.CharField(max_length=30)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo', models.CharField(choices=[('NE', 'NECESSAIRE'), ('BO', 'BOLSA'), ('ES', 'ESTOJO'), ('SA', 'SACOLA')], max_length=2)),
                ('categoria', models.ManyToManyField(through='produto_padrao.ItensCategMatPrima', to='mat_prima.categmatprima')),
            ],
        ),
        migrations.AddField(
            model_name='itenscategmatprima',
            name='produtopadrao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto_padrao.produtopadrao'),
        ),
    ]
