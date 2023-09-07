#Algoritmo de Microscopia confocal de varredura
print("Bem vindo! Sistema de Microscópio confocal.")

print("Anexe as informações necessárias:")
#Dados de entrada do Microscópio
tipo_celula=input("Qual tipo de célula:")
print("Houve alteração na variável inserida?",tipo_celula != '')
comprimento_ondadaluz=float(input("Insira o comprimento de onda desejada em nm:"))
print("Houve alteração na variável inserida?",comprimento_ondadaluz != 0.0)
intensidade_dolazer=float(input("Insira a intensidade do laser desejada em watts (W):"))
print("Houve alteração na variável inserida?",intensidade_dolazer != 0.0)
abertura_numerica=float(input("Insira o valor de abertura desejada :"))
print("Houve alteração na variável inserida?",abertura_numerica != 0.0)
varredurax=float(input("Insira o eixo X da varredura:"))
print("Houve alteração na variável inserida?",varredurax != 0.0)
varreduray=float(input("Insira o eixo Y da varredura:"))
print("Houve alteração na variável inserida?",varreduray != 0.0)
varreduraz=float(input("Insira o eixo Z da varredura:"))
print("Houve alteração na variável inserida?",varreduraz != 0.0)
resolucao_espacial=float(input("Insira a resolução espacial desejada em (nm) ou (um):"))
print("Houve alteração na variável inserida?",resolucao_espacial != 0.0)
resolucao_espectral=float(input("Insira a resolução espectral desejada em (nm):"))
print("Houve alteração na variável inserida?",resolucao_espectral != 0.0)
Filtro_emissao=float(input("insira a faixa de comprimento de onda (nm):"))
print("Houve alteração na variável inserida?",Filtro_emissao != 0.0)
Tempo_exposicao=float(input("Insira o tempo de expoisição em segundos:"))
print("Houve alteração na variável inserida?",Tempo_exposicao != 0.0)

# Exibir informações inseridas pelo usuário de forma organizada
print("Configurações setadas pelo usuário são:")
print(f"Tipo de célula: {tipo_celula}")
print(f"Comprimento de onda desejado: {comprimento_ondadaluz} nm")
print(f"Intensidade do laser desejada: {intensidade_dolazer} W")
print(f"Abertura numérica desejada: {abertura_numerica}")
print(f"Varredura X: {varredurax}")
print(f"Varredura Y: {varreduray}")
print(f"Varredura Z: {varreduraz}")
print(f"Resolução espacial desejada: {resolucao_espacial} nm/µm")
print(f"Resolução espectral desejada: {resolucao_espectral} nm")
print(f"Faixa de comprimento de onda: {Filtro_emissao} nm")
print(f"Tempo de exposição: {Tempo_exposicao} segundos")

#Calibração horizontal 
print("Para calibração do eixo horizontal utilize o primeiro (10x) e ultimo caractere (10x) do seu nome")
caractere_inicial=input("Digite a primeira letra do seu nome:")
caractere_final= input("Digite a ultima letra do seu nome:")
calibracao= input("Inicie a calibração: ")
verificador= [calibracao]
for letra in calibracao:
 print("caractere digitado",letra)
if letra [:10] != caractere_inicial * 10:
 print("Erro na calibração, verifique os caracteres digitados")
elif letra [-10:] != caractere_final * 10:
 print("Erro na calibração, verifique os caracteres digitados")
else:
    print("Calibração Horizontal realizada com sucesso")

#Calibração Vertical
print("Para calibração do eixo vertical utilize o segundo (10x) e penultimo caractere (10x) do seu nome")
caractere_segundo=input("Digite a segunda letra do seu nome:")
caractere_penultimo= input("Digite a penultima letra do seu nome:")
calibracao= input("Inicie a calibração: ")
for letra in calibracao:
 print("caractere digitado",letra)
if letra [:10] != caractere_segundo * 10:
 print("Erro na calibração, verifique os caracteres digitados")
elif letra [-10:] != caractere_penultimo * 10:
 print("Erro na calibração, verifique os caracteres digitados")
else:
    print("Calibração Vertucal realizada com sucesso")
    print("Calibração do sistema foi realizada com sucesso!")





