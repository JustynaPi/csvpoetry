import random

list_a = []
list_b = []
list_c = []
list_d = []

with open("cpvpoetry.csv", "r") as f:
  for line in f:
      words = line.split(";")
      list_a.append(words[0])
      list_b.append(words[1])
      list_c.append(words[2].strip())
      list_d.append(words[3])

def poetry():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    word_d = random.choice(list_d)
    poem = 'W rękach dzieci ' + word_a + ' ' + 'a w ich oczach ' + word_b + ' '+ 'i ' + word_d + ' '+', żadnych szans na '+ word_c
    print(poem)

poetry()