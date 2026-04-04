from django.contrib import admin
from .models import HistoricoPrevisao


@admin.register(HistoricoPrevisao)
class HistoricoPrevisaoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "produto_id",
        "tipo_atendimento_id",
        "resultado_horas",
        "data_abertura",
        "criado_em",
    )
    list_filter = (
        "tipo_atendimento_id",
        "data_abertura",
        "criado_em",
    )
    search_fields = (
        "produto_id",
        "tipo_atendimento_id",
        "defeito_reclamado_id",
        "defeito_constatado_id",
        "solucao_id",
    )
    ordering = ("-criado_em",)