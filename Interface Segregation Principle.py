class Notificador:
    def notificar(self, pedido):
        pass


class NotificadorEmail(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail para {pedido.cliente}: Seu pedido foi {pedido.status}.")


class NotificadorSMS(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS para {pedido.cliente}: Seu pedido foi {pedido.status}.")


# Uso
notificador_email = NotificadorEmail()
notificador_sms = NotificadorSMS()

notificador_email.notificar(pedido_cartao)
notificador_sms.notificar(pedido_boleto)
