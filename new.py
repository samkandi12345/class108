import random 
import plotly.express as pe
import plotly.figure_factory as pff

count = []
dice_result = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

figure = pff.create_distplot([dice_result],["result"],show_hist=False)
figure.show()


