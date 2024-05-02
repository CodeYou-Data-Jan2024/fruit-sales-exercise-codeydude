# add your code 
import pandas as pd

fruit = pd.fruit({"Apples": ["35", "41"],
                  "Bananas": ["21", "34"]},
                  index = ["2017 Sales", "2018 Sales"])
print(fruit)

fruit.to_csv("fruit.csv")

