print('''
LearntFrom : https://www.youtube.com/watch?v=mNqPLIM90ts
------------------------------------------------------------

Copyright(C), 2022
-------------------
Writer: Bishal jaiswal
PublishedDate: Wednesday, September 28, 2022

''')

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from PIL import ImageGrab
from tkinter import filedialog
from os import getcwd,chdir

root = Tk()
root.geometry("1050x570+150+50")
root.iconbitmap("logo.ico")
root.config(bg="#f2f3f5")
root.resizable(FALSE,FALSE)
root.title("White Board")

lasx,lasy = 0,0
color = 'black'

# functions
def getXY(event):
    global lasx,lasy
    lasx,lasy = event.x,event.y

def drawLine(event):
    global lasx,lasy
    canvas.create_line((lasx,lasy,event.x,event.y),fill=color,capstyle=ROUND,smooth=TRUE,width=lineWidth.get())
    lasx,lasy = event.x,event.y

def selectColor(newColor):
    global color
    color = newColor

def erase():
    canvas.delete('all')
    displayPallet()


# canvas
canvas = Canvas(root,bg="white",width=930,height=500,cursor="hand2")
canvas.place(x=100,y=10)


def loadImage(name:str):
    photo = ImageTk.PhotoImage(Image.open(name))
    return photo

# downloadCanvas
def downloadImage():
    try:
        x=root.winfo_rootx()+canvas.winfo_x()
        # print(x)
        y=root.winfo_rooty()+canvas.winfo_y()
        # print(y)
        x1=x+canvas.winfo_width()
        # print(x1)
        y1=y+canvas.winfo_height()
        # print(y1)

        path = filedialog.asksaveasfilename(initialdir=getcwd(),initialfile="*.jpg",filetypes=(("JPG Files","*.jpg"),("PNG Files","*.png")))
        ImageGrab.grab().crop((x,y,x1,y1)).save(path)

    except:
        pass


image = Image.open("download.png")
photo = ImageTk.PhotoImage(image=image)
image = image.resize((5,5))

download = ttk.Button(root,image=photo,command = downloadImage)
download.place(x = 992,y = 520)

def uploadImage():
    fileName = filedialog.askopenfilename(filetypes=[("PNG Files","*.png"),("JPG Files","*.jpg")])

    try:
        img = Image.open(fileName)
        selectedImage = ImageTk.PhotoImage(img)
        canvas.create_image(0,0,image = selectedImage,anchor = NW)
        canvas.image = selectedImage
    except:
        pass

image1 = Image.open("upload.png")
photo1 = ImageTk.PhotoImage(image=image1)
image1 = image1.resize((5,5))

upload = ttk.Button(root,image=photo1,command = uploadImage)
upload.place(x = 930,y = 520)

# colorSection
sectionImage = loadImage("color section.png")
colorSection = Label(root,image=sectionImage,bg="#f2f3f5")
colorSection.place(x=20,y=30)

# canvasForColorSection
cScanvas = Canvas(root,height=350,width=38)
cScanvas.place(x=40,y=80)


# colorsInCanvas
def displayPallet():
    id = cScanvas.create_rectangle((10,10,30,30),fill="black")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('black'))

    id = cScanvas.create_rectangle((10,40,30,60),fill="gray")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('gray'))

    id = cScanvas.create_rectangle((10,70,30,90),fill="brown4")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('brown4'))

    id = cScanvas.create_rectangle((10,120,30,100),fill="red")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('red'))

    id = cScanvas.create_rectangle((10,130,30,150),fill="orange")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('orange'))
    
    id = cScanvas.create_rectangle((10,160,30,180),fill="yellow")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('yellow'))

    id = cScanvas.create_rectangle((10,190,30,210),fill="blue")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('blue'))

    id = cScanvas.create_rectangle((10,220,30,240),fill="purple")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('purple'))

    id = cScanvas.create_rectangle((10,250,30,270),fill="#ffafcc")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('#ffafcc'))

    id = cScanvas.create_rectangle((10,280,30,300),fill="#0096c7")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('#0096c7'))

    id = cScanvas.create_rectangle((10,310,30,330),fill="#fed9b7")
    cScanvas.tag_bind(id,"<Button-1>",lambda x:selectColor('#fed9b7'))

    
displayPallet()

canvas.bind("<Button-1>",getXY)
canvas.bind("<B1-Motion>",drawLine)


# eraserButton
eraserImage = loadImage("eraser.png")
eraser = ttk.Button(root,image=eraserImage,width=20,command=erase)
eraser.place(x=40,y=450)


# scaleToControllLineWidth
def showScaleNum(event):
    lineWidthNum.config(text=f"{lineWidth.get()}")    

lineWidth = IntVar()
scale = ttk.Scale(root,from_=1,to=20,variable=lineWidth)
scale.place(x=50,y=520)

# displayingThe lineWidth choosen
lineWidthNum = ttk.Label(root,text="1")
lineWidthNum.place(x=90,y=550)
scale.bind("<B1-Motion>",showScaleNum)  # updating while changing

root.mainloop()
