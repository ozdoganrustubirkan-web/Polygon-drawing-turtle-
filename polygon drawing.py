import turtle
import time

Gen = input("(Limit 100!) Enter the number of sides (Gen): ")
uzunluk = (int(((100-int(Gen))+2)/5))
derece = (180 - (((int(Gen)-2)*180)/int(Gen)))
turtle.Turtle()
ekran = turtle.Screen()
ekran._root.attributes('-topmost', True)
for _ in range(int(Gen)):
 turtle.forward(uzunluk)
 turtle.left(derece)


time.sleep(2)
turtle.bye()