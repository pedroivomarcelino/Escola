from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    #fixtures = ['prototipo.json'] conecao com os dados de teste criados com os dados do banco de dados
    def setUp(self):
        self.usuario = User.objects.create_superuser('admin',password='admin123',)
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        
        #criando os estudantes
        self.estudante_01 = Estudante.objects.create(
            nome = 'teste estudante UM',
            email = 'testeestudante1@gmail.com',
            cpf = '28472222004',
            data_nascimento = '2000-01-01',
            celular = '99 99999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'teste estudante DOIS',
            email = 'testeestudante2@gmail.com',
            cpf = '28472222010',
            data_nascimento = '2001-01-01',
            celular = '99 99999-9999'
        )
        
    #teste de requisicao GET
    def teste_requisicao_get_para_listar_estudantes(self):
        """Teste de requisicao GET para listar os estudantes"""
        response = self.client.get(self.url)#/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #teste de requisicao GET para um estudante especifico
    def teste_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisicao GET para um estudante especifico"""
        response = self.client.get(self.url+'1/')#/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializado = EstudanteSerializer(instance=dados_estudante)
        self.assertEqual(response.data, dados_estudante_serializado)
    
    #teste de requisicao POST para criar um estudante    
    def teste_requisicao_post_para_criar_um_estudante(self):
        """Teste de requisicao POST para um estudante"""
        dados = {
            'nome': 'teste',
            'email': 'teste@gmail.com',
            'cpf': '73380406058',
            'data_nascimento': '2000-01-01',
            'celular': '99 99999-9999'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    #teste de requisicao DELETE para excluir um estudante
    def teste_requisicao_delete_um_estudante(self):
        """Teste de requisicao DELETE um estudante"""
        response = self.client.delete(f'{self.url}2/')#/estudantes/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    #teste de requisicao PUT para atualizar um estudante
    def teste_requisicao_put_para_atualizar_um_estudante(self):
        """Teste de requisicao PUT para atualizar um estudante"""
        dados = {
            'nome': 'teste',
            'email': 'testeput@gmail.com',
            'cpf': '48277503008',
            'data_nascimento': '2000-01-01',
            'celular': '99 99999-9999'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
        