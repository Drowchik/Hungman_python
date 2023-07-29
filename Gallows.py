#приветсвие
#повтор
#файл
#рисунок виселицы

#проверки на цифры, на две буквы, l
from random import choice; import re


        
people=(
  "+---+\n"
  "|   |\n"
      "|\n"
      "|\n"
      "|\n"
      "|\n"
"=========\n",
  "+---+\n"
  "|   |\n"
  "|  ( )\n"
  "|   \n"
  "|   \n"
  "|   \n"
"=========\n",
"=========\n"
  "+---+\n"
  "|   |\n"
  "|  ( )\n"
  "|   |\n"
  "|   \n"
  "|   \n"
"=========\n",
"=========\n"
  "+---+\n"
  "|   |\n"
  "|  ( )\n"
  "|  \|\n"
  "|   \n"
  "|   \n"
"=========\n",
"=========\n"
  "+---+\n"
  "|   |\n"
  "|  ( )\n"
  "|  \|/\n"
  "|   \n"
  "|   \n"
"=========\n",
"=========\n"
  "+---+\n"
  "|   |\n"
  "|  ( )\n"
  "|  \|/\n"
  "|   |\n"
  "|  / \\\n"
  "|   \n"
"=========\n",
)
def start_hungman () -> str:
    'Приветствует пользователя при первом запуске'
    
    print('\033[1m' + " Добро пожаловать в Hungman!\n" + '\033[0m', "Хотите сыграть в игру?\n\n",
      "Правила достаточно просты: я загадываю слово, а ваша цель отгадать его по 1 букве.\nУ вас есть право на 6 ошибок.\n")
    start = input().title()
    
    return start
  
  
def open_words()->list:
  'Считывает зараняя подготовленные слова'
    
  with open('book.txt', 'r', encoding='utf-8') as f:
       return f.readlines()
    

         
def draw_hugman(index: int):
  'выводи виселицу поэтапно'
  
  print('-------------------------\n', people[index])
  
  
def check_used(char:str, used:list) ->list:
    while True:
      if char in used:
        char = input("Вы ввели некоректную букву или вы уже вводили её. Введите другую: ")
        continue
      if len(char)!=1:
        char = input("Вы ввели некоректную букву или вы уже вводили её. Введите другую: ")
        continue
      if ord(char)<1072 or ord(char)>1103:
        char = input("Вы ввели некоректную букву или вы уже вводили её. Введите другую: ")
        continue
      else:
        used.append(char)
        return used, char


def play(source_word: str, word: str):
  mistake = 0
  used = list()
  while mistake < 6 and source_word!=word:
    print('-------------------------\n', source_word, '\n-------------------------')
    print(f'Вы использовали данные буквы: {used}')
    char=input("Введите предполагаему букву: ").lower()
    used, char=check_used(char, used)
    if char in word:
      
      new_word = ''
      for i in range(len(word)):     
        if word[i] == char:
          new_word += word[i]
          
        else:
          new_word += source_word[i]
          
      source_word = new_word
      
    else:
      draw_hugman(mistake)
      mistake += 1
      
  if source_word==word:
    print(f"\nПоздравляю! Вы отгадали слово {word}")
  else:
    print(f"\nК сожалению, вы проиграли, но не отчаивайтесь!\nПопробуйте снова!\nБыло загадано слово: {word}")  

if start_hungman() == 'Да':
    words = open_words()
    word = choice(words).replace('\n', '')
    source_word = (len(word)) * '*'
    play(source_word, word)
