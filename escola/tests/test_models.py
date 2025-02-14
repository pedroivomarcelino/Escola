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

# class ModelCursoTestCase(TestCase):
    
#     def setUp(self):
#         self.curso = Curso.objects.create(
#             codigo = '0001',
#             descricao = 'Curso de Teste',
#             nivel = 'B'
#         )
        
#     def test_verifica_atributos_de_cursos(self):
#         """Teste que verifica os atributos do modelo Curso"""
#         self.assertEqual(self.curso.codigo, '0001')
#         self.assertEqual(self.curso.descricao, 'Curso de Teste')
#         self.assertEqual(self.curso.nivel, 'B')
        
# class ModelMatriculaTestCase(TestCase):
    
#     def setUp(self):
#         self.estudante = Estudante.objects.create(
#             nome = 'Teste de Modelo',
#             email = 'testemodelo@gmail.com',
#             periodo = 'M'
#         )
        
#     def test_verifica_atributos_de_matriculas(self):
#         """Teste que verifica os atributos do modelo Matricula"""
#         self.assertEqual(self.estudante.nome, 'Teste de Modelo')
#         self.assertEqual(self.estudante.email, 'testemodelo@gmail.com')