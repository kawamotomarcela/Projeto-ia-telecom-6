from django.db import models


class HistoricoPrevisao(models.Model):
    tipo_atendimento_id = models.IntegerField(db_index=True)
    produto_id = models.IntegerField(db_index=True)

    defeito_reclamado_id = models.IntegerField(null=True, blank=True, db_index=True)
    defeito_constatado_id = models.IntegerField(null=True, blank=True, db_index=True)
    solucao_id = models.IntegerField(null=True, blank=True, db_index=True)

    data_abertura = models.DateField(db_index=True)

    fabrica_id = models.IntegerField()
    linha_id = models.IntegerField()
    familia_id = models.IntegerField()

    resultado_horas = models.FloatField()

    criado_em = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Histórico de Previsão"
        verbose_name_plural = "Histórico de Previsões"
        ordering = ["-criado_em"]

    def __str__(self):
        return (
            f"Previsão #{self.id} | "
            f"Produto {self.produto_id} | "
            f"{self.resultado_horas:.2f}h"
        )