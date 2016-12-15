#w canvasie narysuj choinke, przystroj,
from Tkinter import *
root=Tk()
root.title("choinka")

canvas=Canvas(root,width=400,height=600,bg='white')
canvas.pack(expand=YES,fill=BOTH)
'''
canvas.create_line(100,100,200,200)
canvas.create_line(100,200,200,300)
'''
list=[]

for i in range (1,10,2):
    list.append((200-((i-1)*10),i*40))
    list.append((100-(10*i),100+i*40))
    list.append((100-(10*i),100+i*40))
    list.append((200-(((i+2)-1)*10),(i+2)*40))

list.append((100,440))
list.append((100+60,440-13))
list.append((100+60,440-13))
list.append((300-59,440-13))
list.append((300-60,440-13))
list.append((300,440))

for i in range (9,-1,-2):
    list.append((200+((i-1)*10),i*40))
    list.append((300+(10*i),100+i*40))
    list.append((300+(10*i),100+i*40))
    list.append((200+(((i+2)-1)*10),(i+2)*40))

canvas.create_polygon(list,fill="green")

#canvas.create_polygon()
canvas.create_rectangle(160,430,240,583,width=10,fill="brown",outline="brown")

rg=[(240,170),(190,130),(140,90),(240,90),(140,170),(240,370),(190,330),(140,290),(240,290),(140,370),(110,250),(190,220),(270,250),(90,400),(290,400),(100,320),(280,320)]
lst=[(200,50-20),(205,60-20),(215,65-20),(205,70-20),(200,80-20),(200,50-20),(195,60-20),(185,65-20),(195,70-20),(200,80-20)]
canvas.create_polygon(lst,fill="yellow",width=1,outline="black")

for i in rg:
    canvas.create_oval(i[0],i[1],i[0]+20,i[1]+20,width=1,fill='yellow')

'''
canvas.create_oval(10,10,300,300,width=2,fill='yellow')
canvas.create_arc(100,200,300,100,fill='green')
canvas.create_rectangle(50,200,300,300,width=10,fill="#8f8fff")
canvas.create_line(600,300,150,150,width=10,fill='red')
photo=PhotoImage(file='SKETLON.gif')
canvas.create_image(50,300,image=photo,anchor=NW)
widget=Label(canvas,text=u"Ko\u0142o",fg='white',bg="black")
widget.pack()
canvas.create_window(100,100,window=widget)
canvas.create_text(100,280,text=u"prostok\u0105t)
'''
root.mainloop()