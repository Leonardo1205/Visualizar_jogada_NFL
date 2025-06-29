import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def identificar_jogador_e_time(jogada: pd.DataFrame):
    for evento in ('pass_forward', 'handoff'):
        ev = jogada[jogada['event'] == evento]
        if not ev.empty:
            row = ev.iloc[0]
            return row['displayName'], row['club']
    players = jogada[jogada['displayName'].str.lower() != 'football']
    if not players.empty:
        row = players.iloc[0]
        return row['displayName'], row['club']
    return 'N/A', 'N/A'

def plot_jogada(jogada: pd.DataFrame, game_id: int, play_id: int,
                jogador: str, clube: str):
    plt.figure(figsize=(12, 6))
    sns.set_style("white")

    # campo
    plt.plot([0,120,120,0,0], [0,0,53.3,53.3,0], color="green")
    plt.fill_between([0,120], 0, 53.3, color='green', alpha=0.1)
    plt.plot([60,60], [0,53.3], color='white', linestyle='--', linewidth=1)

    bola = jogada[jogada['displayName'].str.lower() == 'football']
    jogadores = jogada[jogada['displayName'].str.lower() != 'football']

    for club in jogadores['club'].unique():
        sub = jogadores[jogadores['club'] == club]
        plt.scatter(sub['x'], sub['y'], s=80, label=club)

    if not bola.empty:
        plt.scatter(bola['x'], bola['y'], color='brown', s=100, label='Ball')

    plt.title(
        f"Game {game_id} | Play {play_id}    —    "
        f"Jogador: {jogador}    |    Time: {clube}"
    )
    plt.xlabel("Jardas (X)")
    plt.ylabel("Jardas (Y)")
    plt.xlim(0,120)
    plt.ylim(0,53.3)
    plt.legend(loc='upper right')

if __name__ == "__main__":
    # 1) Encontra todos os parquet disponíveis
    files = glob.glob("tracking_week_*.parquet")
    semanas = sorted(int(f.split("_")[-1].split(".")[0]) for f in files)
    if not semanas:
        print("❌ Nenhum 'tracking_week_*.parquet' encontrado.")
        sys.exit(1)

    print(f"Semanas disponíveis: {semanas}")
    semana = input("Escolha uma das semanas acima: ").strip()
    if not semana.isdigit() or int(semana) not in semanas:
        print("❌ Semana inválida.")
        sys.exit(1)
    parquet_file = f"tracking_week_{semana}.parquet"

    # 2) Carrega o DataFrame
    try:
        df = pd.read_parquet(parquet_file)
    except Exception as e:
        print(f"❌ Erro ao ler `{parquet_file}`: {e}")
        sys.exit(1)
    print(f"✔ Carregado {len(df):,} registros de {parquet_file}\n")

    # 3) Pede IDs
    try:
        game_id = int(input("Game ID: ").strip())
        play_id = int(input("Play ID: ").strip())
    except ValueError:
        print("❌ Game ID e Play ID devem ser números.")
        sys.exit(1)

    # 4) Filtra a jogada
    jogada = df[(df['gameId'] == game_id) & (df['playId'] == play_id)]
    if jogada.empty:
        print("❌ Jogada não encontrada.")
        sys.exit(1)

    # 5) Identifica e imprime no console
    jogador, clube = identificar_jogador_e_time(jogada)

    # 6) Plota e exibe
    plot_jogada(jogada, game_id, play_id, jogador, clube)
    plt.show()
