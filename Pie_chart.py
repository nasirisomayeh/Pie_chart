# نمودار دایره ای

from cProfile import label
from turtle import color
import matplotlib.pyplot as nem 

teams = [10, 15, 20, 16, 5 , 25] #size

nem.pie(teams,labels=["A", "B", "C", "E", "F", "G"],
        colors=["pink", "red", "yellow","blue", "green", "orange"],
        explode=[0,0,0.2,0 , 0 ,0])

nem.show()