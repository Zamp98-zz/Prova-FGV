#REGIÃO ONDE FOI REALIZADA A ENTREVISTA;IDADE: QUAL A SUA IDADE (EM ANOS COMPLETOS)?;ÁREA;SEXO;COR OU RAÇA;ÚLTIMA SÉRIE ESCOLAR QUE CONCLUIU COM APROVAÇÃO;ATÉ QUE SÉRIE O SEU PAI ESTUDOU;ATÉ QUE SÉRIE A SUA MÃE ESTUDOU;RENDA TOTAL DO CHEFE DA FAMÍLIA NO ÚLTIMO MÊS;RENDA TOTAL DE TODOS OS MORADORES (PARENTES E AGREGADOS) NO ÚLTIMO MÊS;NÚMERO DE MORADORES NO DOMICÍLIO (PARENTES E AGREGADOS);NO ÚLTIMO MÊS, ALGUMA PESSOA DESTE DOMICÍLIO RECEBEU RENDIMENTOS DO BOLSA FAMÍLI;RELIGIÃO;MULHERES QUE USAM ROUPAS QUE MOSTRAM O CORPO MERECEM SER ATACADAS;AS MULATAS SÃO MAIS FOGOSAS DO QUE AS MULHERES BRANCAS;DÁ PARA ENTENDER QUE UM HOMEM QUE CRESCEU EM UMA FAMÍLIA VIOLENTA AGRIDA SUA MUL;OS HOMENS DEVEM SER A CABEÇA DO LAR;CASOS DE VIOLÊNCIA DENTRO DE CASA DEVEM SER DISCUTIDOS SOMENTE ENTRE OS MEMBROS ;INCOMODA VER DOIS HOMENS, OU DUAS MULHERES, SE BEIJANDO NA BOCA EM PÚBLICO;SE AS MULHERES SOUBESSEM COMO SE COMPORTAR, HAVERIA MENOS ESTUPROS;HOMEM QUE BATE NA ESPOSA TEM QUE IR PARA A CADEIA;É VIOLÊNCIA FALAR MENTIRAS SOBRE UMA MULHER PARA OS OUTROS;TODA MULHER SONHA EM SE CASAR;O QUE ACONTECE COM O CASAL EM CASA NÃO INTERESSA AOS OUTROS;QUANDO HÁ VIOLÊNCIA, OS CASAIS DEVEM SE SEPARAR;CASAIS DE PESSOAS DO MESMO SEXO DEVEM TER OS MESMOS DIREITOS DOS OUTROS CASAIS;DÁ PRA ENTENDER QUE UM HOMEM RASGUE OU QUEBRE AS COISAS DA MULHER SE FICOU NERVO;UM HOMEM PODE XINGAR E GRITAR COM SUA PRÓPRIA MULHER;É DA NATUREZA DO HOMEM SER VIOLENTO;EM BRIGA DE MARIDO E MULHER, NÃO SE METE A COLHER;A ROUPA SUJA DEVE SER LAVADA EM CASA;UMA MULHER SÓ SE SENTE REALIZADA QUANDO TEM FILHOS/AS;A MULHER CASADA DEVE SATISFAZER O MARIDO NA CAMA, MESMO QUANDO NÃO TEM VONTADE;PIADA DE PRETO É SÓ BRINCADEIRA, NÃO É RACISMO;UM CASAL DE DOIS HOMENS VIVE UM AMOR TÃO BONITO QUANTO ENTRE UM HOMEM E UMA MULH;MULHER QUE É AGREDIDA E CONTINUA COM O PARCEIRO GOSTA DE APANHAR;CASAMENTO DE HOMEM COM HOMEM OU DE MULHER COM MULHER DEVE SER PROIBIDO;A MULHER QUE APANHA EM CASA DEVE FICAR QUIETA PARA NÃO PREJUDICAR OS FILHOS;A QUESTÃO DA VIOLÊNCIA CONTRA AS MULHERES RECEBE MAIS IMPORTÂNCIA DO QUE MERECE;TEM MULHER QUE É PRA CASAR, TEM MULHER QUE É PRA CAMA
#c) A base é composta por quantas linhas e colunas?
#d) Calcule a frequência de pessoas em cada região do Brasil.
#e) Qual é a região mais frequente (moda)?
#f) Qual é a idade da pessoa mais nova nessa amostra? E da mais velha?
#g) Calcule a média, a mediana e a moda para a variável idade. A partir disso, o que você pode dizer sobre a distribuição dessa variável (assimétrica positiva, assimétrica negativa ou simétrica)?
import math


def getMaior(dados):
    x = int(dados[1])
    for i in range(2, len(dados)):
        if x < int(dados[i]):
            x = int(dados[i])
    return x

def getMenor(dados):
    x = int(dados[1])
    for i in range(2, len(dados)):
        if x > int(dados[i]):
            x = int(dados[i])
    return x
def linhaColunaBase(conteudo):
    coluna = len(conteudo[0])
    linha = len(conteudo) - 1 #desconsiderando o indice da tabela
    return [linha, coluna]

def frequenciaDados(conteudo):
    resultado = []
    referencia = getDistinct(conteudo)
    for j in range(len(referencia)):
        count = 0
        for i in range(len(conteudo)):
            if conteudo[i] == referencia[j]:
                count+=1
        resultado.append([referencia[j], count])
    return resultado

def simetria(moda, media):
    x = media - moda
    if(x > 0):
        return "Assimétrica positiva"
    elif(x < 0):
        return "Assimétrica negativa"
    else:
        return "Simétrica"

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    temp = arquivo.readlines()
    arquivo.close()
    conteudo = []
    for linha in temp:
        conteudo.append(linha.split(";"))
    return conteudo

def adicionaFaixaEtaria(nomeArquivo):
    conteudo = lerArquivo(nomeArquivo)
    colunaIdade = buscaColuna(conteudo[0], "idade")
    resultado = []
    cIdade = int(colunaIdade[0])

    if "Faixa etária:" in conteudo[0]:#caso essa operação já tenha sido feita
        return conteudo
    for i in range(len(conteudo)):
        linha = conteudo[i]
        if(i == 0):
            linha.insert(cIdade + 1,"Faixa etária:")
        else:
            idade = int(conteudo[i][colunaIdade[0]])

            if(idade <= 29):
                linha.insert(cIdade + 1,"Jovens")
            elif(30<= idade <= 59):
                linha.insert(cIdade + 1,"Adultos")
            else:
                linha.insert(cIdade + 1,"Idosos")
        resultado.append(linha)
    return resultado


#função que retorna os valores distintos de uma coluna
def getDistinct(conteudo):
    temp = []
    for linha in conteudo:
        if not linha in temp:
            try:
                x = int(linha)
                temp.append(x)
            except:
                temp.append(linha)
    return temp

def getModa(dados):
    ref = getDistinct(dados)
    quantidade  = 0
    resultado = []
    #print("dados", dados)
    temp = frequenciaDados(dados)
    for linha in temp:
        if(linha[1] >= quantidade):
            quantidade = linha[1]
    for linha in temp:
        if(linha[1] == quantidade):
            resultado.append(linha)
    return resultado

def buscaColuna(indice, valor):
    coluna = []
    if(len(indice) > 0):
        for i in range(len(indice)):
            if valor in indice[i]:
                coluna.append(i)
        return coluna

def getMedia(dados, consideraNulo):
    soma = 0
    divisor = len(dados) - 1
    #temp.pop(0)
    for i in range(1, len(dados), 1):
        if(dados[i]):
            soma += int(dados[i])
        else:#se o dado for nulo, diminui o divisor
            if(consideraNulo == False):
                divisor -= 1
    media = soma/divisor
    return media
    
def getMediana(dados):
    temp = dados.copy()
    #temp.pop(0)
    vetOrdenado = sorted(temp)
    vMeio = []
    qAmostras = len(vetOrdenado)
    meio = qAmostras // 2
    res = 0
    if(qAmostras % 2 == 0):#se o numero de amostras for par [1,2,3,4,5]
        vMeio.append([int(vetOrdenado[meio-1]), int(vetOrdenado[meio])])
        res = ((vMeio[0][0]) + (vMeio[0][1]))/2
    else:
        vMeio.append(int(vetOrdenado[meio]))
        res = vMeio[0]
    #print("res",res)
    return res

def getMatrizColuna(dados, coluna):
    #print("teste:", dados[0])
    temp = dados
    col = []
    #temp.pop(0) #tirando o índice
    if(len(dados) > 0):
        for linha in temp:
            x = 0
            try:
                x = int(linha[coluna])
                col.append(x)
            except:
                if(linha[coluna] != ''):
                    col.append(linha[coluna])
        return col

def escreveArquivo(conteudo, nomeArquivo):
    arquivo = open(nomeArquivo, "w")
    for j in range(len(conteudo)):
        saida = ""
        for i in range(len(conteudo[j])):
            saida += conteudo[j][i]
            if(i < len(conteudo[j]) - 1):
                saida  += ";"
        arquivo.writelines(saida)
    arquivo.close()
    return True

def quartil(dado, tipo):
    dados = dado.copy()
    mediana = getMediana(dados)
    if(tipo ==  1):
        amostra = []
        for i in range(len(dados)):
            x = int(dados[i])
            if x <= mediana:
                amostra.append(x)
        q1 = getMediana(amostra)
        return q1
    elif(tipo == 2):
        return mediana
    elif(tipo ==  3):
        amostra = []
        for i in range(len(dados)):
            x = int(dados[i])
            if x >= mediana:
                amostra.append(x)
        q3 = getMediana(amostra)
        return q3

def deltaV(dados):
    dp = desvioPadrao(dados, False)
    media = getMedia(dados, False)
    cv = dp/media
    cv = cv * 100
    return cv

def desvioPadrao(dados, consideraNulo):
    temp = dados
    media = getMedia(dados, consideraNulo)
    temp = []
    somatorio = 0
    divisor = len(dados)
    for i in range(1, len(dados), 1):
        if(dados[i]):
            x = float(dados[i]) - media
            x = x**2
            somatorio += x
        else:
            if(consideraNulo == False):
                divisor -= 1
    somatorio = somatorio/divisor
    somatorio = math.sqrt(somatorio)
    return somatorio

def getMatrizRegiao(dados, regiao):
    matriz = []
    for linha in dados:
        if regiao in linha:
            matriz.append(linha)
    return matriz

def desvioRendaPorRegiao(dados, reg):#recebe matriz de dados e um vetor de regiões
    resultado = []
    v = dados.copy()
    v.pop(0)
    for regiao in reg:
        temp = []
        for linha in v:
            if regiao in linha:
                temp.append(linha)
        r = buscaColuna(dados[0], "renda total de todos os moradores")
        if(len(temp) > 0):
            aux = getMatrizColuna(temp, r[0])
            resultado.append([regiao, desvioPadrao(aux, False)])
    return resultado
def main():
    respostas = open("respostas.txt", "w")
    nomeArquivo = "base_ipea.csv"
    conteudo = lerArquivo(nomeArquivo)
    # c) A base é composta por quantas linhas e colunas?
    linhaColuna = linhaColunaBase(conteudo)
    respostas.writelines(["Questão C:\n", "Linhas: ",str(linhaColuna[0]), " Colunas: ", str(linhaColuna[1]),"\n"])

    print("Questão C:")
    print("Linhas: ",linhaColuna[0], "Colunas: ", linhaColuna[1])
    # d) Calcule a frequência de pessoas em cada região do Brasil.
    colunaRegiao = getMatrizColuna(conteudo, 0)

    print("Questão D:")
    respostas.writelines(["\nQuestão D:\n"])
    freqReg = frequenciaDados(colunaRegiao)
    freqReg.pop(0)
    for linha in freqReg:
        print("Região:",linha[0]+",","frequência:",linha[1])
        respostas.writelines(["Região: ",str(linha[0])+","," frequência: ",str(linha[1]),"\n"])
    print("Questão E:")
    respostas.write("\nQuestão E:\n")
    maiorFrequencia = getModa(colunaRegiao)
    print("Região mais frequente: ",maiorFrequencia[0][0]+",", "Frequência:", maiorFrequencia[0][1])
    respostas.write("Região mais frequente: " + str(maiorFrequencia[0][0])+"," + "Frequência: " + str(maiorFrequencia[0][1])+"\n")
    # f) Qual é a idade da pessoa mais nova nessa amostra? E da mais velha?


    print("Questão F:")
    valor = "idade"
    #print("conteudo",conteudo[0])
    res = buscaColuna(conteudo[0], valor)
    reg = buscaColuna(conteudo[0], "região")
    #print("coluna(s) correspondente(s) à busca:", "região", reg)

    colunaIdade = getMatrizColuna(conteudo, res[0])
    #print("coluna(s) correspondente(s) à busca:", valor, res)
    maisNova = getMenor(colunaIdade)
    print("Idade da pessoa mais nova:", maisNova)
    maisVelha = getMaior(colunaIdade)
    print("Idade da pessoa mais velha:", maisVelha)
    respostas.writelines(["\nQuestão F:\n", "Idade da pessoa mais nova: ", str(maisNova), " Idade da pessoa mais velha: ", str(maisVelha),"\n"])


    print("Questão G:")
    mediaIdade = getMedia(colunaIdade, 0)
    ci = getMatrizColuna(conteudo, res[0])
    ci.pop(0)
    #print(ci)
    print("Media de idade: ", mediaIdade)
    modaIdade = getModa(colunaIdade)
    print("Moda da idade: ", str(modaIdade[0][0])+",", "Frequência:", str(modaIdade[0][1]))
    ci = colunaIdade.copy()
    ci.pop(0)
    medianaIdade = getMediana(ci)
    print("Mediana da idade:", medianaIdade)
    x = int(modaIdade[0][0])
    s = simetria(x, mediaIdade)
    print(s)

    respostas.writelines(["\nQuestão G:\n","Média de idade: ", str(mediaIdade),"\nModa da idade: ",str(modaIdade[0][0]), " Frequência: ", str(modaIdade[0][1]),"\nMediana da idade: ", str(medianaIdade),"\n"])
    respostas.write(s)

    print("Questão H:")
    conteudo = adicionaFaixaEtaria(nomeArquivo)
    colunaFaixaEtaria = buscaColuna(conteudo[0], "Faixa etária")
    #print("Faixa etária:", colunaFaixaEtaria)
    modaFaixa = getModa(getMatrizColuna(conteudo, colunaFaixaEtaria[0]))
    print("Faixa etária mais frequente: ", modaFaixa[0][0]+',',"Frequência: ", modaFaixa[0][1])
    arqSaida = "base_ipea.csv"


    if(escreveArquivo(conteudo, arqSaida)):
       print("A tabela foi modificada e salva como:", arqSaida)


    respostas.writelines(["\nQuestão H:\n","Faixa etária mais frequente: ", str(modaFaixa[0][0])+','," Frequência: ", str(modaFaixa[0][1]),"\n"])
    '''i) Calcule a média, a mediana, o primeiro quartil, o terceiro quartil e os valores máximo e mínimo 
    para a variável “renda total de todos os moradores, parentes e agregados no último mês”. Comente os resultados. '''
    print("Questão I:")


    respostas.write("\nQuestão I:\n")
    renda = buscaColuna(conteudo[0], "renda total de todos os moradores")
    colunaRenda = getMatrizColuna(conteudo, renda[0])
    #desvio = desvioPadrao(colunaRenda, False)
    mediaRenda = getMedia(colunaRenda, False)
    cr = colunaRenda.copy()
    cr.pop(0)
    medianaRenda = getMediana(cr)


    print("Média de renda:",mediaRenda)
    print("Mediana renda:", medianaRenda)


    respostas.write("Média de renda: " + str(mediaRenda) + "\n")
    respostas.write("Mediana renda: " + str(medianaRenda) + "\n")

    maxRenda = getMaior(colunaRenda)
    minRenda = getMenor(colunaRenda)


    print("Maior renda:", str(maxRenda)+",","menor renda:", minRenda)
    respostas.write("Maior renda: "+ str(maxRenda)+", "+"menor renda: " + str(minRenda)+"\n")


    q1 = quartil(cr, 1)
    q2 = quartil(cr, 2)
    q3 = quartil(cr, 3)


    print("Primeiro quartil:", q1,"segundo quartil:", q2,"terceiro quartil", q3, "\n")
    respostas.write("Primeiro quartil: " + str(q1) + " segundo quartil: " + str(q2) + " terceiro quartil: "+ str(q3) +"\n")


    print(" A média de renda está bem próxima do valor mediano e muito distante dos valores máximos "
          "e mínimos da amostras.\n O valor do primeiro quartil, "
          "segundo e  do terceiro indicam uma variação maior na segunda parte da amostra.\n")
    respostas.write(" A média de renda está bem próxima do valor mediano e muito distante dos valores máximos "
          "e mínimos da amostras.\n O valor do primeiro quartil, "
          "segundo e  do terceiro indicam uma variação maior na segunda parte da amostra.\n")


    print("Questão J:\n")
    print("O primeiro quartil indica que o valor mediano dos primeiros "
          "25% da amostra é de "+str(q1)+" reais. "
            "Enquanto no terceiro quartil,\n que indica o valor mediano da "
            "parte dos 75% das amostras é de " + str(q3)+" reais" + ". A distância interquartil\n desses"
        " dois indica uma variação considerável da renda do primeiro quarto e o terceiro.")
    respostas.write("\nQuestão J:\n")
    respostas.write("O primeiro quartil indica que o valor mediano dos primeiros "
          "25% da amostra é de "+str(q1)+" reais. "
            "Enquanto no terceiro quartil,\n que indica o valor mediano da "
            "parte dos 75% das amostras é de" + str(q3)+" reais" + ". A distância interquartil\n desses"
        " dois indica uma variação considerável da renda do primeiro quarto e o terceiro."+"\n")

    print("\nQuestão K: resposta na linha 193.")
    respostas.write("\nQuestão K: resposta na linha 193.\n")
    '''k) Crie uma função que calcule o coeficiente de variação. Resposta na linha 193
    
    
    l) Calcule o coeficiente de variação para a variável idade e renda. Compare os dois coeficientes devariação. '''
    print("Questão L:")
    respostas.write("\nQuestão L:\n")
    deltaRenda = deltaV(cr)
    deltaIdade = deltaV(ci)
    print("Coeficiente de variação da idade:", str(deltaIdade)+'%'," Coeficiente de variação de renda:", str(deltaRenda)+'%')
    if(deltaIdade < deltaRenda):
        print("o coeficiente de variação de idade é menor que o de renda. Portanto, é mais homogêneo")
        respostas.write("o coeficiente de variação de idade é menor que o de renda. Portanto, é mais homogêneo\n")
    elif(deltaIdade == deltaRenda):
        print("o coeficiente de variação de renda e o de idade são iguais.")
        respostas.write("o coeficiente de variação de renda e o de idade são iguais.\n")
    else:
        print("O coeficiente de variação de idade é maior que o de renda")
        respostas.write("O coeficiente de variação de idade é maior que o de renda. Portanto, é menos homogêneo\n")
    #rotina pra calcular desvio padrão de cada região do país.
    respostas.write("Coeficiente de variação da idade: " + str(deltaIdade)+'%' + " Coeficiente de variação de renda: " + str(deltaRenda)+'%'+'\n')


    '''m) Calcule o desvio - padrão para a renda de acordo com cada região do Brasil. Qual é a região que possui um comportamento mais homogêneo em relação à renda?'''
    print("Questão M:")
    respostas.write("\nQuestão M:\n")
    idReg = getDistinct(getMatrizColuna(conteudo, reg[0]))
    dpReg = desvioRendaPorRegiao(conteudo, idReg)
    x = dpReg[0][1]
    nReg = ""
    for i in range(len(dpReg)):
        print("Região: ", dpReg[i][0]+',', "desvio padrão:", dpReg[i][1])
        respostas.write("Região: " + dpReg[i][0]+',' + "desvio padrão:" + str(dpReg[i][1])+'\n')
        if dpReg[i][1] < x:
            x = dpReg[i][1]
            nReg = dpReg[i][0]
    print("A região com o comportamento mais homogêneo é a", nReg+",", "com o desvio padrão de", x)
    respostas.write("A região com o comportamento mais homogêneo é a " + nReg+"," + " com o desvio padrão de " + str(x)+'\n')
    respostas.close()
main()