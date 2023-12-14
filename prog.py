import os
import codecs


car_sel=''
class Car:
    def __init__(self, brand, country, number, colour, korobka, privod, kuzov, \
                 obiom, mosh, dveri, probeg, ruchnik, fari, sost, op, multi):
        self.brand = brand
        self.country = country
        self.number = number
        self.colour = colour
        self.korobka = korobka
        self.privod = privod
        self.kuzov = kuzov
        self.obiom = obiom
        self.mosh = mosh
        self.dveri = dveri
        self.probeg = probeg
        self.ruchnik = ruchnik
        self.fari = fari
        self.sost = sost
        self.op = op
        self.multi = multi

    def __str__(self):
        return f"{self.brand}\nПроизводитель: {self.country}\nНомер: {self.number}\nЦвет: {self.colour} " \
               f"\nКоробка: {self.korobka}\nПривод: {self.privod}\nКузов: {self.kuzov}\nОбъем: {self.obiom} " \
               f"\nМощность: {self.mosh}\nКол-во дверей: {self.dveri}\nПробег: {self.probeg}\nРучник: {self.ruchnik}\nФары: {self.fari}" \
               f"\nСостояние: {self.sost}\nДвери: {self.op}\nМультимедия: {self.multi}\n"


class CarManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def create_car(self, car):
        file_path = os.path.join(self.folder_path, f"{car.brand}_{car.number}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(car))

    def list_cars(self):
        car_files = [f for f in os.listdir(self.folder_path) if f.endswith(".txt")]
        for i, lego in enumerate(car_files):
            print(str(i + 1)+".", lego)
        print("0. Назад")
        if not car_files:
            print("Нет машин")
        else:
            for car_file in car_files:
                car_sel = int(input())
                print("")
                # Если число больше имеющихся файлов
                if car_sel > len(car_files):
                    print("Error")
                    break
                # если пользователь хочет выйти
                elif car_sel == 0:
                    break
                # если число отрицательное
                elif car_sel < 0:
                    print("Error")
                    break
                else:
                    with open("gg/" + car_files[car_sel - 1], "r", encoding="utf-8") as file:
                        print(file.read())
                        break

    def delete_car(self):
        car_files = [f for f in os.listdir(self.folder_path) if f.endswith(".txt")]
        print("Выбирите автомобиль который хотите удалить:")
        for i, lego in enumerate(car_files):
            print(str(i + 1)+'.', lego)
        print("0. Назад")
        for car_file in car_files:
            baz = int(input())

            if baz > len(car_files):
                print("Error")
                break
            elif baz == 0:
                break
            elif baz < 0:
                break
            else:
                os.remove("gg/" + car_files[baz - 1])
                del car_files[baz - 1]
                break

    def re(self):
        car_files = [f for f in os.listdir(self.folder_path) if f.endswith(".txt")]
        if not car_files:
            print("Нет машин")
        else:
            for i, lego in enumerate(car_files):
                print(i + 1, lego)
            print("0 Назад")
            car_sel=int(input())
            if car_sel==0:
                return 0
            else:
                return car_files[car_sel-1]

    def edit_car(self,brand):
        file_path = os.path.join(self.folder_path, f"{brand}")
        print("Выбирите характеристику ,которую хотите изменить:")
        print("1.Номер")
        print("2.Цвет")
        print("3.Коробка")
        print("4.Привод")
        print("5.Кузов")
        print("6.Объем")
        print("7.Мощность")
        print("8.Пробег")
        print("9.Ручник")
        print("10.Фары")
        print("11.Состояние двигателя")
        print("12.Двери")
        print("13.Мультимедия")
        print("0. Назад")
        ca=int(input())
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(file_path, "w", encoding="utf-8") as file:
                for line in lines:
                    if line.startswith("Номер") and ca==1:
                        new = input()
                        file.write(f"Номер: {new}\n")
                    elif line.startswith("Цвет") and ca==2:
                        new = input()
                        file.write(f"Цвет: : {new}\n")
                    elif line.startswith("Коробка") and ca == 3:
                        print("Выбирите коробку передач:")
                        print("1. Автомат")
                        print("2. Механика")
                        k=int(input())
                        if k==1:
                            file.write(f"Коробка: Автоматическая\n")
                        elif k==2:
                            file.write(f"Коробка: Механическая\n")
                        elif k>2:
                            file.write(line)
                    elif line.startswith("Привод") and ca == 4:
                        print("Выбирите привод автомобиля:")
                        print("1. Передний")
                        print("2. Задний")
                        print("3. 4wd")
                        k = int(input())
                        if k == 1:
                            file.write(f"Привод: Передний\n")
                        elif k == 2:
                            file.write(f"Привод: Задний\n")
                        elif k == 3:
                            file.write(f"Привод: 4wd\n")
                        elif k > 3:
                            file.write(line)
                    elif line.startswith("Кузов") and ca == 5:
                        print("Выбирите кузов автомобиля:")
                        print("1. Универсал")
                        print("2. Седан")
                        print("3. Хетчбэк")
                        k = int(input())
                        if k == 1:
                            file.write(f"Кузов: Универсал\n")
                        elif k == 2:
                            file.write(f"Кузов: Седан\n")
                        elif k == 3:
                            file.write(f"Кузов: Хетчбэк\n")
                        elif k > 3:
                            file.write(line)
                    elif line.startswith("Объем") and ca == 6:
                        new = input()
                        file.write(f"Объем: {new}\n")
                    elif line.startswith("Мощность") and ca == 7:
                        new = input()
                        file.write(f"Мощность: {new}\n")
                    elif line.startswith("Пробег") and ca == 8:
                        new = input()
                        file.write(f"Пробег: {new}\n")
                    elif line.startswith("Ручник") and ca == 9:
                        print("Ручник:")
                        print("1. Поднят")
                        print("2. Опущен")
                        k = int(input())
                        if k == 1:
                            file.write(f"Ручник: Поднят\n")
                        elif k == 2:
                            file.write(f"Ручник: Опущен\n")
                        elif k > 2:
                            file.write(line)
                    elif line.startswith("Фары") and ca == 10:
                        print("Фары:")
                        print("1. Горят")
                        print("2. Не горят")
                        k = int(input())
                        if k == 1:
                            file.write(f"Фары: Горят\n")
                        elif k == 2:
                            file.write(f"Фары: Не горят\n")
                        elif k > 2:
                            file.write(line)
                    elif line.startswith("Состояние двигателя") and ca == 11:
                        print("Состояние двигателя:")
                        print("1. Заведен")
                        print("2. Заглущен")
                        k = int(input())
                        if k == 1:
                            file.write(f"Состояние двигателя: Заведен\n")
                        elif k == 2:
                            file.write(f"Состояние двигателя: Заглущен\n")
                        elif k > 2:
                            file.write(line)
                    elif line.startswith("Двери") and ca == 12:
                        print("Двери:")
                        print("1. Открыты")
                        print("2. Закрыты")
                        k = int(input())
                        if k == 1:
                            file.write(f"Двери: Открыты\n")
                        elif k == 2:
                            file.write(f"Двери: Закрыты\n")
                        elif k > 2:
                            file.write(line)
                    elif line.startswith("Мультимедия") and ca == 13:
                        print("Мультимедия:")
                        print("1. Есть")
                        print("2. Нет")
                        k = int(input())
                        if k == 1:
                            file.write(f"Мультимедия: Есть\n")
                        elif k == 2:
                            file.write(f"Мультимедия: Нет\n")
                        elif k > 2:
                            file.write(line)
                    else:
                        file.write(line)
        else:
            print("Нет машин")

    def poisk_colour(self, colour):
        matching_cars = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                car_file_path = os.path.join(self.folder_path, filename)
                with open(car_file_path, 'r',encoding="utf-8") as car_file:
                    lines = car_file.readlines()
                for line in lines:
                    if line.startswith("Цвет:"):
                        car_color = line.split(":")[1].strip()
                        if car_color == color:
                            matching_cars.append(filename[:-4])
        return matching_cars

    def poisk_numa(self, number):
        matching_cars = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                car_file_path = os.path.join(self.folder_path, filename)
                with open(car_file_path, 'r',encoding="utf-8") as car_file:
                    lines = car_file.readlines()
                for line in lines:
                    if line.startswith("Номер:"):
                        car_num = line.split(":")[1].strip()
                        if car_num == number:
                            matching_cars.append(filename[:-4])
        return matching_cars

    def poisk_strana(self, country):
        matching_cars = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                car_file_path = os.path.join(self.folder_path, filename)
                with open(car_file_path, 'r',encoding="utf-8") as car_file:
                    lines = car_file.readlines()
                for line in lines:
                    if line.startswith("Производитель: "):
                        car_pr = line.split(":")[1].strip()
                        if car_pr == country:
                            matching_cars.append(filename[:-4])
        return matching_cars

    def cop(self):
        car_files = [f for f in os.listdir(self.folder_path) if f.endswith(".txt")]
        print("Выберите автомобиль в котором хотите копировать данные:")
        for i, lego in enumerate(car_files):
            print(str(i + 1) + '.', lego)
        print("0. Назад")
        for car_file in car_files:
            baz = int(input())
            if baz > len(car_files):
                print("Error")
                break
            elif baz == 0:
                break
            elif baz < 0:
                break
            else:
                print("Введите новый номер авто:")
                new = input()
                with open("gg/" + car_files[baz - 1], 'r', encoding="utf-8") as file:
                    pos = 2
                    f = codecs.open("gg/" + car_files[baz - 1], 'r', encoding='utf8')
                    L = f.readlines()
                    if (pos >= 0) and (pos < len(L)):
                        if (pos == len(L) - 1):
                            L[pos] = 'Номер: ' + new
                        else:
                            L[pos] = 'Номер: ' + new + '\n'
                    f.close()
                    f = codecs.open("gg/" + car_files[baz - 1], 'w+', encoding='utf8')
                    for line in L:
                        f.write(line)
                    f.close()
                    content = file.read()
                with open("gg/" + new + car_files[baz - 1], 'w', encoding="utf-8") as file:
                    file.write(content)
    def dobav(self):
        car_files = [f for f in os.listdir(self.folder_path) if f.endswith(".txt")]
        print("Выберите автомобиль в который хотите добавить параметр:")
        for i, lego in enumerate(car_files):
            print(str(i + 1) + "." + lego)
        print("0. Назад")
        for car_file in car_files:
            baz = int(input())
            if baz > len(car_files):
                print("Error")
                break
            elif baz == 0:
                break
            elif baz < 0:
                break
            else:
                print("Введите новый параметр:")
                par = input()
                print("Введите значение параметра:")
                znach = input() + "\n"
                with open("gg/" + car_files[baz - 1], "a", encoding="utf-8") as file:
                    file.write(par + ": " + znach)
                    break
    def ud(self):
        folder = 'C:/Users/PC/proj/venv/gg'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)






# -----------------------------
print("1. Список автомобилей")
print("2. Добавить автомобиль")
print("3. Удалить автомобиль")
print("4. Редактировать парметр автомобиля")
print("5. Поиск")
print("6. Копирование параметров автомобиля")
print("7. Добавить параметр")
print("8. Удалить все машины")
print("0. Выйти")
print("Ваш ответ:")

menu = int(input())
while menu != 0:
    # вывод списка автомобилей
    if menu == 1:
        car_manager = CarManager("gg")
        # Вывод списка автомобилей
        car_manager.list_cars()
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())
    # добавление нового авто
    elif menu == 2:
        car_manager = CarManager("gg")
        print("Введите название автомобиля:")
        nazv = input()
        print("Введите Производителя:")
        proizvoditel = input()
        print("Введите номер автомобиля:")
        mamba = input()
        print("Введите цвет автомобиля:")
        calar = input()
        print("Введите коробку передач(автомат или механика):")
        koro = input()
        print("Введите привод:")
        privod = input()
        print("Введите кузов:")
        kuzia = input()
        print("Введите объем:")
        obo = input()
        print("Введите мощность:")
        moshnost = input()
        print("Введите кол-во дверей")
        kal = input()
        print("Введите пробег")
        pr = input()
        # Создание нового автомобиля
        car1 = Car(nazv.upper(), proizvoditel, mamba, calar, koro, privod, kuzia, obo, moshnost, kal, pr, "опущен",
                   "выключены", "не заведена", "закрыты", "нет")
        car_manager.create_car(car1)
        print("")
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())
    # удаление авто
    elif menu == 3:
        car_manager = CarManager("gg")
        car_manager.delete_car()
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())
    # изменение параметра авто
    elif menu == 4:
        car_manager = CarManager("gg")
        car=car_manager.re()
        if car==0:
            print("1. Список автомобилей")
            print("2. Добавить автомобиль")
            print("3. Удалить автомобиль")
            print("4. Редактировать парметр автомобиля")
            print("5. Поиск")
            print("6. Копирование параметров автомобиля")
            print("7. Добавить параметр")
            print("8. Удалить все машины")
            print("0. Выйти")
            print("Ваш ответ:")

            menu = int(input())
        else:
            car_manager.edit_car(car)
    #поиск автомобиля
    elif menu==5:
        car_manager=CarManager("gg")
        print("По какому параметру хотите организовать поиск:")
        print("1. Цвет")
        print("2. Номер")
        print("3. Производитель")
        isheika = int(input())

        if isheika==1:
            color = input("Введите цвет для поиска: ")
            matching_cars = car_manager.poisk_colour(color)
            if matching_cars:
                print(f"Найденные автомобили с цветом {color}: {', '.join(matching_cars)}")
                print("")
                print("1. Вывести характеристи автомобилей")
                print("2. Назад")
                cha_vi = int(input())
                if cha_vi==1:
                    for i, lego in enumerate(matching_cars):
                        print(i + 1, lego)
                    car_sel = int(input())
                    file_main = open("gg/" + matching_cars[car_sel - 1]+".txt", "r", encoding="utf-8")
                    file_main_viv = file_main.read()
                    print(file_main_viv)
                    print("1. Список автомобилей")
                    print("2. Добавить автомобиль")
                    print("3. Удалить автомобиль")
                    print("4. Редактировать парметр автомобиля")
                    print("5. Поиск")
                    print("6. Копирование параметров автомобиля")
                    print("7. Добавить параметр")
                    print("8. Удалить все машины")
                    print("0. Выйти")
                    print("Ваш ответ:")

                    menu = int(input())
                else:
                    print("1. Список автомобилей")
                    print("2. Добавить автомобиль")
                    print("3. Удалить автомобиль")
                    print("4. Редактировать парметр автомобиля")
                    print("5. Поиск")
                    print("6. Копирование параметров автомобиля")
                    print("7. Добавить параметр")
                    print("8. Удалить все машины")
                    print("0. Выйти")
                    print("Ваш ответ:")

                    menu = int(input())
            else:
                print(f"Автомобилей с цветом {color} не найдено.")
                break
        elif isheika==2:
            nomerok777 = input("Введите номер для поиска: ")
            matching_cars = car_manager.poisk_numa(nomerok777)
            if matching_cars:
                print(f"Найденные автомобили с номером {nomerok777}: {', '.join(matching_cars)}")
                print("")
                print("1. Вывести характеристи автомобилей")
                print("2. Назад")
                cha_vi = int(input())
                if cha_vi == 1:
                    for i, lego in enumerate(matching_cars):
                        print(i + 1, lego)
                    car_se = int(input())
                    file_main = open("gg/" + matching_cars[car_se - 1]+".txt", "r", encoding="utf-8")
                    file_main_viv = file_main.read()
                    print(file_main_viv)
                    print("1. Список автомобилей")
                    print("2. Добавить автомобиль")
                    print("3. Удалить автомобиль")
                    print("4. Редактировать парметр автомобиля")
                    print("5. Поиск")
                    print("6. Копирование параметров автомобиля")
                    print("7. Добавить параметр")
                    print("8. Удалить все машины")
                    print("0. Выйти")
                    print("Ваш ответ:")
                    menu = int(input())
                else:
                    print("1. Список автомобилей")
                    print("2. Добавить автомобиль")
                    print("3. Удалить автомобиль")
                    print("4. Редактировать парметр автомобиля")
                    print("5. Поиск")
                    print("6. Копирование параметров автомобиля")
                    print("7. Добавить параметр")
                    print("8. Удалить все машины")
                    print("0. Выйти")
                    print("Ваш ответ:")
                    menu = int(input())
            else:
                print(f"Автомобилей с номером {nomerok777} не найдено.")
                break
        elif isheika==3:
            countrry = input("Введите страну для поиска: ")
            matching_cars = car_manager.poisk_strana(countrry)
            if matching_cars:
                print(f"Найденные автомобили с страной производителя {countrry}: {', '.join(matching_cars)}")
                print("")
                print("1. Вывести характеристи автомобилей")
                print("2. Назад")
                cha_vi = int(input())
                if cha_vi == 1:
                    for i, lego in enumerate(matching_cars):
                        print(i + 1, lego)
                    car_se = int(input())
                    file_main = open("gg/" + matching_cars[car_se - 1]+".txt", "r", encoding="utf-8")
                    file_main_viv = file_main.read()
                    print(file_main_viv)
                    print("1. Список автомобилей")
                    print("2. Добавить автомобиль")
                    print("3. Удалить автомобиль")
                    print("4. Редактировать парметр автомобиля")
                    print("5. Поиск")
                    print("6. Копирование параметров автомобиля")
                    print("7. Добавить параметр")
                    print("8. Удалить все машины")
                    print("0. Выйти")
                    print("Ваш ответ:")

                    menu = int(input())
                else:
                    print("1. Список автомобилей")
                    print("2. Добавить автомобиль")
                    print("3. Удалить автомобиль")
                    print("4. Редактировать парметр автомобиля")
                    print("5. Поиск")
                    print("6. Копирование параметров автомобиля")
                    print("7. Добавить параметр")
                    print("8. Удалить все машины")
                    print("0. Выйти")
                    print("Ваш ответ:")

                    menu = int(input())
            else:
                print(f"Автомобилей с страной производителя {countrry} не найдено.")
                break
        else:
            print("По какому параметру хотите организовать поиск:")
            print("1. Производитель")
            print("2. Номер")
            print("3. Цвет")
            isheika = int(input())
    elif menu == 6:
        car_manager = CarManager("gg")
        car = car_manager.cop()
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())
    elif menu==7:
        car_manager = CarManager("gg")
        car = car_manager.dobav()
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())
    elif menu == 8:
        car_manager = CarManager("gg")
        car = car_manager.ud()
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())
    # исключение на ошибку
    else:
        print("1. Список автомобилей")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Редактировать парметр автомобиля")
        print("5. Поиск")
        print("6. Копирование параметров автомобиля")
        print("7. Добавить параметр")
        print("8. Удалить все машины")
        print("0. Выйти")
        print("Ваш ответ:")
        menu = int(input())