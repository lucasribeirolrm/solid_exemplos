class ProcessadorDePagamento:
    def processar(self, pedido):
        raise NotImplementedError("Este método deve ser implementado por subclasses.")


class ProcessadorDeCartao(ProcessadorDePagamento):
    def processar(self, pedido):
        print(f"Processando pagamento por cartão de {pedido.total} para {pedido.cliente}...")
        pedido.atualizar_status("pago")


class ProcessadorDeBoleto(ProcessadorDePagamento):
    def processar(self, pedido):
        print(f"Processando pagamento por boleto de {pedido.total} para {pedido.cliente}...")
        pedido.atualizar_status("pago")


# Uso
pedido = Pedido("Maria", 200.00)
processador_cartao = ProcessadorDeCartao()
processador_boleto = ProcessadorDeBoleto()

processador_cartao.processar(pedido)
notificador.notificar(pedido)

pedido_boleto = Pedido("Carlos", 300.00)
processador_boleto.processar(pedido_boleto)
notificador.notificar(pedido_boleto)
