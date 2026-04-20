from django.contrib import admin
from .models import HistoricoPrevisao

admin.site.site_header = "Painel Administrativo - Predição de Tempo"
admin.site.site_title = "Administração"
admin.site.index_title = "Gerenciamento do Sistema"


@admin.register(HistoricoPrevisao)
class HistoricoPrevisaoAdmin(admin.ModelAdmin):
    change_list_template = "admin/previsao/historicoprevisao/listagem.html"

    list_display = (
        "id",
        "produto_id",
        "tipo_atendimento_id",
        "defeito_constatado_id",
        "resultado_formatado",
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

    readonly_fields = (
        "criado_em",
    )

    ordering = ("-criado_em",)
    list_per_page = 25
    date_hierarchy = "criado_em"

    def resultado_formatado(self, obj):
        return f"{obj.resultado_horas:.2f} h"

    resultado_formatado.short_description = "Resultado"