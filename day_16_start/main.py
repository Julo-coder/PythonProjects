# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkCyan", "coral")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)
table.align = "l"
print(table)

