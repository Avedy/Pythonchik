"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time


def inputik():
    c=0
    while True:
        print("Введите быстрее")
        time.sleep(3)
        c+=1
        if c==10:
            print("Вы взорвались")
            break


def bomba():
    code = input("\nВведите код: ")
    if code == "гонеп":
        print("Бомба разминирована")
    else:
        print("Вы взорвались")

if __name__ == "__main__":
    thread = threading.Thread(target=inputik)
    thread.daemon = True
    thread.start()
    bomba()