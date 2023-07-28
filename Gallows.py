#приветсвие
#повтор
#файл
#рисунок виселицы
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
  "|  / \n"
  "|   \n"
"=========\n"
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
        words = f.readlines()
        
  return words
def draw_hugman(index: int):
  'выводи виселицу поэтапно'
  
  print(people[index])
def play(source_word: str, word: str):
  print(source_word)
  mistake=0
  while mistake < 7 or source_word==word:
    char=input("Введите предполагаему букву:")
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
    print(source_word)


if start_hungman() == 'Да':
    words=open_words()
    word = choice(words).replace('\n', '')
    source_word = (len(word)) * '*'
    play(source_word, word)
