Trabalho desenvolvido por Ederson Schulze e Ramon Valentim

rodar singeleton: rode o comando no terminal "python singleton.py"

rodar o decorator:

python "app.py". Precisa instalar o flask com "pip install flask.py"


# 1. Singleton

## Problema Resolvido:

Garantir que apenas uma instância da classe de registro de usuários seja criada durante toda a execução do sistema.
Necessidade: Evitar duplicação de dados ou conflitos ao gerenciar um único recurso compartilhado.
Explicação da Implementação:

A classe RegistroUsuarios foi implementada usando o padrão Singleton, garantindo que múltiplas chamadas retornem a mesma instância.
Isso foi realizado com a sobrecarga do método __new__, criando uma única instância acessível globalmente.
Teste Realizado:

Verificou-se que diferentes variáveis referenciam a mesma instância.
Adicionou-se usuários para validar que todos os dados são centralizados.
 

# 2. Decorator
## Problema Resolvido:

Criar um sistema de geração de relatórios modular e flexível, permitindo adicionar funcionalidades como cabeçalhos, rodapés, bordas e cores de texto de forma dinâmica.
Necessidade: Evitar modificações diretas na classe base, permitindo estender o comportamento do sistema sem violar o princípio aberto/fechado (OCP).
Explicação da Implementação:

Uma estrutura de decoradores foi criada com uma classe base DecoradorRelatorio.
Decoradores específicos (DecoradorCabecalho, DecoradorRodape, etc.) adicionam funcionalidades ao relatório base (RelatorioBasico) dinamicamente.
Teste Realizado:

Validou-se a interação entre múltiplos decoradores aplicados em sequência.
O sistema foi testado com diferentes combinações para garantir flexibilidade e modularidade.