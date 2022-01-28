'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''
lista = []
legrovidebb = []
def rovid(szo1, szo2, szo3):
  lista.append(szo1)
  lista.append(szo2)
  lista.append(szo3)
  if len(szo1) < len(szo2):
    legrovidebb.append(szo1)
  else:
    legrovidebb.append(szo2)
  if len(szo3) < len(legrovidebb[0]):
    legrovidebb.clear()
    legrovidebb.append(szo3)
  print(f"A legrövidebb szó: {legrovidebb} ")


rovid("asdasa", "asds", "aasdaasdasds")


