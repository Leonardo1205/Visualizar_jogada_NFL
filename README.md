# 🏈 Visualizador de Jogadas NFL Big Data Bowl 🚀

Uma ferramenta em **Python** para **visualizar graficamente** jogadas do dataset **NFL Big Data Bowl 2025**.  
Identifica automaticamente o jogador que inicia a jogada (passe ou handoff), mostra seu time em posse e plota em campo as trajetórias dos jogadores e da bola.

🛠️ **Tecnologias Utilizadas**

- **Python 3.8+**  
- **Pandas** (manipulação de dados)  
- **PyArrow** (formato Parquet)  
- **Matplotlib** & **Seaborn** (visualização gráfica)  
- **Glob** (detecção automática de arquivos)

📥 **Download dos Dados**

1. Crie conta no [Kaggle](https://www.kaggle.com/)  
2. Acesse **NFL Big Data Bowl 2025** → **Data**  
3. Baixe os arquivos  
   - `tracking_week_1.csv`  
   - `tracking_week_2.csv`  
   - … até as semanas desejadas  


🚀 **Como Executar**
1. Clonar o repositório https://github.com/Leonardo1205/Visualizar_jogada_NFL
2. Coloque todos os CSVs na raiz do projeto (`projeto_Nfl/`)
3. Converter arquivos CSV em PARQUET executando o comando: python converter_tracking_para_parquet.py
4. Depois dar o comando python visualizar_jogada.py
   - Escolha a semana, com base nos arquivos baixados 
   - Informe Game ID e Play ID
   - Confira a janela com o gráfico da jogada




