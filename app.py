from flask import Flask, request, render_template
from abc import ABC, abstractmethod

app = Flask(__name__)

class Relatorio(ABC):
    @abstractmethod
    def gerar(self):
        pass

class RelatorioBasico(Relatorio):
    def gerar(self):
        return "Conteúdo do Relatório"

class DecoradorRelatorio(Relatorio):
    def __init__(self, relatorio: Relatorio):
        self._relatorio = relatorio

    def gerar(self):
        return self._relatorio.gerar()

class DecoradorCabecalho(DecoradorRelatorio):
    def __init__(self, relatorio: Relatorio, cabecalho: str):
        super().__init__(relatorio)
        self.cabecalho = cabecalho

    def gerar(self):
        return f"{self.cabecalho}\n{super().gerar()}"

class DecoradorRodape(DecoradorRelatorio):
    def __init__(self, relatorio: Relatorio, rodape: str):
        super().__init__(relatorio)
        self.rodape = rodape

    def gerar(self):
        return f"{super().gerar()}\n{self.rodape}"

class DecoradorBorda(DecoradorRelatorio):
    def gerar(self):
        return f"**********\n{super().gerar()}\n**********"

class DecoradorCorTexto(DecoradorRelatorio):
    def __init__(self, relatorio: Relatorio, cor: str):
        super().__init__(relatorio)
        self.cor = cor

    def gerar(self):
        return f"[Cor: {self.cor}]\n{super().gerar()}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        relatorio = RelatorioBasico()

        if "cabecalho" in request.form:
            relatorio = DecoradorCabecalho(relatorio, "=== Cabeçalho do Relatório ===")
        if "rodape" in request.form:
            relatorio = DecoradorRodape(relatorio, "=== Rodapé do Relatório ===")
        if "borda" in request.form:
            relatorio = DecoradorBorda(relatorio)
        if "cor" in request.form:
            cor = request.form["cor"]
            relatorio = DecoradorCorTexto(relatorio, cor)

        resultado = relatorio.gerar()
        return render_template("index.html", resultado=resultado)

    return render_template("index.html", resultado=None)

if __name__ == "__main__":
    app.run(debug=True)
