Diagrama UML (em sintaxe Mermaid)

classDiagram
class ReprodutorMusical {
  +tocar()
  +pausar()
  +selecionarMusica(String musica)
}

class AparelhoTelefonico {
  +ligar(String numero)
  +atender()
  +iniciarCorreioVoz()
}

class NavegadorInternet {
  +exibirPagina(String url)
  +adicionarNovaAba()
  +atualizarPagina()
}

class Iphone implements ReprodutorMusical, AparelhoTelefonico, NavegadorInternet
