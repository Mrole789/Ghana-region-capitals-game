from turtle import Screen, Turtle
import pandas

turtle = Turtle()
screen = Screen()
screen.setup(width=800, height=700)
screen.title("Ghana Regions and Their Capital Cities Game")

img = "ghana_map.gif"
screen.addshape(img)
turtle.shape(img)
turtle.shapesize(10,10,10)

gh_rnc = pandas.read_csv("16_regions_and_capitals.csv")

# For finding cordinates for regions by clicking on turtle screen
# def get_mouse_click_cor(x, y):
#     print(x, y)
# 
# screen.onscreenclick(get_mouse_click_cor)

# screen.mainloop() # for keeping turtle running after clicking the turtle screen

jon = Turtle()
jon.penup()
jon.hideturtle()

correct_answers = 1
regions_guessed = ["Accra"]

game_on = True
while game_on:

    answer = screen.textinput(title=f"{correct_answers}/32 correct", prompt="What is another region or city name?")
    
    #if the user types 'exit' the game ends and console shows regions or cities you missed
    if answer.lower() == "exit":
        print("\nRegions or cities you missed:\n")
        for x in gh_rnc.state:
            if x not in regions_guessed:
                print(x)
        break
    
    xcor = 0
    ycor = 0
    
    for x in gh_rnc.state:
        if answer.lower() == x.lower():
            
            #to make sure a region or city repeated is not counted or written again
            if x not in regions_guessed:
                regions_guessed.append(x)
    
                correct_answers += 1
                xcor = int(gh_rnc.x[gh_rnc.state == x])
                ycor = int(gh_rnc.y[gh_rnc.state == x])
                
                jon.goto(xcor,ycor)
                
                #determinining the font size to use for either the region or city
                ptype = gh_rnc.rc[gh_rnc.state == x].item()
                
                if ptype == "reg":
                    fontx = ('Times New Roman',12,'bold')
                else:
                    fontx = ('Times New Roman',10,'bold')
                    
                jon.write(f'{x}', font=fontx)
                if correct_answers == 32:
                    game_on = False

screen.exitonclick()