# Aplicações
Acesse: https://todolist.cloudboosterlab.org/
# Authentication
A app Authentication é responsável pela administração do usuário, incluindo:

# Criação de usuários: Registro de novos usuários.
# Login de usuários: Autenticação de usuários existentes.


# Arquivos Importantes
forms.py: Contém os formulários para registro e login de usuário.
views.py: Realiza a comunicação entre os modelos e os templates.

Tarefa
A app Tarefa gerencia toda a lógica de negócios relacionada ao gerenciamento de tarefas. Segue os mesmos princípios da app Authentication, mas:

Não possui um forms.py, pois utiliza HTMX para dinamizar a aplicação.
Não utiliza Class-Based Views (CBV), optando por uma abordagem mais simples.

# Configuração do Docker
Dockerfile e docker-compose.yml
O Dockerfile e o docker-compose.yml foram adaptados para subir em uma nuvem própria que já possui uma rede configurada. Caso você não tenha uma rede, será necessário:

Adaptar o docker-compose.yml para criar uma nova rede.
O projeto já inclui um serviço Postgres, mas normalmente, você deve ter um contêiner Postgres rodando na mesma rede e lembre-se das envs.

# Para instalar as Dependencias
pip install -r requirements.txt
para subit o container após vc adptar o docker-compose.yml
docker-compose up
