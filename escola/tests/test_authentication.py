from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser('admin',password='admin123',)
        self.url = reverse('Estudantes-list') 
        
    #testando as credenciais corretas
    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticacao de um user com credenciais corretas"""
        usuario = authenticate(username='admin', password='admin123')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
        
    #testando as credenciais incorretas
    def test_autenticacao_user_com_credenciais_incorretas(self):
        """Teste que verifica a autenticacao de um user com credenciais incorretas"""
        usuario = authenticate(username='admn', password='admin123')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        
    #testando senha incorretas
    def test_autenticacao_user_com_senha_incorretas(self):
        """Teste que verifica a autenticacao de um user com senha incorretas"""
        usuario = authenticate(username='admin', password='admin13')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        
    def test_requisicao_get_autorizada(self):
        """Teste que verifica uma requisicao GET autorizada"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisicao GET nao autorizada"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)