import random

correct_answers = 0
user_input = input("Введите ваше имя: ")


def normal_words(words):
    """
    Создаёт список слов из документа
    """
    list_of_words = []
    with open(words, "rt", encoding="utf-8") as words_:
        for word_ in words_:
            list_of_words.append(word_.strip())
        return list_of_words


def shuffled_words(words):
    """
    Создаёт список перемешанных слов
    """
    list_of_shuffled_words = []
    with open(words, "rt", encoding="utf-8") as words:
        for word in words:
            list_of_letters = [letter for letter in word.strip()]
            random.shuffle(list_of_letters)
            joined_word = "".join(list_of_letters)
            list_of_shuffled_words.append(joined_word)
        return list_of_shuffled_words


def users_data(users_information):
    """
    Получает список результатов
    """
    with open(users_information, "rt", encoding="utf-8") as results:
        scores = []
        for result in results:
            player, score = result.strip().split(":")
            scores.append(int(score))
        return scores


normal_words_ = normal_words("words.txt")
shuffled_words_ = shuffled_words("words.txt")

for secret_index in range(len(normal_words_)):
    print(f"Угадайте слово: {shuffled_words_[secret_index]}")
    user_attempt = input()
    if user_attempt == normal_words_[secret_index]:
        print("Верно! Вы получаете 10 очков")
        correct_answers += 10
    else:
        print(f"Неверно! Верный ответ – {normal_words_[secret_index]}")

# Создаёт документ, в котором записываются имена тестируемых и их результаты
with open("history.txt", "a", encoding="utf-8") as user_name:
    user_name.write(f"{user_input} : {correct_answers}\n")

total_games = len(users_data("history.txt"))
max_score = max(users_data("history.txt"))

print(f"Всего игр сыграно: {total_games}")
print(f"Максимальный рекорд: {max_score}")
