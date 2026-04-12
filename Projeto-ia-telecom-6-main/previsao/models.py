from django.db import models


class HistoricoPrevisao(models.Model):
    tipo_atendimento_id = models.IntegerField()
    produto_id = models.IntegerField()

    defeito_reclamado_id = models.IntegerField(null=True, blank=True)
    defeito_constatado_id = models.IntegerField(null=True, blank=True)
    solucao_id = models.IntegerField(null=True, blank=True)

    data_abertura = models.DateField()

    fabrica_id = models.IntegerField()
    linha_id = models.IntegerField()
    familia_id = models.IntegerField()

    resultado_horas = models.FloatField()

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Histórico de Previsão"
        verbose_name_plural = "Histórico de Previsões"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Previsão #{self.id} | Produto {self.produto_id} | {self.resultado_horas:.2f}h"