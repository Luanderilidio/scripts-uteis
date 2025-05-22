import pandas as pd
import os 

# Configurações iniciais
input_file = "154C - Frequências Turma x Disciplina - Professor(3).xlsx"
output_folder = "Planilhas_Separadas"
escola_coluna = "Lotacao" 
cidade_coluna = "Municipio" 

# Criar diretório de saída, se não existir
os.makedirs(output_folder, exist_ok=True)

# Carregar a planilha
df = pd.read_excel(input_file, engine="openpyxl")

# Verifica se as colunas existem
if escola_coluna not in df.columns or cidade_coluna not in df.columns:
    raise ValueError(f"Verifique se as colunas '{escola_coluna}' e '{cidade_coluna}' existem na planilha.")

# Agrupar e salvar por escola
for (cidade, escola), grupo in df.groupby([cidade_coluna, escola_coluna]):
    cidade_nome = str(cidade).strip().replace(" ", "_")  # Remove espaços extras
    escola_nome = str(escola).strip().replace(" ", "_")  # Remove espaços extras
    output_file = os.path.join(output_folder, f"{escola_nome} - {cidade_nome} INFREQUÊNCIA - 19-05-25.xlsx")
    
    # Salvar grupo em novo arquivo
    grupo.to_excel(output_file, index=False, engine="openpyxl")

print("Divisão concluída!")
