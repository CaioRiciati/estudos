while True:
    from random import randint
    from time import sleep
    numero = int(input("que numero estou pensando?: "))
    for i in range(1,4):
        sleep(0.8)
        print(i)

    roleta = randint(0,5)
    if numero == roleta:
        print("vc ganhou!! nao vai morrer bixo")
    elif     numero == 7:
        print("vc ganhou!! nao vai morrer bixo")
        break
    else:
        print("se fudeu")
    print("RECOMEÇANDO...")
    sleep (3)
    print("-----------------------------------------------------------------------------------------------------------------")

