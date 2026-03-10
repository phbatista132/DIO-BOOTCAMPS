#  Projeto Educacional – Simulação de Malware em Python

## Objetivo
Este projeto demonstra, em ambiente **100% controlado e educacional**, como funcionam dois tipos de malware comuns — **Ransomware** e **Keylogger** — através de scripts em Python.  
O foco é compreender o funcionamento, refletir sobre defesa e documentar medidas de prevenção.

---

## Ransomware Simulado

### Técnicas utilizadas
- **Criação de arquivos de teste**: gerar arquivos `.txt`, `.pdf` ou `.jpg` fictícios.  
- **Criptografia**: uso da biblioteca `cryptography` (módulo `Fernet`) para criptografar o conteúdo dos arquivos.  
- **Mensagem de resgate**: criação automática de um arquivo `README_RESCUE.txt` com instruções falsas de pagamento.  
- **Descriptografia**: script reverso que, com a chave correta, devolve os arquivos ao estado original.  

### Objetivo educacional
- Mostrar como ransomwares sequestram dados.  
- Evidenciar a importância de **backups** e **controle de acesso**.  

---

## Keylogger Simulado

### Técnicas utilizadas
- **Captura de teclas**: uso da biblioteca `pynput` ou `keyboard` para registrar entradas do teclado.  
- **Armazenamento**: salvar as teclas em um arquivo oculto `.txt`.  
- **Automação**: envio do arquivo de log por e-mail usando `smtplib`.  
- **Furtividade**: execução em segundo plano, sem janela visível.  

### Objetivo educacional
- Demonstrar como keyloggers coletam informações sensíveis (senhas, mensagens).  
- Reforçar a necessidade de **antivírus**, **firewall** e **conscientização do usuário**.  

---

## Reflexão sobre Defesa

### Medidas de prevenção
- **Antivírus e firewall**: detectam comportamentos suspeitos como acesso contínuo ao teclado ou criptografia em massa.  
- **Sandboxing**: executar programas desconhecidos em ambiente isolado.  
- **Conscientização do usuário**: evitar clicar em links suspeitos ou abrir anexos desconhecidos.  
- **Boas práticas**: manter sistemas atualizados, usar backups regulares e restringir permissões de execução.  
