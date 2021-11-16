class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        return

    def soma(self):
        return self.a + self.b

    def subtraçao(self):
        return self.a - self.b

    def multiplicaçao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

    def potencia(self):
        return self.a ** self.b

    def modulo(self):
        return self.a % self.b

number_1 = int(input("Digite o 1º valor (maior): "))
number_2 = int(input("Digite o 2º valor (menor): "))

if number_1 < number_2:
    x = number_1
    number_1 = number_2
    number_2 = x

calculadora = Math(number_1,number_2)

print(f"""=========================
A soma do valores {number_1} e {number_2} é {calculadora.soma()}
A subtração dos valores {number_1} e {number_2} é {calculadora.subtraçao()}
A multiplicação dos valores {number_1} e {number_2} é {calculadora.multiplicaçao()}
A divisão dos valores {number_1} e {number_2} é {calculadora.divisao():.2f}
A potencia entre os valores {number_1} e {number_2} é {calculadora.potencia()}
O modulo entre os valores {number_1} e {number_2} é {calculadora.modulo()}
""")