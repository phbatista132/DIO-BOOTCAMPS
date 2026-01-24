import pandas as pd

# ============================
# ETAPA 1 - EXTRAÇÃO
# ============================
# Lê os dados de um arquivo CSV fictício com colunas: Nome, Conta, Cartao
# Exemplo de CSV (usuarios.csv):


usuarios = pd.read_csv("usuarios.csv")

print("=== Dados Extraídos ===")
print(usuarios)

# ============================
# ETAPA 2 - TRANSFORMAÇÃO
# ============================
# Cria mensagens personalizadas para cada usuário
usuarios["Mensagem"] = usuarios.apply(
    lambda row: f"Olá {row['Nome']}, sua conta {row['Conta']} está vinculada ao cartão {row['Cartao']}.",
    axis=1
)

print("\n=== Dados Transformados ===")
print(usuarios[["Nome", "Mensagem"]])

# ============================
# ETAPA 3 - CARREGAMENTO
# ============================
# Salva os dados enriquecidos em um novo arquivo CSV
usuarios.to_csv("usuarios_com_mensagens.csv", index=False)
