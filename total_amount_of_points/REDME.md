# Total amound of points

Nuestro equipo de fútbol ha terminado el campeonato.
Los resultados de los partidos de nuestro equipo se registran en una colección de cadenas. Cada partido está representado por una cadena en el formato "x:y", donde x está el puntaje de nuestro equipo y el puntaje de ynuestros oponentes.
Por ejemplo: ["3:1", "2:2", "0:1", ...]

Los puntos se otorgan por cada partido de la siguiente manera:
si x > y: 3 puntos (ganar)
si x < y: 0 puntos (pérdida)
si x = y: 1 punto (empate)

Necesitamos escribir una función que tome esta colección y devuelva la cantidad de puntos que nuestro equipo (x) obtuvo en el campeonato según las reglas dadas anteriormente.

Notas:
```
Nuestro equipo siempre juega 10 partidos en el campeonato
0 <= x <= 4
0 <= y <= 4
```

[Enlace CodeWars](https://www.codewars.com/kata/5bb904724c47249b10000131/train/python)