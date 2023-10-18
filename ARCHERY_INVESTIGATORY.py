## @author: Akanksha and Ankur

import turtle,time,random

# STARTING PAGE

wn = turtle.Screen()
wn.clearscreen()
wn.bgcolor('Sky Blue')
heading = ' >>>---ARCHERY-GAME----> '
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('maroon')
pen.goto(-750, 0)
pen.write(heading, False, align = 'left', font = ('Lucida Calligraphy', 65, 'bold', 'italic'))

logo_g = turtle.Turtle()
logo_g.penup()
logo_g.shape('circle')
logo_g.color('green')
logo_g.hideturtle()
logo_g.shapesize(10, 10)
logo_g.goto(0, -200)
logo_g.showturtle()

logo_b = turtle.Turtle()
logo_b.penup()
logo_b.shape('circle')
logo_b.color('blue')
logo_b.hideturtle()
logo_b.shapesize(7, 7)
logo_b.goto(0, -200)
logo_b.showturtle()

logo_r = turtle.Turtle()
logo_r.penup()
logo_r.shape('circle')
logo_r.color('red')
logo_r.hideturtle()
logo_r.shapesize(4, 4)
logo_r.goto(0, -200)
logo_r.showturtle()

time.sleep (10)

# INSTRUCTIONS 

wn = turtle.Screen()
wn.clearscreen()
wn.bgcolor('lavender')

heading = ' ~~~~~  GAME INSTRUCTONS  ~~~~~ '
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('chocolate')
pen.goto(-600, 300)
pen.write(heading, False, align = 'left', font = ('papyrus', 45, 'bold'))

instructions = ''' Hit the arrow to the target board according to the wind-speed to get a \n
                BULL'S EYE !! \n
-> You will get 5 Arrows.\n
-> Press 8 : To move up\n
-> Press 2 : To move down\n
-> Click any botton : To Shoot! '''

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('indigo')
pen.goto(-600, -150)
pen.write(instructions, False, align = 'left', font = ('Felix Titling', 20, 'bold'))

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('red')
pen.goto(-600, -250)
pen.write('PLEASE  ENTER  YOUR  NAME  IN  THE  CONSOLE  TO  START  THE  GAME',\
          False, align = 'left', font = ('Felix Titling', 25, 'underline'))

time.sleep(20)
wn.clearscreen()

with open ('archery_score_history.txt','r') as scorehistory:
    print (scorehistory.read(),'\n')
with open ('archery_hiscores.txt','r') as hiscorers:
    print (hiscorers.read(),'\n')

name = input('Please enter your name: ')
time.sleep(5)

points = 0
for chance in range(1,6):
    wn = turtle.Screen()
    wn.clearscreen()
    wn.bgcolor('lavender')
    
    # Arrow
    arrow = turtle.Turtle()
    arrow.speed(0)
    arrow.penup()
    arrow.hideturtle()
    arrow.shapesize(2,6)
    arrow.goto(450,0)
    arrow.showturtle()
    arrow.left(180)
    
    # TARGET BOARD
    
    # 100 Points
    mid = turtle.Turtle()
    mid.speed(0)
    mid.hideturtle()
    mid.penup()
    mid.shape('square')
    mid.shapesize(2,1)
    mid.color('red')
    mid.goto(-500,0)
    mid.showturtle()
    
    # 50 Points
    
    # Right
    side = turtle.Turtle()
    side.speed(0)
    side.hideturtle()
    side.penup()
    side.shape('square')
    side.shapesize(2,1)
    side.color('blue')
    side.goto(-500,40)
    side.showturtle()
    
    # Left
    side2 = turtle.Turtle()
    side2.speed(0)
    side2.hideturtle()
    side2.penup()
    side2.shape('square')
    side2.shapesize(2,1)
    side2.color('blue')
    side2.goto(-500,-40)
    side2.showturtle()
    
    # 10 Points
    
    # Right
    last = turtle.Turtle()
    last.speed(0)
    last.hideturtle()
    last.penup()
    last.shape('square')
    last.shapesize(2,1)
    last.color('green')
    last.goto(-500,83)
    last.showturtle()
    
    # Left
    last2 = turtle.Turtle()
    last2.speed(0)
    last2.hideturtle()
    last2.penup()
    last2.shape('square')
    last2.shapesize(2,1)
    last2.color('green')
    last2.goto(-500,-83)
    last2.showturtle()
    
    # Points
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color('black')
    # 100
    pen.goto(-570,-23)
    pen.write('100',False,align = 'left',font = ('Lucida',25,'normal'))
    # 50
    pen.goto(-550,15)
    pen.write('50',False,align = 'left',font = ('Lucida',25,'normal'))
    # 50
    pen.goto(-550,-60)
    pen.write('50',False,align = 'left',font = ('Lucida',25,'normal'))
    # 10
    pen.goto(-550,60)
    pen.write('10',False,align = 'left',font = ('Lucida',25,'normal'))
    # 10
    pen.goto(-550,-100)
    pen.write('10',False,align = 'left',font = ('Lucida',25,'normal'))
    
    #chances
    word = 'ARROW -  ' + str(chance) + '  LOADED'
    pen.color('navy blue')
    pen.goto(-220,-300)
    pen.write(word,False,align = 'left',font = ('Arial',30,'underline'))
    
    if chance == 1:
        a = turtle.Turtle()
        a.speed(0)
        a.penup()
        a.hideturtle()
        a.shapesize(2,6)
        a.goto(-95,-320)
        a.showturtle()
        a.left(90)
        
        a2 = turtle.Turtle()
        a2.speed(0)
        a2.penup()
        a2.hideturtle()
        a2.shapesize(2,6)
        a2.goto(-65,-320)
        a2.showturtle()
        a2.left(90)
        
        a3 = turtle.Turtle()
        a3.speed(0)
        a3.penup()
        a3.hideturtle()
        a3.shapesize(2,6)
        a3.goto(-35,-320)
        a3.showturtle()
        a3.left(90)
        
        a4 = turtle.Turtle()
        a4.speed(0)
        a4.penup()
        a4.hideturtle()
        a4.shapesize(2,6)
        a4.goto(-5,-320)
        a4.showturtle()
        a4.left(90)
    
    if chance == 2:
        a = turtle.Turtle()
        a.speed(0)
        a.penup()
        a.hideturtle()
        a.shapesize(2,6)
        a.goto(-95,-320)
        a.showturtle()
        a.left(90)
        
        a2 = turtle.Turtle()
        a2.speed(0)
        a2.penup()
        a2.hideturtle()
        a2.shapesize(2,6)
        a2.goto(-65,-320)
        a2.showturtle()
        a2.left(90)
        
        a3 = turtle.Turtle()
        a3.speed(0)
        a3.penup()
        a3.hideturtle()
        a3.shapesize(2,6)
        a3.goto(-35,-320)
        a3.showturtle()
        a3.left(90)

    if chance == 3:
        a = turtle.Turtle()
        a.speed(0)
        a.penup()
        a.hideturtle()
        a.shapesize(2,6)
        a.goto(-95,-320)
        a.showturtle()
        a.left(90)
        
        a2 = turtle.Turtle()
        a2.penup()
        a2.hideturtle()
        a2.shapesize(2,6)
        a2.goto(-65,-320)
        a2.showturtle()
        a2.left(90)
        
    if chance == 4:
        a = turtle.Turtle()
        a.speed(0)
        a.penup()
        a.hideturtle()
        a.shapesize(2,6)
        a.goto(-95,-320)
        a.showturtle()
        a.left(90)
        
    if chance == 5:
        a = turtle.Turtle()
        a.speed(0)
        a.penup()
        a.hideturtle()
        a.goto(-170,-360)
        a.write('LAST ARROW!',False,align = 'left',font = ('Arial',30,'normal'))

    # Wind Speed
    
    wndspd = random.randint(1,10)
    wndspd /= 10
    select = random.randint(1,2)    
    pen.goto(-200,250)
    pen.color('blue')
    string = 'WIND SPEED:  ' + str(int(wndspd*10))
    pen.write(string,False,align = 'left',font = ('Felix Titling',30,'italic'))
    
    arrow1 = turtle.Turtle()
    arrow1.speed(0)
    arrow1.penup()
    arrow1.shape('arrow')
    arrow1.color('blue')
    arrow1.hideturtle()
    arrow1.shapesize(1.5,4)
    arrow1.goto(150,270)
    arrow1.showturtle()
    if select == 1:
        arrow1.right(90)
    else:
        arrow1.left(90)
    
    # Start
    def up():
        global arrow
        if arrow.ycor() < 300:
            arrow.sety(arrow.ycor() + 12.345)
    def down():
        global arrow
        if arrow.ycor() > -300:
            arrow.sety(arrow.ycor() - 12.345)
    def shoot():
        global shooted
        shooted = True
    def none():
        pass
    
    shooted = False
    while True:
        if not shooted:
            wn.update()
            wn.listen()
            wn.onkey(up,'8')
            wn.onkey(down,'2')
            wn.onkey(shoot,' ')
        else:
            wn.listen()
            wn.onkey(none,'8')
            wn.onkey(none,'2')
            wn.onkey(none,' ')
            break
    
    for repeat in range(950//10):
        wn.update()
        if select == 1:
            arrow.goto(arrow.xcor() - 10, arrow.ycor() - wndspd * 2) 
        else:
            arrow.goto(arrow.xcor() - 10, arrow.ycor() + wndspd * 2) 
    
    dis = {}
    dis ['mid'] = arrow.distance(mid)
    dis ['side'] = arrow.distance(side)
    dis ['side2'] = arrow.distance(side2)
    dis ['last'] = arrow.distance(last)
    dis ['last2'] = arrow.distance(last2)
    maxi = 0
    a = 0
    for key in dis:
        if dis[key] > maxi:
            maxi = dis[key]
            a = key
            
    if a == 'mid':
        maxi = arrow.distance(mid)
    if a == 'side':
        maxi = arrow.distance(side)
    if a == 'side2':
        maxi = arrow.distance(side2)
    if a == 'last':
        maxi = arrow.distance(last)
    if a == 'last2':
        maxi = arrow.distance(last2)
    for key in dis:
          if dis[key] < maxi:
              maxi = dis[key]
              pts = key
              
    pen.goto(-200,0)
    if  arrow.ycor() < 103 and arrow.ycor() > -103:
        size = 50
        if pts == 'mid':
            points += 100
            pen.setx(-400)
            pen.color('brown')
            pts = "100 POINTS!! BULL'S EYE!"
            
        elif pts == 'side' or pts == 'side2':
            points += 50
            pen.color('chocolate')
            pts = '50 POINTS!'
            
        elif pts == 'last' or pts == 'last2':
            points += 10
            pen.color('orange')
            pts = '10 POINTS'
            
        pen.write(pts,False,align = 'left',font = ('Lucida',size,'normal'))
        
    else:
        pen.color('red')
        pen.write("MISS! :'(",False,align = 'left',font = ('Lucida',85,'normal'))
    time.sleep(3)

wn.clearscreen()
wn = turtle.Screen()
wn.bgcolor('lavender')

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('purple')
pen.goto(-520,0)
pen.write('GAME FINISHED',False,align = 'left',font = ('Comic Sans ITC',100,'italic'))
pen.goto(-640,-80)
pts =' --- '+ str(points) + '/500 (' + str((points / 500) * 100) + '%) ACCURACY ---'
pen.write(pts,False,align = 'Left',font = ('Lucida Calligraphy',50,'normal'))

if points == 500:
    high = turtle.Turtle()
    high.hideturtle()
    high.penup()
    high.color('red')
    high.goto(-450,-250)
    high.write('HIGH SCORE !!!',False,align = 'left',font = ('Eras Demi ITC',80,'normal'))
time.sleep(5)

data = open('archery_score_history.txt','a+')
record = '\n' + name + ' - ' + str (points)
data.write(record)
data.close()

hiscorers = open ('archery_hiscores.txt', 'a+')
if points == 500:
    player = '\n' + name
    hiscorers.write(player)
hiscorers.close ()
    
    
    
    
