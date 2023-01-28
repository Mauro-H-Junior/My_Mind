from django.db import models

# Create your models here.
tipo_escolhas_avaliacao_diaria = {
    ('PÉSSIMO', 'PÉSSIMO SUPORTE'),    
    ('RUIM', 'RUIM'),    
    ('BOM', 'BOM'),
    ('EXCELENTE', 'EXCELENTE'),

}

tipo_escolhas_alerta_cristes = {
    ('PANICO', 'PANICO'),    
    ('ANSIEDADE', 'ANSIEDADE'),    
    ('DEPRESSAO DE CURSO', 'DEPRESSAO'),
}

acontecimento_negativo = models.TextField("Assunto do chamado",max_length=100)
acontecimento_positivo = models.TextField("Assunto do chamado",max_length=100)
