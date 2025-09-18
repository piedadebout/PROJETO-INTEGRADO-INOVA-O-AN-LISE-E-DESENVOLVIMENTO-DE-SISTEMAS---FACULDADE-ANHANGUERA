import re

# ===================== DADOS =====================
pacientes = []
horarios_disponiveis = [
    "20/09 às 14h", "20/09 às 15h",
    "21/09 às 10h", "21/09 às 11h",
    "22/09 às 14h", "22/09 às 15h"
]

fila_atendimento = []
SENHA_ADMIN = "admin123"

# ===================== MENU =====================
def menu():
    print('\n=== SISTEMA CLÍNICA MAIS SAÚDE ===')
    print('1. Cadastrar Paciente')
    print('2. Ver estatísticas')
    print('3. Buscar Paciente')
    print('4. Listar todos os Pacientes')
    print('5. Agendar consulta')
    print('6. Confirmar consulta (controle de acesso)')
    print('7. Cancelar consulta')
    print('8. Consultar horários')
    print('9. Adicionar novos horários (Admin)')
    print('10. Organizar fila de atendimento')
    print('11. Sair')
    opcao = input('Escolha uma opção: ')
    if opcao not in [str(i) for i in range(1, 12)]:
        print('Opção inválida! Tente novamente.')
        return None
    return opcao

# ===================== AUXILIARES =====================
def pausar():
    input("\nPressione Enter para continuar...")

def horarios_disponiveis_ativos():
    ocupados = [p["horario"] for p in pacientes if p["horario"]]
    return [h for h in horarios_disponiveis if h not in ocupados]

# ===================== PACIENTES =====================
def cadastrar_paciente():
    print("\n=== CADASTRAR PACIENTE ===")
    nome = input("Nome: ")
    while True:
        idade = input("Idade: ")
        if idade.isdigit() and int(idade) > 0:
            idade = int(idade)
            break
        print("Idade inválida! Digite apenas números maiores que 0.")
    while True:
        telefone = input("Telefone (apenas números): ")
        if telefone.isdigit():
            break
        print("Telefone inválido! Digite apenas números.")
    documentos_ok = input("Documentos em dia? (s/n): ").lower() == "s"
    pagamentos_ok = input("Pagamentos em dia? (s/n): ").lower() == "s"

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "horario": None,
        "documentos_ok": documentos_ok,
        "pagamentos_ok": pagamentos_ok
    }
    pacientes.append(paciente)
    print(f"\nPaciente {nome} cadastrado com sucesso!")

    # Mostrar horários disponíveis para agendamento
    disponiveis = horarios_disponiveis_ativos()
    if disponiveis:
        print("\nHorários disponíveis para agendamento:")
        for i, h in enumerate(disponiveis, start=1):
            print(f"{i}. {h}")
    else:
        print("\nNão há horários disponíveis no momento.")
    pausar()

def listar_pacientes():
    print("\n=== LISTA DE PACIENTES ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    for i, p in enumerate(pacientes, start=1):
        horario = p["horario"] if p["horario"] else "Sem horário agendado"
        documentos = "OK" if p["documentos_ok"] else "Pendentes"
        pagamentos = "OK" if p["pagamentos_ok"] else "Pendentes"
        print(f"{i}. {p['nome']} - {p['idade']} anos - Tel: {p['telefone']} - {horario} - Documentos: {documentos} - Pagamentos: {pagamentos}")
    pausar()

def buscar_paciente():
    print("\n=== BUSCAR PACIENTE ===")
    nome_busca = input("Digite o nome do paciente: ")
    encontrados = [p for p in pacientes if p["nome"].lower() == nome_busca.lower()]
    if not encontrados:
        print("Paciente não encontrado.")
    for p in encontrados:
        horario = p["horario"] if p["horario"] else "Sem horário agendado"
        documentos = "OK" if p["documentos_ok"] else "Pendentes"
        pagamentos = "OK" if p["pagamentos_ok"] else "Pendentes"
        print(f"Nome: {p['nome']} - Idade: {p['idade']} - Tel: {p['telefone']} - {horario} - Documentos: {documentos} - Pagamentos: {pagamentos}")
    pausar()

# ===================== HORÁRIOS =====================
def adicionar_horarios():
    print("\n=== ADICIONAR NOVOS HORÁRIOS (Admin) ===")
    senha = input("Digite a senha de admin: ")
    if senha != SENHA_ADMIN:
        print("Senha incorreta! Acesso negado.")
        pausar()
        return
    novo = input("Digite o novo horário (DD/MM às HHh): ")
    if not re.match(r'^\d{2}/\d{2} às \d{1,2}h$', novo):
        print("Formato inválido! Use DD/MM às HHh.")
    elif novo in horarios_disponiveis:
        print("Horário já existe.")
    else:
        horarios_disponiveis.append(novo)
        print("Horário adicionado com sucesso!")
    pausar()

def consultar_horarios():
    print("\n=== CONSULTAR HORÁRIOS ===")
    disponiveis = horarios_disponiveis_ativos()
    if not disponiveis:
        print("Não há horários disponíveis.")
    else:
        for i, h in enumerate(disponiveis, start=1):
            print(f"{i}. {h}")
    pausar()

def agendar_consulta():
    print("\n=== AGENDAR CONSULTA ===")
    nome = input("Digite o nome do paciente: ")
    paciente = next((p for p in pacientes if p["nome"].lower() == nome.lower()), None)
    if not paciente:
        print("Paciente não cadastrado.")
        pausar()
        return
    if paciente["horario"]:
        print(f"O paciente já possui horário: {paciente['horario']}")
        pausar()
        return

    disponiveis = horarios_disponiveis_ativos()
    if not disponiveis:
        print("Não há horários disponíveis.")
        pausar()
        return
    if len(disponiveis) == 1:
        paciente["horario"] = disponiveis[0]
        print(f"Consulta agendada automaticamente: {disponiveis[0]}")
    else:
        print("Horários disponíveis:")
        for i, h in enumerate(disponiveis, start=1):
            print(f"{i}. {h}")
        escolha = input("Escolha o número do horário: ")
        if not escolha.isdigit() or int(escolha) not in range(1, len(disponiveis)+1):
            print("Opção inválida.")
            pausar()
            return
        paciente["horario"] = disponiveis[int(escolha)-1]
        print(f"Consulta agendada: {paciente['horario']}")
    pausar()

def cancelar_consulta():
    print("\n=== CANCELAR CONSULTA ===")
    nome = input("Digite o nome do paciente: ")
    paciente = next((p for p in pacientes if p["nome"].lower() == nome.lower()), None)
    if not paciente or not paciente["horario"]:
        print("Paciente não possui consulta agendada.")
    else:
        confirmar = input(f"Confirma cancelamento do horário {paciente['horario']}? (s/n): ")
        if confirmar.lower() == "s":
            paciente["horario"] = None
            print("Consulta cancelada.")
    pausar()

# ===================== CONTROLE DE ACESSO =====================
def controle_acesso():
    print("\n=== CONTROLE DE ACESSO ===")
    nome = input("Digite o nome do paciente: ")
    paciente = next((p for p in pacientes if p["nome"].lower() == nome.lower()), None)
    if not paciente:
        print("Paciente não cadastrado.")
        pausar()
        return
    medico_disponivel = input("Médico disponível? (s/n): ").lower() == "s"
    tipo = input("Tipo de atendimento (normal/emergencia): ").lower()
    motivos = []

    if paciente["horario"] is None:
        motivos.append("Sem horário agendado")
    if not paciente["documentos_ok"]:
        motivos.append("Documentos pendentes")
    if not paciente["pagamentos_ok"]:
        motivos.append("Pagamentos pendentes")
    if not medico_disponivel:
        motivos.append("Médico indisponível")

    atendimento = False
    if tipo == "normal":
        atendimento = (paciente["horario"] and paciente["documentos_ok"] and medico_disponivel) or (paciente["documentos_ok"] and medico_disponivel and paciente["pagamentos_ok"])
    elif tipo == "emergencia":
        atendimento = medico_disponivel and (paciente["documentos_ok"] or paciente["pagamentos_ok"])

    if atendimento:
        print("Paciente liberado para atendimento.")
        while True:
            cpf = input("Digite CPF (apenas números): ")
            if cpf.isdigit():
                fila_atendimento.append({"nome": paciente["nome"], "cpf": cpf})
                break
            print("CPF inválido! Digite apenas números.")
    else:
        print("Paciente NÃO pode ser atendido pelos seguintes motivos:")
        for m in motivos:
            print(f"- {m}")
    pausar()

# ===================== FILA DE ATENDIMENTO =====================
def organizar_fila():
    print("\n=== FILA DE ATENDIMENTO ===")
    if not fila_atendimento:
        print("Fila vazia.")
    else:
        paciente_atendido = fila_atendimento.pop(0)
        print(f"{paciente_atendido['nome']} atendido.")
        if fila_atendimento:
            print("Pacientes restantes na fila:")
            for p in fila_atendimento:
                print(f"{p['nome']} - CPF: {p['cpf']}")
        else:
            print("Nenhum paciente na fila.")
    pausar()

# ===================== ESTATÍSTICAS =====================
def estatisticas():
    print("\n=== ESTATÍSTICAS ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        total = len(pacientes)
        media = sum(p["idade"] for p in pacientes)/total
        mais_novo = min(pacientes, key=lambda p: p["idade"])
        mais_velho = max(pacientes, key=lambda p: p["idade"])
        print(f"Número total de pacientes: {total}")
        print(f"Idade média: {media:.1f}")
        print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
        print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
    pausar()

# ===================== PROGRAMA PRINCIPAL =====================
while True:
    opcao = menu()
    if opcao == '1':
        cadastrar_paciente()
    elif opcao == '2':
        estatisticas()
    elif opcao == '3':
        buscar_paciente()
    elif opcao == '4':
        listar_pacientes()
    elif opcao == '5':
        agendar_consulta()
    elif opcao == '6':
        controle_acesso()
    elif opcao == '7':
        cancelar_consulta()
    elif opcao == '8':
        consultar_horarios()
    elif opcao == '9':
        adicionar_horarios()
    elif opcao == '10':
        organizar_fila()
    elif opcao == '11':
        print("Saindo do sistema... Até logo!")
        break
