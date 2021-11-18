class Cicle:
    def __init__(self, raio):
        self.raio = raio

    def comprimento(self):
        comprimento = self.raio * 2 * 3.14
        return print(f"O comprimento do circulo é de {comprimento:.2f} cm")

    def area(self):
        area = 3.14 * (self.raio ** 2)
        return print(f"O valor da área do circulo é {area} cm²")

    def tamanho_raio(self):
        diametro = self.raio * 2
        return print(f"O tamanho do raio do circulo é de {self.raio} cm e seu diâmetro é {diametro} cm")

raio = float(input("""=============================
BEM VINDO AO CALCULADOR CICLE
=============================
POR FAVOR, DIGITE SEU RAIO (cm): """))

Circulo = Cicle(raio)
circulo_comprimento = Circulo.comprimento()
circulo_area = Circulo.area()
circulo_tamanho_raio = Circulo.tamanho_raio()

