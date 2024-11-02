import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, warriors):
        threading.Thread.__init__(self)
        self.name = name
        self.warriors = warriors
        self.powers = 100
        self.days_battles = self.powers // self.warriors

    def battles(self, name, warriors):
        for day in range(self.days_battles):
            time.sleep(1)
            battles_rest = self.powers - self.warriors * (day + 1)
            print(f'{self.name} сражается {day + 1} день(дня)..., осталось {battles_rest} воинов.')
            if battles_rest == 0:
                print(f'{self.name} одержал победу спустя {day + 1} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battles(self.name, self.warriors)


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
