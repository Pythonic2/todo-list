from django.test import TestCase
from django.contrib.auth import get_user_model
from tarefa.models import Tarefa



class TarefaModelTest(TestCase):



    def setUp(self):
        CustomUser = get_user_model()
        self.usuario = CustomUser.objects.create_user(
            username='usuario_teste',
            email='email@teste.com',
            nome='xpto',
            password='senha123!@#'
        )

        self.tarefa = Tarefa.objects.create(
            titulo='Tarefa Teste',
            descricao = 'descricao teste',
            usuario=self.usuario
        )


    def test_criacao_tarefa(self):
        self.assertEqual(self.tarefa.titulo, 'Tarefa Teste')
        self.assertEqual(self.tarefa.descricao, 'descricao teste')
        self.assertEqual(self.tarefa.usuario.username, 'usuario_teste')


    def test_edicao_tarefa(self):
        self.tarefa.titulo = 'Tarefa editada'
        self.tarefa.save()
        tarefa_editada = Tarefa.objects.get(id=self.tarefa.id)
        self.assertEqual(tarefa_editada.titulo, 'Tarefa editada')

    def test_deletar_tarefa(self):
        tarefa_id = self.tarefa.id
        self.tarefa.delete()

        with self.assertRaises(Tarefa.DoesNotExist):
            Tarefa.objects.get(id=tarefa_id)