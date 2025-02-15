from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Teste falhou')
    
    #criando um novo estudante para o teste
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testemodelo@gmail.com',
            cpf = '66066550055',
            data_nascimento = '1987-06-01',
            celular = '21 99999-9999'
        )
    
    def test_verifica_atributos_de_estudantes(self):
        """Teste que verifica os atributos do modelo Estudante"""
        #validando os dados passados pelos atributos no setUp
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '66066550055')
        self.assertEqual(self.estudante.data_nascimento, '1987-06-01')
        self.assertEqual(self.estudante.celular, '21 99999-9999')

class ModelCursoTestCase(TestCase):
    
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CTM',
            descricao = 'Curso Teste Modelo',
            nivel = 'B',
        )
    
    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, 'CTM')
        self.assertEqual(self.curso.descricao, 'Curso Teste Modelo')
        self.assertEqual(self.curso.nivel, 'B')
        
class ModelMatriculaTestCase(TestCase):
    
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')