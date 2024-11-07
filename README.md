# Aplicações
Acesse: https://todolist.cloudboosterlab.org/
# Authentication
A app Authentication é responsável pela administração do usuário, incluindo:

# Criação de usuários: Registro de novos usuários.
# Login de usuários: Autenticação de usuários existentes.


# Arquivos Importantes
forms.py: Contém os formulários para registro e login de usuário.
views.py: Realiza a comunicação entre os modelos e os templates.

# Tarefa
A app Tarefa gerencia toda a lógica de negócios relacionada ao gerenciamento de tarefas. Segue os mesmos princípios da app Authentication, mas:

Não possui um forms.py, pois utiliza HTMX para dinamizar a aplicação.
Não utiliza Class-Based Views (CBV), optando por uma abordagem mais simples.

# Configuração do Docker
(removendo network)
você precisa apenas criar um .env na raiz do projeto com os segiuntes itens: 
DB_NAME=nome_banco;
DB_USER=nome_user;
DB_PASSWORD=senha;
DB_PORT=5432;
DB_HOST=postgres;

# PARA RODAR LOCAL:
docker-compose up
