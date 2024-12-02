class ProcessadorDePagamento:
    def processar(self, pedido):
        raise NotImplementedError


class ProcessadorCartao(ProcessadorDePagamento):
    def processar(self, pedido):
        print(f"Processando pagamento com cartão para {pedido.usuario.nome}.")


class ProcessadorBoleto(ProcessadorDePagamento):
    def processar(self, pedido):
        print(f"Processando pagamento com boleto para {pedido.usuario.nome}.")


class SistemaDePedidos:
    def __init__(self, processador: ProcessadorDePagamento):
        self.processador = processador

    def realizar_pedido(self, usuario, total):
        pedido = Pedido(usuario, total)
        self.processador.processar(pedido)


# Uso
usuario = Usuario("Pedro", "pedro@example.com")
sistema_cartao = SistemaDePedidos(ProcessadorCartao())
sistema_boleto = SistemaDePedidos(ProcessadorBoleto())

sistema_cartao.realizar_pedido(usuario, 300.00)
sistema_boleto.realizar_pedido(usuario, 150.00)
