e=0 #вода
f=False
r=0 #огонь
w=0 #земля
t=0 #воздух
m=0 #хаос
c=0 #порядок
n=0 #население
def setup():
    
    size(1400,800)
def draw():
    background(70)
    rect( 40,30,90,90)
    rect(200,30,120,90)
    rect(360,30,90,90)
    rect(490,30,90,90)
    rect(670,30,90,90)
    rect(900,30,90,90)
    rect(1100,30,90,90)
    text(n,670,15)
    text(e,40,15)
    text(r,200,15)
    text(w,360,15)
    text(t,490,15)
    text(m,900,15)
    text(c,1100,15)
    textSize(20)
    text(u"планета:",300,400)
    text(u"состояние:",300,500)
    text(u"население:",300,600)
    if e>5 and e<20 and w>30 and w<40 and t>30 and t<40:
        circle(800,500,30)
        text(u"Сатурн",400,400)
    if e==0 and r>30 and r<40 and w>30 and w<50 and t==0:
        circle(800,500,30)
        text(u"Меркурий",400,400)
    if e>5 and e<15 and r>20 and r<50 and w==50 and t>10 and t<20:
        circle(800,500,30)
        text(u"Венера",400,400)
    if e>20 and e>35  and r>20 and r<25 and w>30 and w<50 and t>20 and t<30:
        circle(800,500,30)
        text(u"Земля",400,400)
    if e>1 and e<12 and r>10 and r<25 and w==0 and t>40 and t<60:
        circle(800,500,30)
        text(u"Юпитер",400,400)
    if e==0 and r>50 and r<90 and w>30 and w<50 and t==0:
        circle(800,500,30)
        text(u"Марс",400,400)
    if e>40 and e<60 and r==0 and w>5 and w<15 and t>20 and t<35:
        circle(800,500,30)
        text(u"Нептун",400,400)
    if e>40 and e<60 and r==0 and w>5 and w<15 and t>40 and t<50:
        circle(800,500,30)
        text(u"Уран",400,400)                                
    if m>c:
        rect(1000,600,40,30)
        text(u"Война",420,500)
    if c>m:
        rect(1000,600,40,30)
        text(u"Мир",420,500)
    if m==c and m>0 and c>0:
        rect(1000,600,40,30)
        text(u"Равновесие",420,500)
    if n>10 and n<15:
        text(u"Люди",420,600)
        rect(100,500,60,109)
    if n>20 and n<30:
        text(u"Эльфы",420,600)
        rect(100,500,60,109)
    if n>31 and n<41:
        text(u"Дроу",420,600)
        rect(100,500,60,109)
    if n>43 and n<50:
        text(u"Гномы",420,600)
        rect(100,500,60,109)
    if n>51 and n<61:
        text(u"Духи",420,600)
        rect(100,500,60,109)                    
def keyPressed():
    global e,r,w,t,m,c,n
    if keyCode == (UP):
        e+=1
    if keyCode == (LEFT):
        r+=1
    if keyCode == (RIGHT):
        w+=1
    if keyCode == (DOWN):
        t+=1
    if keyCode == (SHIFT):
        m+=1
    if keyCode == (ALT):
        n+=1      
def mouseClicked():
    global c
    if mouseButton == (LEFT):
        text(u"население",670,140)
        text(u"вода",40,140)
        text(u"огонь",200,140)
        text(u"земля",360,140)
        text(u"воздух",490,140)
    if mouseButton == (RIGHT):
        c+=1 
