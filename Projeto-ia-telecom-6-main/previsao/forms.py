from django import forms
from .utils import get_form_choices


class PrevisaoForm(forms.Form):
    tipo_atendimento_id = forms.TypedChoiceField(
        label="Tipo de Atendimento",
        coerce=int,
        choices=(),
        error_messages={
            "required": "Selecione o tipo de atendimento.",
            "invalid_choice": "Selecione uma opção válida.",
        },
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Selecione o tipo de atendimento da OS."
    )

    produto_id = forms.IntegerField(
        label="Produto (ID)",
        min_value=1,
        error_messages={
            "required": "Informe o produto.",
            "invalid": "Digite um número válido.",
        },
        widget=forms.NumberInput(attrs={
            "class": "form-input",
            "placeholder": "Ex: 414898",
        }),
        help_text="Por enquanto, informe manualmente o produto_id existente em export_produtos.csv."
    )

    defeito_reclamado_id = forms.TypedChoiceField(
        label="Defeito Reclamado",
        required=False,
        choices=(),
        coerce=int,
        empty_value=0,
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Opcional."
    )

    defeito_constatado_id = forms.TypedChoiceField(
        label="Defeito Constatado",
        required=False,
        choices=(),
        coerce=int,
        empty_value=0,
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Opcional."
    )

    solucao_id = forms.TypedChoiceField(
        label="Solução",
        required=False,
        choices=(),
        coerce=int,
        empty_value=0,
        widget=forms.Select(attrs={"class": "form-input"}),
        help_text="Opcional."
    )

    data_abertura = forms.DateField(
        label="Data de Abertura",
        input_formats=["%Y-%m-%d"],
        error_messages={
            "required": "Informe a data de abertura.",
            "invalid": "Use uma data válida.",
        },
        widget=forms.DateInput(attrs={
            "class": "form-input",
            "type": "date",
        }),
        help_text="A data será usada para gerar ano, mês, dia e dia da semana."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = get_form_choices()
        self.fields["tipo_atendimento_id"].choices = choices["tipos_atendimento"]
        self.fields["defeito_reclamado_id"].choices = choices["defeitos_reclamados"]
        self.fields["defeito_constatado_id"].choices = choices["defeitos_constatados"]
        self.fields["solucao_id"].choices = choices["solucoes"]

    def clean(self):
        cleaned_data = super().clean()

        produto_id = cleaned_data.get("produto_id")
        tipo_atendimento_id = cleaned_data.get("tipo_atendimento_id")

        if produto_id is not None and produto_id <= 0:
            self.add_error("produto_id", "O produto deve ser maior que zero.")

        if tipo_atendimento_id is not None and tipo_atendimento_id <= 0:
            self.add_error("tipo_atendimento_id", "O tipo de atendimento deve ser maior que zero.")

        return cleaned_data