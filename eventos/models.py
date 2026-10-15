from django.db import models

# Create your models here.


class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    capacidade = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Locais"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, related_name='eventos')
    categoria = models.ManyToManyField(Categoria, null=True, blank=True, related_name='eventos')
    
    def vagas_restantes(self):
        total_inscricoes = self.inscricoes.count()
        return self.local.capacidade - total_inscricoes
    
    class Meta:
        ordering = ['-inicio']
    
    def __str__(self):
        return self.titulo
    
class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    palestrante = models.CharField(max_length=100)
    horario = models.DateTimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='atividades')
    
    class Meta:
        ordering = ['horario']
    
    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    
    class Meta:
        verbose_name_plural = "Inscrições"
    
    def __str__(self):
        return self.nome
    
class Relatorio(models.Model):
    presentes = models.IntegerField()
    observacoes = models.TextField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='relatorios')
    
    def __str__(self):
        return f'Relatório do evento {self.evento.titulo}'
    
    