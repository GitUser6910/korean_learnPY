import random

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

def quiz(words, quiz_words):
    random.shuffle(words)
    for russian_word in quiz_words:
        korean_word = [word.split(" - ")[0] for word in words if russian_word in word][0]
        options = [korean_word]
        while len(options) < 3:
            random_word = random.choice(words).split(" - ")[0]
            if random_word != korean_word and random_word not in options:
                options.append(random_word)
        random.shuffle(options)
        print(f"--{russian_word}")
        for i, option in enumerate(options, 1):
            print(f"{i} - {option}")
        while True:
            answer = input("Ваш ответ: ")
            try:
                answer_index = int(answer) - 1
                if 0 <= answer_index < len(options):
                    if options[answer_index] == korean_word:
                        print("Правильно\n")
                        break
                    else:
                        print("Ошибка. Попробуйте еще раз")
                else:
                    print(f"Некорректный ввод. Введите число от 1 до {len(options)}")
            except ValueError:
                print(f"Некорректный ввод. Введите число от 1 до {len(options)}")

def write_practice(words):
    for word in words:
        korean_word, russian_word = word.split(" - ")
        while True:
            user_input = input(f"{russian_word} - ")
            if user_input.lower() == korean_word.lower():
                print("Правильно")
                break
            else:
                print("Неправильно. Попробуйте еще раз")

def main():
    print("Корейский язык")
    print("--------------")
    print("1 - Викторина")
    print("2 - Тренеровка письма")
    option = input("--Введите вариант: ")
    if option == "1":
        print("1 - Фрукты")
        print("2 - Овощи")
        quiz_option = input("Введите тему: ")
        if quiz_option == "1":
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for word in fruits_arr:
                print(word, end='')
                input()
            print("А теперь викторина. Удачи!")
            quiz(fruits_arr, fruits_quiz)
        elif quiz_option == "2":
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for word in vegetables_arr:
                print(word, end='')
                input()
            print("А теперь викторина. Удачи!")
            quiz(vegetables_arr, vegetables_quiz)
    elif option == "2":
        print("1 - Фрукты")
        print("2 - Овощи")
        quiz_option = input("Введите тему: ")
        if quiz_option == "1":
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for word in fruits_arr:
                print(word, end='')
                input()
            print("А теперь письменное закрепление материала. Удачи!")
            write_practice(fruits_arr)
        elif quiz_option == "2":
            print("Нажимайте 'Enter' после каждого слова если вы его запомнили")
            for word in vegetables_arr:
                print(word, end='')
                input()
            print("А теперь письменное закрепление материала. Удачи!")
            write_practice(vegetables_arr)
    else:
        print("Вы ввели неверный вариант")

if __name__ == "__main__":
    main()