class Счетчик:
    def __init__(self):
        self.__значение = 0

    def add(self):
        self.__значение += 1

    def получить_значение(self):
        return self.__значение


class Животное:
    def __init__(self, имя, команда, дата_рождения):
        self.__имя = имя
        self.__команда = команда
        self.__дата_рождения = дата_рождения

    def получить_имя(self):
        return self.__имя

    def получить_команду(self):
        return self.__команда

    def получить_возраст(self):
        # Реализация расчета возраста на основе даты рождения
        # В этом примере предполагается использование библиотеки datetime
        pass

    def обучить(self, новая_команда):
        self.__команда = новая_команда


class ДомашнееЖивотное(Животное):
    def __init__(self, имя, команда, дата_рождения, порода):
        super().__init__(имя, команда, дата_рождения)
        self.__порода = порода

    def получить_породу(self):
        return self.__порода


class Собака(ДомашнееЖивотное):
    def __init__(self, имя, команда, дата_рождения, порода, размер):
        super().__init__(имя, команда, дата_рождения, порода)
        self.__размер = размер

    def получить_размер(self):
        return self.__размер


class Кошка(ДомашнееЖивотное):
    def __init__(self, имя, команда, дата_рождения, порода, окрас):
        super().__init__(имя, команда, дата_рождения, порода)
        self.__окрас = окрас

    def получить_окрас(self):
        return self.__окрас


class Хомяк(ДомашнееЖивотное):
    def __init__(self, имя, команда, дата_рождения, порода, размер_колеса):
        super().__init__(имя, команда, дата_рождения, порода)
        self.__размер_колеса = размер_колеса

    def получить_размер_колеса(self):
        return self.__размер_колеса


def основное_меню():
    print("1. Завести новое животное")
    print("2. Определить животное в правильный класс")
    print("3. Увидеть список команд, которое выполняет животное")
    print("4. Обучить животное новым командам")
    print("5. Выход")


def main():
    счетчик = Счетчик()

    while True:
        try:
            основное_меню()
            выбор = int(input("Выберите действие: "))

            if выбор == 1:
                имя = input("Введите имя животного: ")
                команда = input("Введите команду животного: ")
                дата_рождения = input("Введите дату рождения животного (ГГГГ-ММ-ДД): ")

                # Создаем экземпляр счетчика и увеличиваем его значение
                with счетчик:
                    счетчик.add()

                print(f"Животное успешно зарегистрировано. Номер в реестре: {счетчик.получить_значение()}")
                # В этом месте вы можете создать экземпляр животного и добавить его в реестр

            elif выбор == 2:
                # В этом месте вы можете определить животное в правильный класс
                pass

            elif выбор == 3:
                # В этом месте вы можете вывести список команд, которое выполняет животное
                pass

            elif выбор == 4:
                # В этом месте вы можете обучить животное новым командам
                pass

            elif выбор == 5:
                print("Выход из программы.")
                break

            else:
                print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")

        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
