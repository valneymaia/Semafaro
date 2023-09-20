import threading
import time
import random

semaforo = threading.Semaphore(3)  # Inicializa o semáforo com 3 permissões para as caixas
fila = []

def cliente():
    while True:
        semaforo.acquire()  # O cliente adquire uma permissão para uma das caixas
        if fila:
            cliente_atual = fila.pop(0)  # Remove o primeiro cliente da fila
            print(f"{threading.currentThread().getName()} está sendo atendido.")
            tempo_atendimento = random.randint(3, 10)
            time.sleep(tempo_atendimento)
            print(f"{threading.currentThread().getName()} foi atendido em {tempo_atendimento} segundos.")
        semaforo.release()  # Libera a caixa para o próximo cliente
        time.sleep(random.randint(1, 3))  # Cliente aguarda um tempo aleatório antes de entrar na fila

def gerar_clientes():
    for i in range(30):
        cliente_thread = threading.Thread(target=cliente)
        cliente_thread.start()
        fila.append(cliente_thread)
        time.sleep(random.randint(1, 5))  # Gera clientes aleatoriamente

if __name__ == "__main__":
    gerar_clientes()
