# ie-72-kr
import random

def get_user_choice():
    user_input = input("Выберите (к, н, б): ").lower()
    while user_input not in ['к', 'н', 'б']:
        print("Неверный ввод. Пожалуйста, выберите к, н или б.")
        user_input = input("Выберите (к, н, б): ").lower()
    return user_input

def get_computer_choice():
    choices = ['к', 'н', 'б']
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'к' and computer_choice == 'н') or \
            (user_choice == 'н' and computer_choice == 'б') or \
            (user_choice == 'б' and computer_choice == 'к'):
        return "Вы выиграли!"
    else:
        return "Комп выиграл!"

def play_game():
    print("Добро пожаловать в игру 'К, Н, Б'!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Вы выбрали: {user_choice}")
    print(f"Комп выбрал: {computer_choice}")

    result = winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
