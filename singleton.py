class Singleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

class RegistroUsuarios(Singleton):
    def __init__(self):
        if not hasattr(self, "usuarios"):
            self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario}' adicionado.")

    def obter_usuarios(self):
        return self.usuarios

if __name__ == "__main__":
    registro1 = RegistroUsuarios()
    registro2 = RegistroUsuarios()

    registro1.adicionar_usuario("Alice")
    registro2.adicionar_usuario("Bob")

    print("Ambas as instâncias são iguais?", registro1 is registro2)  # True
    print("Usuários registrados:", registro1.obter_usuarios())
