class FizzBuzz:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def FizzBuzzi(self):
        for i in range(2, self.n3 + +1):
            if i % (self.n1 * self.n2) == 0:
                print("FizzBuzz")
            elif i % self.n1 == 0:
                print("Fizz")
            elif i % self.n2 == 0:
                print("Buzz")

    def trocar_number1(self):
        question = input("Deseja trocar o seu primeiro valor? [sim/nao]: ")
        if question.lower() == 'sim':
            while True:
                self.n1 = int(input("Insira o novo valor: "))
                if self.n1 > 9:
                    print("Valor não aceitável, tente novamente.")
                elif self.n1 < 2:
                    print("Valor não aceitável, tente novamente.")
                else:
                    break
        else:
            pass

    def trocar_number2(self):
        question = input("Deseja trocar o seu segundo valor? [sim/nao]: ")
        if question.lower() == 'sim':
            while True:
                self.n2 = int(input("Insira o novo valor: "))
                if self.n2 > 9:
                    print("Valor não aceitável, tente novamente.")
                elif self.n2 < 2:
                    print("Valor não aceitável, tente novamente.")
                else:
                    break
        else:
            pass

    def trocar_number3(self):
        question = input("Deseja trocar o seu terceiro valor? [sim/nao]: ")
        if question.lower() == 'sim':
            while True:
                self.n3 = int(input("Insira o novo valor: "))
                if self.n3 > 100:
                    print("Valor não aceitável, tente novamente.")
                elif self.n3 < 10:
                    print("Valor não aceitável, tente novamente.")
                else:
                    break
        else:
            pass




while True:
    numero_loop1 = int(input("Digite o primeiro valor: "))
    if numero_loop1 > 9:
        print("Valor não aceitável, tente novamente.")
    elif numero_loop1 < 2:
        print("Valor não aceitável, tente novamente.")
    else:
        break

while True:
    numero_loop2 = int(input("Digite o segundo valor: "))
    if numero_loop2 > 9:
        print("Valor não aceitável, tente novamente")
    elif numero_loop2 < 2:
        print("Valor não aceitável, tente novamente.")
    else:
        break

while True:
    numero_3 = int(input("Digite o terceiro valor: "))
    if numero_3 > 100:
        print("Valor não aceitável, tente novamente.")
    elif numero_3 < 10:
        print("Valor não aceitável, tente novamente.")
    else:
        break

fizzbuzz = FizzBuzz(numero_loop1, numero_loop2, numero_3)

fizzbuzz.trocar_number1()
fizzbuzz.trocar_number2()
fizzbuzz.trocar_number3()
fizzbuzz.FizzBuzzi()

