from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class serializerEstudanteTestCase(TestCase):
    
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testemodelo@gmail.com',
            cpf = '66066550055',
            data_nascimento = '1987-06-01',
            celular = '21 99999-9999'
        )
        
        self.estudante_serializer = EstudanteSerializer(instance=self.estudante)
    
    def teste_verifica_campos_serializados_de_estudante(self):
        """Teste que verifica os campos serializados do modelo Estudante"""
        dados = self.estudante_serializer.data
        self.assertEqual(set(dados.keys()),set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))
        
    def teste_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        """Teste que verifica o conteudo dos campos serializados do modelo Estudante"""
        dados = self.estudante_serializer.data
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf) 
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['celular'], self.estudante.celular)