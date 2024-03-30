import turtle

''' 
╭─╮ ┬┈┬ ╭╮╭ ╭─╮ ┬─╮ ┈ ╭╮┈ ┬┈┬ ┈ ╭─╮ ╭─╮ ╭┬╮ ┬┈┬ 
│┈│ │││ │││ ├┤┈ ├┬╯ ┈ ├┴╮ ╰┬╯ ┈ ╰─╮ ├┤┈ ┈│┈ ├─┤  
╰─╯ ╰┴╯ ╯╰╯ ╰─╯ ┴╰─ ┈ ╰─╯ ┈┴┈ ┈ ╰─╯ ╰─╯ ┈┴┈ ┴┈┴  

              '''

Sl=turtle.getscreen()
S=turtle.Turtle()
turtle.bgcolor('black')
S.speed('fastest')

J=S.clone()
L=J.clone()
K=L.clone()

S.color('white','black')
J.color('black','black')
L.color('white','black')
K.color('black','black')



def Sl(n=50):
    while n<=300:
        S.circle(n)
        n=n+12
def Jk(n=40):
    while n<=250:
        J.circle(n)
        n=n+10
def Ls(n=30):
    while n<=200:
        L.circle(n)
        n=n+8
def Kj(n=25):
    while n<=150:
        K.circle(n)
        n=n+6     
    
    
for call in range(8):
    Sl()
    S.rt(45)
for call in range(8):
    Jk()
    J.rt(45)
for call in range(8):
    Ls()
    L.rt(45)
for call in range(8):
    Kj()
    K.rt(45)
    