"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time


def napominalka():
    text=input("Пойди покушать\n")
    time.sleep(5)
    print("Напоминал-КА:", text)


napominalka_thread=threading.Thread(target=napominalka)
napominalka_thread.start()

time.sleep(5)
print("коНЕЦ")