"""
CONSTANTE = "VARIÁVEIS" QUE NÃO MUDAM
Muitas condições no mesmo if (ruim)
 <- Contagem de complexidade (ruim)
"""

velocidade = 65 # velocidade atual do carro
local_do_carro = 102 #local em que o carro está na estrada

RADAR_1 = 60 #VELOCIDADE MÁXIMA DO RADAR
LOCAL_1 = 100 #LOCAL DO RADAR
RADAR_RANGE = 1 #RANGE DO RADAR

"""if velocidade > RADAR_1:
    print('Velocidade do carro passou do permitido do radar 1.')
if local_do_carro >= (LOCAL_1 - RADAR_RANGE) and local_do_carro <= (LOCAL_1 - RADAR_RANGE):
    print('Carro Multado')"""

if velocidade > RADAR_1 and local_do_carro >= (LOCAL_1 - RADAR_RANGE) and local_do_carro <= (LOCAL_1 + RADAR_RANGE):
    print('Você foi Multado')
else:
    print('Você não foi multado.')