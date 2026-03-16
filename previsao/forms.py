from django import forms


class PrevisaoForm(forms.Form):
    tipo_atendimento_id = forms.IntegerField(
        label="Tipo de Atendimento (ID)",
        min_value=1,
        error_messages={
            "required": "Informe o tipo de atendimento.",
            "invalid": "Digite um número válido.",
        },
        widget=forms.NumberInput(attrs={
            "class": "form-input",
            "placeholder": "Ex: 252",
        }),
        help_text="Digite o ID do tipo de atendimento."
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
        help_text="Digite o produto_id existente em export_produtos.csv."
    )

    defeito_reclamado_id = forms.IntegerField(
        label="Defeito Reclamado (ID)",
        required=False,
        min_value=0,
        error_messages={
            "invalid": "Digite um número válido.",
        },
        widget=forms.NumberInput(attrs={
            "class": "form-input",
            "placeholder": "Opcional",
        }),
        help_text="Preencha apenas se esse campo existir para a OS."
    )

    defeito_constatado_id = forms.IntegerField(
        label="Defeito Constatado (ID)",
        required=False,
        min_value=0,
        error_messages={
            "invalid": "Digite um número válido.",
        },
        widget=forms.NumberInput(attrs={
            "class": "form-input",
            "placeholder": "Opcional",
        }),
        help_text="Preencha apenas se esse campo existir para a OS."
    )

    solucao_id = forms.IntegerField(
        label="Solução (ID)",
        required=False,
        min_value=0,
        error_messages={
            "invalid": "Digite um número válido.",
        },
        widget=forms.NumberInput(attrs={
            "class": "form-input",
            "placeholder": "Opcional",
        }),
        help_text="Preencha apenas se esse campo existir para a OS."
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

    def clean(self):
        cleaned_data = super().clean()

        produto_id = cleaned_data.get("produto_id")
        tipo_atendimento_id = cleaned_data.get("tipo_atendimento_id")

        if produto_id is not None and produto_id <= 0:
            self.add_error("produto_id", "O produto deve ser maior que zero.")

        if tipo_atendimento_id is not None and tipo_atendimento_id <= 0:
            self.add_error("tipo_atendimento_id", "O tipo de atendimento deve ser maior que zero.")

        return cleaned_data