#Напишите функцию inimesed(), при запуске которой происходит заполнение двух списков: люди[], рост[]. Количество элементов в списках ограничивается пользователем (либо оговаривается сколько людей надо опросить, либо в режиме online- данные вносятся пока не закончатся данные о людях).
#После заполнения массивов появляется меню с выбором действий:
#•1 Удалить из списка человека и данные о его росте, введя имя человека;
#•2 Отобразить в алфавитном порядке список людей и их рост;
#•3 Найти самого высокого и самого низкого из людей;
#•4 Найти средний рост n первых людей в списке ;
#•5 Свой вариант.
#Для описания действий создайте необходимые функции.
from modul import *
growth = []
people = []


num_people = int(input("Enter number of people to be interviewed (or enter 0 for online mode): "))
if num_people == 0:
    while True:
        person = input("Enter the name of the person (or enter 'done' to exit): ")
        if person == 'done':
            break
        height = float(input("Enter the height of the person (in meters): "))
        people.append(person)
        growth.append(height)
else:
    for i in range(num_people):
        person = input("Enter the name of the person: ")
        height = float(input("Enter the height of the person (in meters): "))
        people.append(person)
        growth.append(height)
        print(growth)
        print(people)


while True:
        print("What do you want to do with the data?")
        print("1. Remove a person from the list")
        print("2. Display the list of people in alphabetical order")
        print("3. Find the highest and lowest height of people")
        print("4. Find the average height of the first n people in the list")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            person = input("Enter the name of the person to be removed: ")
            try:
                index = people.index(person)
                del people[index]
                del growth[index]
                print(f"{person} has been removed from the list.")
            except ValueError:
                print(f"{person} was not found in the list.")
            print(growth)
            print(people)
        elif choice == 2:
            people_growth = zip(people, growth)
            people_growth = sorted(people_growth, key=lambda x: x[0])
            people, growth = zip(*people_growth)
            print("List of people in alphabetical order:")
            for i in range(len(people)):
                print(f"{people[i]}: {growth[i]} meters")
        elif choice == 3:
            print(f"The highest height is {max(growth)} meters and belongs to {people[growth.index(max(growth))]}")
            print(f"The lowest height is {min(growth)} meters and belongs to {people[growth.index(min(growth))]}")
        elif choice == 4:
            n = int(input("Enter the value of n: "))
            if n > len(people):
                print("Invalid value of n.")
                continue
            avg = sum(growth[:n])/n
            print(f"The average height of the first {n} people is {avg} meters.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

