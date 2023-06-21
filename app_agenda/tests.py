from django.test import TestCase, Client
from django.urls import reverse
from .models import Tarefa

class FormularioTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_salvar = reverse('salvar')
    
    def test_salvar_tarefa_com_prazo(self):
        # Criar uma tarefa válida para enviar no formulário
        tarefa = {
            'tarefa': 'Minha tarefa',
            'prazo': '2023-06-30'
        }
        
        # Enviar a solicitação POST para salvar a tarefa
        response = self.client.post(self.url_salvar, tarefa)
        
        # Verificar se a tarefa foi salva corretamente no banco de dados
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Tarefa.objects.filter(tarefa='Minha tarefa', prazo='2023-06-30').exists())

    def test_salvar_tarefa_sem_prazo(self):
        # Criar uma tarefa inválida sem o campo 'prazo'
        tarefa = {
            'tarefa': 'Minha tarefa sem prazo',
            'prazo': ''
        }
        
        # Enviar a solicitação POST para salvar a tarefa sem o prazo
        response = self.client.post(self.url_salvar, tarefa)
        
        # Verificar se a tarefa não foi salva no banco de dados devido à restrição NOT NULL
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Tarefa.objects.filter(tarefa='Minha tarefa sem prazo').exists())


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_home = reverse('home')
    
    def test_home(self):
        # Criar algumas tarefas de exemplo
        Tarefa.objects.create(tarefa='Tarefa 1', prazo='2023-06-30')
        Tarefa.objects.create(tarefa='Tarefa 2', prazo='2023-07-15')
        
        # Enviar a solicitação GET para a página inicial (home)
        response = self.client.get(self.url_home)
        
        # Verificar se a resposta tem o status code 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verificar se as tarefas são exibidas corretamente na página
        self.assertContains(response, 'Tarefa 1')
        self.assertContains(response, 'Tarefa 2')
    
