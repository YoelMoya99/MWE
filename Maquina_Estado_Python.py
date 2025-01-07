Estado_Presente_Maquina_1 = ''

# ---- Definicion de estados Maquina 1 --- #

def Maquina_1():
    Estado_Presente_Maquina_1()

def Maquina_1_Estado_1():
    global Estado_Presente_Maquina_1
    print('M1, E1, para E3')
    Estado_Presente_Maquina_1 = Maquina_1_Estado_3

def Maquina_1_Estado_2():
    global Estado_Presente_Maquina_1
    print('M1,E2, para E4')
    Estado_Presente_Maquina_1 = Maquina_1_Estado_4

def Maquina_1_Estado_3():
    global Estado_Presente_Maquina_1
    print('M1, E3, para E2')
    Estado_Presente_Maquina_1 = Maquina_1_Estado_2

def Maquina_1_Estado_4():
    global Estado_Presente_Maquina_1
    print('M1, E4, para E1')
    Estado_Presente_Maquina_1 = Maquina_1_Estado_1


if __name__ == '__main__':

    Estado_Presente_Maquina_1 = Maquina_1_Estado_1

    for i in range(10):
        Maquina_1()

    print('Ya termino la ejecucion')
