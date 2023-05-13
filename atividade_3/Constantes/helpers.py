import psutil
import os
from datetime import datetime
from Constantes.definitions import ServerLogInfo

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def open_file_log(thread_id, server_info : ServerLogInfo):    
    
    file_name = f'thread_{thread_id}'
    base_path = f'log/{server_info.date}'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    with open(f'{base_path}/info.log', 'w') as info:
        info.write(f'limit: {server_info.limit}')
        info.close()
    
    final_path = f'{base_path}/{file_name}.log'
    
    file = open(final_path, 'a')

    if server_info.first:
        # cabeçalho do CSV
        file.write('cpu_usage;memory_usage;\n')
        server_info.first = False

    return file