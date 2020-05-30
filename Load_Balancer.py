ref_arq_input = "input.txt"  # Nome do arquivo input (entrada)
ref_arq_output = "output.txt"  # Nome do arquivo outpurt (saída)


ttask = int(open(ref_arq_input, 'r').readlines()[0])
umax = int(open(ref_arq_input, 'r').readlines()[1])
servidores = []
usuarios = []
custo_por_tick = 1
custo = 0


def consulta_servidores(linha_atual):
    cont = 0
    while (linha_atual > 0):
        if len(servidores) == 0:
            print("Nenhum servidor encontrado, abrindo um novo")
            servidores.append(1)
            cont += 1
            inclui_usrs()
            linha_atual -= 1
        else:
            if (cont < len(servidores)):
                if servidores[cont] < umax:
                    servidores[cont] += 1
                    inclui_usrs()
                    cont += 1
                    linha_atual -= 1
                else:
                    cont += 1
            else:
                servidores.append(1)
                inclui_usrs()
                linha_atual -= 1


def fecha_servidores():
    print('Reorganizando servidores')
    retira_usuario()
    while 0 in servidores:
        servidores.remove(0)
    print('Lista de servidores reorganizada!:', servidores)
    if len(servidores) > 1:
        otimiza_servidores()
    cria_output()


def cria_output():
    with open(ref_arq_output, 'a') as f:
        for item in servidores:
            f.write("%s," % item)
        f.write("\n")


def ins_custo():
    with open(ref_arq_output, 'a') as f:
        f.write("Custo final em reais = ")
        f.write(str(custo))


def inclui_usrs():
    usuarios.append(ttask+1)


def tempo_ttask():
    cont = 0
    for user in usuarios:
        usuarios[cont] = usuarios[cont]-1
        cont += 1


def retira_usuario():
    cont = 0
    cont2 = 0
    while 0 in usuarios:
        if usuarios[cont] == 0:
            usuarios.remove(0)
            while(servidores[cont2] <= 0):
                cont2 += 1
            servidores[cont2] = servidores[cont2]-1
        else:
            cont -= 1


def otimiza_servidores():
    var = 0
    cont = 0
    cont2 = 1
    servidores_provisorio = []
    for s in servidores:
        servidores_provisorio.append(servidores[cont])
        cont += 1
    cont = 0
    while all(s < umax for s in servidores):
        for p in servidores_provisorio:
            if (s+p) == umax:
                var = s + p
                servidores[cont] = var
                del servidores[cont2]
                del servidores_provisorio[cont2]
                cont2 += 1
        cont += 1


with open(ref_arq_input) as file:
    for line in file.readlines()[2:]:
        linha_atual = int(line)
        consulta_servidores(linha_atual)
        retira_usuario()
        tempo_ttask()
        fecha_servidores()
        custo = custo + len(servidores)*custo_por_tick


while(len(usuarios) != 0):
    retira_usuario()
    fecha_servidores()
    tempo_ttask()
    custo = custo + len(servidores)*custo_por_tick


print("Custo final =", custo)
ins_custo()
