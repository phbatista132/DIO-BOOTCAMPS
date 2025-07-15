public class Iphone implements ReprodutorMusical, AparelhoTelefonico, NavegadorInternet {

    // ReprodutorMusical
    public void tocar() {
        System.out.println("Tocando música...");
    }

    public void pausar() {
        System.out.println("Música pausada.");
    }

    public void selecionarMusica(String musica) {
        System.out.println("Selecionando: " + musica);
    }

    // AparelhoTelefonico
    public void ligar(String numero) {
        System.out.println("Ligando para: " + numero);
    }

    public void atender() {
        System.out.println("Atendendo chamada...");
    }

    public void iniciarCorreioVoz() {
        System.out.println("Iniciando correio de voz...");
    }

    // NavegadorInternet
    public void exibirPagina(String url) {
        System.out.println("Exibindo página: " + url);
    }

    public void adicionarNovaAba() {
        System.out.println("Nova aba adicionada.");
    }

    public void atualizarPagina() {
        System.out.println("Atualizando página...");
    }

    //Teste da Classe
    public static void main(String[] args) {
        Iphone meuIphone = new Iphone();

        // Módulo musical
        meuIphone.selecionarMusica("Imagine - John Lennon");
        meuIphone.tocar();
        meuIphone.pausar();

        // Módulo telefone
        meuIphone.ligar("11987654321");
        meuIphone.atender();
        meuIphone.iniciarCorreioVoz();

        // Módulo navegador
        meuIphone.exibirPagina("");
        meuIphone.adicionarNovaAba();
        meuIphone.atualizarPagina();
    }
}
