Este projeto foi desenvolvido a pedido da instituição Anhanguera, como parte da graduação em Tecnólogo em Análise e Desenvolvimento de Sistemas que estou realizando.

A proposta do sistema era criar uma solução para atendimento na área da saúde, permitindo gerenciar pacientes, consultas, horários e filas de atendimento de forma prática e intuitiva.

O desenvolvimento do projeto foi baseado nos conhecimentos adquiridos tanto na instituição quanto em cursos complementares, como Curso do Guanabara e Udemy.

Reconheço que ainda há muitas melhorias possíveis, especialmente em termos de funcionalidades, interface e organização do código. No entanto, devido a limitações de tempo e dedicação, optei por disponibilizar esta versão como pública, para que qualquer pessoa interessada possa visualizar, estudar ou utilizar o sistema.


🏥 Sistema de Gestão de Clínica – Clínica Mais Saúde
Sistema em Python para gerenciamento completo de pacientes, consultas e controle de atendimento em uma clínica.
Permite cadastrar pacientes, agendar consultas, controlar fila e administrar horários de forma prática e intuitiva.

🎯 Funcionalidades
Cadastro de pacientes com validação de idade, telefone, documentos e pagamentos.

Agendamento de consultas com horários disponíveis exibidos automaticamente.

Controle de acesso para liberar pacientes de acordo com documentos, pagamentos e disponibilidade do médico.

Fila de atendimento para organizar e acompanhar pacientes atendidos.

Administração de horários com senha de administrador.

Estatísticas sobre pacientes cadastrados (idade média, paciente mais novo/velho).

📋 Menu do Sistema

=== SISTEMA CLÍNICA MAIS SAÚDE ===
1. Cadastrar Paciente
2. Ver estatísticas
3. Buscar Paciente
4. Listar todos os Pacientes
5. Agendar consulta
6. Confirmar consulta (controle de acesso)
7. Cancelar consulta
8. Consultar horários
9. Adicionar novos horários (Admin)
10. Organizar fila de atendimento
11. Sair

🖥️ Exemplo de Uso

Cadastro de Paciente
=== CADASTRAR PACIENTE ===
Nome: João Silva
Idade: 30
Telefone (apenas números): 11999999999
Documentos em dia? (s/n): s
Pagamentos em dia? (s/n): s

Paciente João Silva cadastrado com sucesso!

Horários disponíveis para agendamento:
1. 20/09 às 14h
2. 20/09 às 15h
3. 21/09 às 10h
...

Agendamento de Consulta
=== AGENDAR CONSULTA ===
Digite o nome do paciente: João Silva
Horários disponíveis:
1. 20/09 às 14h
2. 20/09 às 15h
Escolha o número do horário: 1

Consulta agendada: 20/09 às 14h

Controle de Acesso
=== CONTROLE DE ACESSO ===
Digite o nome do paciente: João Silva
Médico disponível? (s/n): s
Tipo de atendimento (normal/emergencia): normal

Paciente liberado para atendimento.
Digite CPF (apenas números): 12345678900

Se o paciente não puder ser atendido:
Paciente NÃO pode ser atendido pelos seguintes motivos:
- Sem horário agendado
- Documentos pendentes

Fila de Atendimento
=== FILA DE ATENDIMENTO ===
João Silva atendido.
Pacientes restantes na fila:
Maria Oliveira - CPF: 98765432100


💻 Tecnologias Utilizadas

Python 3

Biblioteca padrão: re para validação de entradas (horário, CPF, etc.)

🚀 Como Rodar o Sistema

Clone o repositório:
1.Clone o repositório:
git clone https://github.com/seuusuario/clinica-mais-saude.git
2.Acesse a pasta:
cd clinica-mais-saude
3.Execute o programa:
python clinica.py

Substitua clinica.py pelo nome do arquivo do seu sistema.

🔑 Senha de Administrador

Para adicionar novos horários: admin123

clinica-mais-saude/
│
├─ clinica.py           # Código principal do sistema
├─ README.md            # Documentação
└─ imagens/             # Capturas de tela ou GIFs

Total de pacientes cadastrados

Idade média

Paciente mais novo

Paciente mais velho

📂 Estrutura do Projeto

clinica-mais-saude/
│
├─ clinica.py           # Código principal do sistema
├─ README.md            # Documentação
└─ imagens/             # Capturas de tela ou GIFs
