import random
import sys

fruits_arr = [
    "사과 - яблоко",
    "배 - груша",
    "바나나 - банан",
    "포도 - виноград",
    "오렌지 - апельсин",
    "레몬 - лимон",
    "자몽 (그레이프프루트) - грейпфрут, помело",
    "귤 - мандарин",
    "석류 (성뉴) - гранат",
    "복숭아 - персик",
    "살구 - абрикос",
    "자두 - слива",
    "체리 - вишня, черешня",
    "딸기 - клубника",
    "수박 - арбуз",
    "멜론 - дыня",
    "참외 - дынька(маленькая восточная дыня)",
    "감 - хурма",
    "키위 - киви",
    "파인애플 - ананас",
    "파파야 - папайя",
    "망고 - манго",
    "무화과 - инжир",
    "망고스틴 - мангостин"
]

fruits_quiz = [
    "яблоко",
    "груша",
    "банан",
    "виноград",
    "апельсин",
    "лимон",
    "грейпфрут, помело",
    "мандарин",
    "гранат",
    "персик",
    "абрикос",
    "слива",
    "вишня, черешня",
    "клубника",
    "арбуз",
    "дыня",
    "дынька(маленькая восточная дыня)",
    "хурма",
    "киви",
    "ананас",
    "папайя",
    "манго",
    "инжир",
    "мангостин"
]

vegetables_arr = [
    "가지 - баклажан",
    "콩 - фасоль",
    "완두콩 - горох",
    "양배추 - капуста",
    "감자 - картофель",
    "양파 - лук",
    "당근 - морковь",
    "오이 - огурец",
    "후추 - перец",
    "파슬리 - петрушка",
    "토마토 - помидор",
    "무 - редис",
    "사탕무우 - свекла",
    "셀러리 - сельдерей",
    "호박 - тыква",
    "딜 - укроп",
    "콩 - фасоль",
    "마늘 - чеснок",
    "밤색 - щавель"
]

vegetables_quiz = [
    "баклажан",
    "фасоль",
    "горох",
    "капуста",
    "картофель",
    "лук",
    "морковь",
    "огурец",
    "перец",
    "петрушка",
    "помидор",
    "редис",
    "свекла",
    "сельдерей",
    "тыква",
    "укроп",
    "фасоль",
    "чеснок",
    "щавель"
]

def main():
    print("Корейский язык")
    print("--------------")
    print("1 - Викторина")
    print("2 - Тренеровка письма")
    option = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("--Введите вариант: "))
    random.shuffle(fruits_arr)
    random.shuffle(vegetables_arr)

    if option == 1:
        print("1 - Фрукты")
        print("2 - Овощи")
        quiz = int(sys.argv[2]) if len(sys.argv) > 2 else int(input("Введите тему: "))
        if quiz == 1:
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for fruit in fruits_arr:
                print(fruit, end=' ')
                input()
            print("А теперь викторина. Удачи!")
            for fruit, translation in zip(fruits_quiz, fruits_arr):
                options = [translation.split(" - ")[0]]  # Правильный ответ
                while len(options) < 3:
                    random_word = random.choice(fruits_arr).split(" - ")[0]
                    if random_word not in options and random_word != fruit:
                        options.append(random_word)
                random.shuffle(options)
                print("--", fruit)
                for i, option in enumerate(options):
                    print(i + 1, "-", option)
                while True:
                    try:
                        answer = int(input("Ваш ответ: "))
                        if 1 <= answer <= len(options):
                            if options[answer - 1] == translation.split(" - ")[0]:
                                print("Правильно\n")
                                break
                            else:
                                print("Ошибка. Попробуйте еще раз")
                        else:
                            print("Некорректный ввод. Введите число от 1 до", len(options))
                    except ValueError:
                        print("Некорректный ввод. Введите число от 1 до", len(options))
        elif quiz == 2:
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for vegetable in vegetables_arr:
                print(vegetable, end=' ')
                input()
            print("А теперь викторина. Удачи!")
            for vegetable, translation in zip(vegetables_quiz, vegetables_arr):
                options = [translation.split(" - ")[0]] # Правильный ответ
                while len(options) < 3:
                    random_word = random.choice(vegetables_arr).split(" - ")[0]
                    if random_word not in options and random_word != vegetable:
                        options.append(random_word)
                random.shuffle(options)
                print("--", vegetable)
                for i, option in enumerate(options):
                    print(i + 1, "-", option)
                while True:
                    try:
                        answer = int(input("Ваш ответ: "))
                        if 1 <= answer <= len(options):
                            if options[answer - 1] == translation.split(" - ")[0]:
                                print("Правильно\n")
                                break
                            else:
                                print("Ошибка. Попробуйте еще раз")
                        else:
                            print("Некорректный ввод. Введите число от 1 до", len(options))
                    except ValueError:
                        print("Некорректный ввод. Введите число от 1 до", len(options))
    elif option == 2:
        print("1 - Фрукты")
        print("2 - Овощи")
        quiz_write = int(sys.argv[2]) if len(sys.argv) > 2 else int(input("Введите тему: "))
        if quiz_write == 1:
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for fruit in fruits_arr:
                print(fruit, end=' ')
                input()
            print("А теперь письменное закрепление материала. Удачи!")
            for translation in fruits_arr:
                korean_word, russian_word = translation.split(" - ")
                while True:
                    user_input = input(russian_word + " - ")
                    if user_input.lower() == korean_word:
                        print("Правильно")
                        break
                    else:
                        print("Неправильно. Попробуйте еще раз")
        elif quiz_write == 2:
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for vegetable in vegetables_arr:
                print(vegetable, end=' ')
                input()
            print("А теперь письменное закрепление материала. Удачи!")
            for translation in vegetables_arr:
                korean_word, russian_word = translation.split(" - ")
                while True:
                    user_input = input(russian_word + " - ")
                    if user_input.lower() == korean_word:
                        print("Правильно")
                        break
                    else:
                        print("Неправильно. Попробуйте еще раз")
    else:
        print("Вы ввели неверный вариант")

if __name__ == "__main__":
    main()