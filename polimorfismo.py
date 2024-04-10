class Persona  :

    def __init__(self, nombre ) :
        self.nombre = nombre

    def avanza(self):
        return "ando caminandando"

class Ciclista(Persona) :

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        return "ando moviendom e en mi bicicleta"

if __name__ == '__main__':
    persona = Persona('clodomiro')
    print(persona.avanza())

    ciclista = Ciclista('kuiper')
    print(ciclista.avanza())
