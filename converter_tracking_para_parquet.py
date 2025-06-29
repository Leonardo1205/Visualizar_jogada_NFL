import pandas as pd
import glob
import os

def csv_para_parquet(csv_path: str, parquet_path: str):
    print(f"Convertendo {csv_path} → {parquet_path} ...")
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, engine='pyarrow')
    print("  OK")

if __name__ == "__main__":
    arquivos_csv = glob.glob('tracking_week_*.csv')
    for csv in arquivos_csv:
        base = os.path.splitext(csv)[0]
        parquet = f"{base}.parquet"
        csv_para_parquet(csv, parquet)
    print("Conversão concluída para todos os arquivos.")
