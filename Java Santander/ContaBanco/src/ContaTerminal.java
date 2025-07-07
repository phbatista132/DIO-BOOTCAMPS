import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Por favor, digite o número da Conta!");
        int numeroConta = scanner.nextInt();

        System.out.println("Por favor, digite o número da Agência!");
        scanner.nextLine();
        String agencia = scanner.nextLine().to;

        System.out.println("Por favor, informe seu nome!");
        String nomeCliente = scanner.nextLine().toUpperCase();

        System.out.println("Por favor, informe o valor!");
        float saldo = scanner.nextFloat();

        System.out.printf(
                "Olá %s, obrigado por criar uma conta em nosso banco, sua agência é %s, conta %d e seu saldo: R$%.2f já está disponível para saque.%n",
                nomeCliente, agencia, numeroConta, saldo);

        scanner.close();
    }
}