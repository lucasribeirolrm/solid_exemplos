class Entrega:
    def calcular_tempo(self):
        raise NotImplementedError("Este método deve ser implementado por subclasses.")


class EntregaExpressa(Entrega):
    def calcular_tempo(self):
        return "Entrega em 1 dia"


class EntregaNormal(Entrega):
    def calcular_tempo(self):
        return "Entrega em 5 dias"


def verificar_entrega(entrega: Entrega):
    print(f"Tempo de entrega: {entrega.calcular_tempo()}")


# Uso
entrega_expressa = EntregaExpressa()
entrega_normal = EntregaNormal()

verificar_entrega(entrega_expressa)
verificar_entrega(entrega_normal)
