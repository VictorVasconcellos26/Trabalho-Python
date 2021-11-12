class Conversor:
    def __init__(self, a):
        self.a = a

    def DecimalForBinario(self, a):
        return  bin(self.a)

    def DecimalforHexadecimal(self):
        return hex(self.a)

    def BinarioForHexadecimal(self):
        self.a = hex(int(self.a))
        return

    def BinarioForDecimal(self):
        self.a = int(self.a, 2)
        return

    def HexadecimalForDecimal(self):
        self.a = int(self.a, 16)
        return
    def HexadecimalForBinario(self):
        self.a = bin(int(self.a, 16))[2:]
        return

Number = int(input("Digite um numero de sua preferencia: "))
print('''ESCOLHA UMA DAS OPÇÕES DE CONVERSÃO:
    [ 1 ] Converter de decimal para binario
    [ 2 ] Converter de decimal para hex
    [ 3 ] Converter de binario para hex
    [ 4 ] Converter de binario para decimal
    [ 5 ] Converter de hex para decimal
    [ 6 ] Converter de hex para binario    
 ''')
op = int(input("Sua opção: "))
if op == 1:
    print(f'{Number.DecimalForBinario()}')
else:
    op == 2:
    print(f'{Number.DecimalforHexadecimal()}')
else:
    op == 3:
        print(f'{Number.BinarioForHexadecimal()}')
else:
    op == 4:
        print(f'{Number.BinarioForDecimal()}')






