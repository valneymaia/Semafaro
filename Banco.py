import threading
import time
import random

semaforo = threading.Semaphore(3)  # Inicializa o semáforo com 3 permissões para as caixas
fila = []
clientes_atendidos = 0
total_clientes = 30

def cliente(caixa):
    global clientes_atendidos
    while True:
        semaforo.acquire()  # O cliente agurda e permissao para ir um dos caixas
        if fila:
            cliente_atual = fila.pop(0)  # Remove o primeiro cliente da fila
            print(f"Cliente {cliente_atual} está sendo atendido no {caixa}.")
            tempo_atendimento = random.randint(3, 10)
            time.sleep(tempo_atendimento)
            print(f"Cliente {cliente_atual} foi atendido no {caixa} em {tempo_atendimento} segundos.")
            clientes_atendidos += 1  # Incrementa o número de clientes atendidos
            if clientes_atendidos == total_clientes:
                print("Todos os clientes foram atendidos.") #imprime quando todos 30 clientes sao atendidos
        semaforo.release()  # Libera a caixa para o próximo cliente
        time.sleep(random.randint(1, 3))  # Cliente aguarda um tempo aleatório antes de entrar na fila tempo de caminha até o caixa

def gerar_clientes():
    for i in range(1, total_clientes + 1):
        fila.append(i)  # chama os clientes à fila
        time.sleep(random.randint(1, 5))  # Gera clientes aleatoriamente

if __name__ == "__main__":
    for i in range(3):
        caixa_thread = threading.Thread(target=cliente, args=(f"Caixa {i+1}",))
        caixa_thread.start()
    gerar_clientes()
