class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def atualizar_email(self, novo_email):
        self.email = novo_email
        print(f"Email de {self.nome} atualizado para: {self.email}")


class Pedido:
    def __init__(self, usuario, total):
        self.usuario = usuario
        self.total = total
        self.status = "pendente"

    def atualizar_status(self, status):
        self.status = status
        print(f"Status do pedido de {self.usuario.nome} atualizado para: {self.status}")


class Notificador:
    def notificar(self, usuario, mensagem):
        print(f"Notificando {usuario.nome}: {mensagem}")


# Uso
usuario = Usuario("João", "joao@example.com")
pedido = Pedido(usuario, 150.00)
notificador = Notificador()

pedido.atualizar_status("pago")
notificador.notificar(usuario, "Seu pedido foi pago com sucesso!")
