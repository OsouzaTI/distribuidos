import pandas as pd
import matplotlib.pyplot as plt
import os

def path_log_name(log_path):
    return log_path.split('/')[-1]

def concatenar_logs(log_path) -> pd.DataFrame:
    data_frames = []
    for path in map(lambda p: p.path, os.scandir(log_path)):
        name = path.split('/')[-1]
        if name == 'info.log': 
            continue
        log_csv = pd.read_csv(path, delimiter=';')
        data_frames.append(log_csv)
    return pd.concat(data_frames, ignore_index=True)

def maximo(data: pd.DataFrame) -> list[float, float]:
    return [data['cpu_usage'].max(), data['memory_usage'].max()]


log_paths = map(lambda p: p.path, os.scandir())
for log_path in log_paths:
    if(log_path == './grafico.py'):
        continue 
    log_path = log_path.replace('./', '')
    logs = concatenar_logs(f'{os.getcwd()}/{log_path}')
    print(maximo(logs))
