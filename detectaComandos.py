import time
from mpu6050_i2c import *


def detectaComandos(sensor_ativo=True,tempo_de_amostragem=2,intervalo_de_amostragem=0.01,tempo_estacionario=0.1):
    #Calibragem
    estacionarios_maximos = [[0.05,0.06,0.53],[4,4,4]]
    estacionarios_minimos = [[-0.09,-0.03,0.5],[-4,-4,-4]]

    #Inicializacao das variaveis usadas
    amostras = [[[],[],[]],[[],[],[],[]]]
    tempo_parado = 0
    estado_estacionario = False

    #Enquanto o sensor estiver ativo faz a deteccao de comandos
    while sensor_ativo:
        #Coleta os valores atuais dos sensores
        try:
            acelerometro_x, acelerometro_y, acelerometro_z, giroscopio_x, giroscopio_y, giroscopio_z = mpu6050_conv()
        except:
            continue

        #Acrescenta os valores atuais dos sensores aas amostras
        amostras[0][0].append(acelerometro_x)
        amostras[0][1].append(acelerometro_y)
        amostras[0][2].append(acelerometro_z)
        amostras[1][0].append(giroscopio_x)
        amostras[1][1].append(giroscopio_y)
        amostras[1][2].append(giroscopio_z)
        
        #Caso as ultimas "tempo_estacionario/intervalo_de_amostragem" amostras se enquadrem na definicao de estacionario eh definido que se esta em estado estacionario
        if (estacionarios_minimos[0][0] < amostras[0][0][-1] < estacionarios_maximos[0][0]) and (estacionarios_minimos[0][1] < amostras[0][1][-1] < estacionarios_maximos[0][1]) and (estacionarios_minimos[0][2] < amostras[0][2][-1] < estacionarios_maximos[0][2]) and (estacionarios_minimos[1][0] < amostras[1][0][-1] < estacionarios_maximos[1][0]) and (estacionarios_minimos[1][1] < amostras[1][1][-1] < estacionarios_maximos[1][1]) and (estacionarios_minimos[1][2] < amostras[1][2][-1] < estacionarios_maximos[1][2]):
            tempo_parado += intervalo_de_amostragem
            if tempo_parado == tempo_estacionario:
                estado_estacionario = True
                tempo_parado = 0
        else:
            tempo_parado = 0
        
        #Detecta se ocorreu algum comando
        abaixaVolume(amostras)
        
        #Remove o status de estado estacionario
        estado_estacionario = False
        
        #Caso ja tenha se atingido o numero de amostras definido remove a amostra mais antiga
        if len(amostras[0][0]) == tempo_de_amostragem/intervalo_de_amostragem:
            del(amostras[0][0][0])
            del(amostras[0][1][0])
            del(amostras[0][2][0])
            del(amostras[1][0][0])
            del(amostras[1][1][0])
            del(amostras[1][2][0])
        
        #Espera o intervalo de amostragem definido antes de coletar a proxima amostra
        time.sleep(intervalo_de_amostragem)


def abaixaVolume(amostras):
    #Calibragem (x e z do acelemetro se movimentam, x aumenta e z diminui)
    maximos = [[0,0.04,0.5],[]]
    minimos = [[-0.4,-0.15,0.35],[]]
    
    #Detecta se ocorreu o comando de abaixar o volume
    if (min(amostras[0][0]) < minimos[0][0]) and (max(amostras[0][0]) > maximos[0][0]) and (min(amostras[0][2]) < minimos[0][2]) and (max(amostras[0][2]) > maximos[0][2]) and (amostras[0][0].index(min(amostras[0][0]))<amostras[0][0].index(max(amostras[0][0]))) and (amostras[0][2].index(min(amostras[0][2]))>amostras[0][2].index(max(amostras[0][2]))) and (minimos[0][1] < min(amostras[0][1]) < maximos[0][1]) and (minimos[0][1] < max(amostras[0][1]) < maximos[0][1]):
        print("Detectado o comando para abaixar o volume.")
        amostras.clear()

