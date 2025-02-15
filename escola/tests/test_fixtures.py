from django.test import TestCase
from escola.models import Estudante, Curso


class FixturesTestCase(TestCase):
    fixtures = ['prototipo.json']
    
    
    def teste_carregamento_fixtures(self):
        """Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf='12345678939')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '21 987651234')
        self.assertEqual(curso.descricao, '1')