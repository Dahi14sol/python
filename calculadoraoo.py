class Calculadora:
    # atributos
    p = None
    primer_numero = None
    segundo_numero = None
    resultado = None
    historial = None
    
    def __init__(self, p, s):
        self.primer_numero = p
        self.segundo_numero  = s
        self.resultado = 0.0
        self.historial = []

    def set_numeros(self, p, s):
        self.primer_numero = p
        self.segundo_numero = s

    def get_suma(self):
       self.resultado = self.primer_numero + self.segundo_numero
       texto = str(self.primer_numero) + "+" + str(self.segundo_numero) + "=" + str(self.resultado)
       self.historial.append( texto)
       return self.resultado
    
    def get_resultado(self):
        return self.resultado
    
    def get_historial(self):
        return self.historial

if __name__=="__main__":
    calc = Calculadora(12,15)
    print(calc.get_suma())
    calc.set_numeros(10,10)
    print(calc.get_suma())
    print(calc.get_historial())

