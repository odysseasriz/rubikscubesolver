import pyaudio
import numpy as np
import cv2
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from Tkinter import *
from PIL import Image
import time
import sys
import kociemba
import random
import tkMessageBox


def Camera_Activation():

        camera1 = cv2.VideoCapture(1)

        
        for i in xrange(30):
           temp = camera1.read()
        
        retval, camera_capture = camera1.read()

        file = "C:\Users\Odysseas\Desktop\test1.jpg"

        cv2.imwrite(file, camera_capture)

        camera1.release()

        
        im = np.array(Image.open("C:\Users\Odysseas\Desktop\test1.jpg"), dtype=np.uint8)

        fig,ax = plt.subplots(1)

        ax.imshow(im)

        plt.ion()

        plt.show()
       

        file = "/home/odysseas/Desktop/Coding/test1.jpg"
        img = cv2.imread(file)


        RGB1 = np.array([img[151,411],  # GREEN                  
        img[160,365],
        img[175,310],
        img[130,370],
        img[152,264],
        img[118,340],
        img[120,275],
        img[130,230],
        img[230,330],  # YELLOW
        img[210,380],
        img[195,425],
        img[285,320],
        img[250,420],
        img[345,315],
        img[325,365],
        img[330,390],
        img[165,197],
        img[195,235],  # ORANGE               
        img[220,280],
        img[225,195],
        img[280,275],
        img[290,180],
        img[310,230],
        img[340,270]])

        plt.close('all')

    #################################################

        camera2 = cv2.VideoCapture(2)

        
        for i in xrange(30):
           temp = camera2.read()
        
        retval, camera_capture1 = camera2.read()

        file = "/home/odysseas/Desktop/Coding/test2.jpg"

        cv2.imwrite(file, camera_capture1)

        camera2.release()
        cv2.destroyAllWindows
        
        im1 = np.array(Image.open("/home/odysseas/Desktop/Coding/test2.jpg"), dtype=np.uint8)

        fig,ax = plt.subplots(1)

        ax.imshow(im1)

        plt.show()


        file = "/home/odysseas/Desktop/Coding/test2.jpg"
        img1 = cv2.imread(file)

        RGB2 = np.array([img1[257,315],  # BLUE                   
        img1[280,350],
        img1[310,380],
        img1[275,275],
        img1[325,340],
        img1[295,235],
        img1[320,270],
        img1[340,285],
        img1[145,340],  # WHITE                  
        img1[170,370],
        img1[209,409],
        img1[187,343],
        img1[234,402],
        img1[231,345],
        img1[258,370],
        img1[280,406],
        img1[196,215],
        img1[165,260],  # RED            
        img1[145,300],
        img1[220,220],
        img1[184,300],
        img1[260,215],
        img1[245,260],
        img1[230,300]])
        
        RGB = np.concatenate((RGB1,RGB2), axis=0)
        plt.close('all')
        return RGB

def Range(rgb_array, c_array, my_color):

    red = [0,0,255]
    green = [0,145,0]
    blue = [255,0,0]
    yellow = [0,255,255]
    white = [255,255,255]
    orange = [0,155,255]
    
    for i in range(rgb_array.shape[0]):
        
        if rgb_array[i,2] >= 130 and rgb_array[i,2] <= 255 and rgb_array[i,1] >= 30 and rgb_array[i,1] <= 89 and rgb_array[i,0] >= 40 and rgb_array[i,0] <= 140:
            c_array[i] = 'L'
            rgb_array[i,:] = red
        elif rgb_array[i,2] >= 10 and rgb_array[i,2] <= 80 and rgb_array[i,1] >= 100 and rgb_array[i,1] <= 220 and rgb_array[i,0] >= 100 and rgb_array[i,0] <= 220:
            c_array[i] = 'U'
            rgb_array[i,:] = green
        elif rgb_array[i,2] >= 160 and rgb_array[i,2] <= 255 and rgb_array[i,1] >= 175 and rgb_array[i,1] <= 255 and rgb_array[i,0] >= 90 and rgb_array[i,0] <= 205:
            c_array[i] = 'B'
            rgb_array[i,:] = yellow
        elif rgb_array[i,2] >= 130 and rgb_array[i,2] <= 255 and rgb_array[i,1] >= 150 and rgb_array[i,1] <= 255 and rgb_array[i,0] >= 205 and rgb_array[i,0] <= 255:
            c_array[i] = 'F'
            rgb_array[i,:] = white
        elif rgb_array[i,2] >= 150 and rgb_array[i,2] <= 255 and rgb_array[i,1] >= 90 and rgb_array[i,1] <= 155 and rgb_array[i,0] >= 35 and rgb_array[i,0] <= 120:
            c_array[i] = 'R'
            rgb_array[i,:] = orange
        elif rgb_array[i,2] >= 10 and rgb_array[i,2] <= 80 and rgb_array[i,1] >= 40 and rgb_array[i,1] <= 120 and rgb_array[i,0] >= 155 and rgb_array[i,0] <= 255:
            c_array[i] = 'D'
            rgb_array[i,:] = blue
        my_color[i] = '#%02x%02x%02x' % (rgb_array[i,2], rgb_array[i,1], rgb_array[i,0])

    return c_array


def toneoutput0():
    
    p = pyaudio.PyAudio()

    volume = 1    # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.65   # in seconds, may be float
    f0 = 2000        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples0 = (np.sin(2*np.pi*np.arange(fs*duration)*f0/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples0)

    stream.stop_stream()
    stream.close()

    p.terminate()

    return;

def toneoutput1():
    
    p = pyaudio.PyAudio()

    volume = 1    # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.73   # in seconds, may be float
    f0 = 3200        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples0 = (np.sin(2*np.pi*np.arange(fs*duration)*f0/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples0)

    stream.stop_stream()
    stream.close()

    p.terminate()

    return;

def toneoutput2():
    
    p = pyaudio.PyAudio()

    volume = 1    # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 2.9  # in seconds, may be float
    f2 = 4500        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples2)

    stream.stop_stream()
    stream.close()

    p.terminate()

    return;

def toneoutput6():
    
    p = pyaudio.PyAudio()

    volume = 1    # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 3.15   # in seconds, may be float
    f6 = 6500        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples6 = (np.sin(2*np.pi*np.arange(fs*duration)*f6/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples6)

    stream.stop_stream()
    stream.close()

    p.terminate()

    return;

def toneoutput7():
    
    p = pyaudio.PyAudio()

    volume = 1    # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.43   # in seconds, may be float
    f7 = 14000        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples7 = (np.sin(2*np.pi*np.arange(fs*duration)*f7/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples7)

    stream.stop_stream()
    stream.close()

    p.terminate()

    return;

def toneoutput10():
    
    p = pyaudio.PyAudio()

    volume = 1    # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 1.5   # in seconds, may be float
    f10 = 20000       # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples10 = (np.sin(2*np.pi*np.arange(fs*duration)*f10/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples10)

    stream.stop_stream()
    stream.close()

    p.terminate()

    return;

def Tkinter(mycolor,string,time,show):

    root = Tk()
   
    canvas = Canvas(root, width = 1000, height = 1000)
    canvas.pack()
        
    canvas.create_text(160, 25, font="times 18", text='Solution moves: ')
    canvas.create_text(520, 25, font="times 18", text=string)

    if show == 0:
        canvas.create_text(213, 75, font="times 18", text='')
    else:
        canvas.create_text(213, 75, font="times 18", text=('Total time is: ' + str(time) + ' seconds'))
    


    ############# L = RED #######################

    canvas.create_rectangle(410,50,460,100,fill=mycolor[2])
    canvas.create_rectangle(475,50,525,100,fill=mycolor[4])
    canvas.create_rectangle(540,50,590,100,fill=mycolor[7])

    canvas.create_rectangle(410,115,460,165,fill=mycolor[1])
    canvas.create_rectangle(475,115,525,165,fill='green')
    canvas.create_rectangle(540,115,590,165,fill=mycolor[6])

    canvas.create_rectangle(410,180,460,230,fill=mycolor[0])
    canvas.create_rectangle(475,180,525,230,fill=mycolor[3])
    canvas.create_rectangle(540,180,590,230,fill=mycolor[5])

    #######################################

    ########### D = BLUE ######################

    canvas.create_rectangle(215,245,265,295,fill=mycolor[13])
    canvas.create_rectangle(280,245,330,295,fill=mycolor[11])
    canvas.create_rectangle(345,245,395,295,fill=mycolor[8])

    canvas.create_rectangle(215,310,265,360,fill=mycolor[14])
    canvas.create_rectangle(280,310,330,360,fill='orange')
    canvas.create_rectangle(345,310,395,360,fill=mycolor[9])

    canvas.create_rectangle(215,375,265,425,fill=mycolor[15])
    canvas.create_rectangle(280,375,330,425,fill=mycolor[12])
    canvas.create_rectangle(345,375,395,425,fill=mycolor[10])

    #######################################

    ########### F = WHITE #####################

    canvas.create_rectangle(410,245,460,295,fill=mycolor[21])
    canvas.create_rectangle(475,245,525,295,fill=mycolor[19])
    canvas.create_rectangle(540,245,590,295,fill=mycolor[16])

    canvas.create_rectangle(410,310,460,360,fill=mycolor[22])
    canvas.create_rectangle(475,310,525,360,fill='white')
    canvas.create_rectangle(540,310,590,360,fill=mycolor[17])

    canvas.create_rectangle(410,375,460,425,fill=mycolor[23])
    canvas.create_rectangle(475,375,525,425,fill=mycolor[20])
    canvas.create_rectangle(540,375,590,425,fill=mycolor[18])

    #######################################

    ########### U = GREEN #####################

    canvas.create_rectangle(605,245,655,295,fill=mycolor[37])
    canvas.create_rectangle(670,245,720,295,fill=mycolor[35])
    canvas.create_rectangle(735,245,785,295,fill=mycolor[32])

    canvas.create_rectangle(605,310,655,360,fill=mycolor[38])
    canvas.create_rectangle(670,310,720,360,fill='red')
    canvas.create_rectangle(735,310,785,360,fill=mycolor[33])

    canvas.create_rectangle(605,375,655,425,fill=mycolor[39])
    canvas.create_rectangle(670,375,720,425,fill=mycolor[36])
    canvas.create_rectangle(735,375,785,425,fill=mycolor[34])

    #########################################

    ########## R = ORANGE #####################

    canvas.create_rectangle(410,440,460,490,fill=mycolor[29])
    canvas.create_rectangle(475,440,525,490,fill=mycolor[27])
    canvas.create_rectangle(540,440,590,490,fill=mycolor[24])

    canvas.create_rectangle(410,505,460,555,fill=mycolor[30])
    canvas.create_rectangle(475,505,525,555,fill='blue')
    canvas.create_rectangle(540,505,590,555,fill=mycolor[25])

    canvas.create_rectangle(410,570,460,620,fill=mycolor[31])
    canvas.create_rectangle(475,570,525,620,fill=mycolor[28])
    canvas.create_rectangle(540,570,590,620,fill=mycolor[26])

    #########################################
    ############ B = YELLOW #####################

    canvas.create_rectangle(410,635,460,685,fill=mycolor[45])
    canvas.create_rectangle(475,635,525,685,fill=mycolor[43])
    canvas.create_rectangle(540,635,590,685,fill=mycolor[40])

    canvas.create_rectangle(410,700,460,750,fill=mycolor[46])
    canvas.create_rectangle(475,700,525,750,fill='yellow')
    canvas.create_rectangle(540,700,590,750,fill=mycolor[41])

    canvas.create_rectangle(410,765,460,815,fill=mycolor[47])
    canvas.create_rectangle(475,765,525,815,fill=mycolor[44])
    canvas.create_rectangle(540,765,590,815,fill=mycolor[42])

    #root.mainloop()

    w = 1000
    h = 1000
    x = 0
    y = 0
    
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    canvas.update()

def fix_ascii(sequence):
        
        length = len(sequence)
        seq_fix = []

        j = 0
        while (j < length):
            if j<(length - 1):
                if sequence[j+1].isalpha() == False:
                    move = sequence[j] + sequence[j+1]
                    j=j+1
                else:
                    move = sequence[j]
            else:
                move = sequence[j]
            j = j+1
            seq_fix.append(move)

        return seq_fix

def moves_generator(size):

    moves = ['D', 'D2', 'D\'', 'U', 'U2', 'U\'', 'R', 'R2', 'R\'', 'L', 'L2', 'L\'', 'F', 'F2', 'F\'', 'B', 'B2', 'B\'']
    
    return fix_ascii(''.join(random.choice(moves) for _ in range(size)))

def instr_button():
    tkMessageBox.showinfo("Instructions","Move: Moves a motor based on the selected move from the list. \n\nRandom: Randomizes the cube and solves it. \n\nSolve: Solves the current state of the cube. ")

def choice():
    sequence = moves_generator(18)
    print sequence
    solve1(sequence)

def solve_button():
    solve2()
    
def exit_button():
    quit()
    
def Tkinter1(string,time,show):

    root = Tk()

    w = 1500
    h = 1000
    x = 0
    y = 0


    def selection():
        value=str((listbox.get(ACTIVE)))
        Frequencies(value)
        
    A = Button(root, text ="Exit", bd = 20, command = exit_button)
    B = Button(root, text ="Solve", bd = 20, command = solve_button)
    C = Button(root, text ="Random", bd = 20, command = choice)
    D = Button(root, text ="Move", bd = 20, command = selection)
    E = Button(root, text ="Instructions", bd = 20, command = instr_button)
    listbox = Listbox(root,width=20, height=18,font=("Helvetica", 12))

    ##scrollbar = Scrollbar(listbox, orient="vertical")
    ##scrollbar.config(command=listbox.yview)
    ##scrollbar.pack(side="right", fill="y")

    E.pack(side="top")
    A.pack(side="bottom")
    B.pack(side="right",padx=10)
    C.pack(side="right",padx=10)
    D.pack(side="right",padx=10)
    listbox.pack(side="right",padx=10)

    for item in ["U", "U'", "U2","R", "R'", "R2","F", "F'", "F2","D", "D'", "D2","L", "L'", "L2","B", "B'", "B2"]:
        listbox.insert(END, item)


   
    canvas = Canvas(root, width = 1000, height = 1000)
    canvas.pack()
        
    canvas.create_text(160, 25, font="times 18", text='Solution moves: ')
    canvas.create_text(520, 25, font="times 18", text=string)

    if show == 0:
        canvas.create_text(213, 75, font="times 18", text='')
    else:
        canvas.create_text(213, 75, font="times 18", text=('Total time is: ' + str(time) + ' seconds'))
    


    ############# L = RED #######################

    canvas.create_rectangle(410,50,460,100,fill='red')
    canvas.create_rectangle(475,50,525,100,fill='red')
    canvas.create_rectangle(540,50,590,100,fill='red')

    canvas.create_rectangle(410,115,460,165,fill='red')
    canvas.create_rectangle(475,115,525,165,fill='red')
    canvas.create_rectangle(540,115,590,165,fill='red')

    canvas.create_rectangle(410,180,460,230,fill='red')
    canvas.create_rectangle(475,180,525,230,fill='red')
    canvas.create_rectangle(540,180,590,230,fill='red')

    #######################################

    ########### D = BLUE ######################

    canvas.create_rectangle(215,245,265,295,fill='blue')
    canvas.create_rectangle(280,245,330,295,fill='blue')
    canvas.create_rectangle(345,245,395,295,fill='blue')

    canvas.create_rectangle(215,310,265,360,fill='blue')
    canvas.create_rectangle(280,310,330,360,fill='blue')
    canvas.create_rectangle(345,310,395,360,fill='blue')

    canvas.create_rectangle(215,375,265,425,fill='blue')
    canvas.create_rectangle(280,375,330,425,fill='blue')
    canvas.create_rectangle(345,375,395,425,fill='blue')

    #######################################

    ########### F = WHITE #####################

    canvas.create_rectangle(410,245,460,295,fill='white')
    canvas.create_rectangle(475,245,525,295,fill='white')
    canvas.create_rectangle(540,245,590,295,fill='white')

    canvas.create_rectangle(410,310,460,360,fill='white')
    canvas.create_rectangle(475,310,525,360,fill='white')
    canvas.create_rectangle(540,310,590,360,fill='white')

    canvas.create_rectangle(410,375,460,425,fill='white')
    canvas.create_rectangle(475,375,525,425,fill='white')
    canvas.create_rectangle(540,375,590,425,fill='white')

    #######################################

    ########### U = GREEN #####################

    canvas.create_rectangle(605,245,655,295,fill='green')
    canvas.create_rectangle(670,245,720,295,fill='green')
    canvas.create_rectangle(735,245,785,295,fill='green')

    canvas.create_rectangle(605,310,655,360,fill='green')
    canvas.create_rectangle(670,310,720,360,fill='green')
    canvas.create_rectangle(735,310,785,360,fill='green')

    canvas.create_rectangle(605,375,655,425,fill='green')
    canvas.create_rectangle(670,375,720,425,fill='green')
    canvas.create_rectangle(735,375,785,425,fill='green')

    #########################################

    ########## R = ORANGE #####################

    canvas.create_rectangle(410,440,460,490,fill='orange')
    canvas.create_rectangle(475,440,525,490,fill='orange')
    canvas.create_rectangle(540,440,590,490,fill='orange')

    canvas.create_rectangle(410,505,460,555,fill='orange')
    canvas.create_rectangle(475,505,525,555,fill='orange')
    canvas.create_rectangle(540,505,590,555,fill='orange')

    canvas.create_rectangle(410,570,460,620,fill='orange')
    canvas.create_rectangle(475,570,525,620,fill='orange')
    canvas.create_rectangle(540,570,590,620,fill='orange')

    #########################################
    ############ B = YELLOW #####################

    canvas.create_rectangle(410,635,460,685,fill='yellow')
    canvas.create_rectangle(475,635,525,685,fill='yellow')
    canvas.create_rectangle(540,635,590,685,fill='yellow')

    canvas.create_rectangle(410,700,460,750,fill='yellow')
    canvas.create_rectangle(475,700,525,750,fill='yellow')
    canvas.create_rectangle(540,700,590,750,fill='yellow')

    canvas.create_rectangle(410,765,460,815,fill='yellow')
    canvas.create_rectangle(475,765,525,815,fill='yellow')
    canvas.create_rectangle(540,765,590,815,fill='yellow')

    #root.mainloop()


    
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    canvas.update()
    root.mainloop()
    

def Frequencies(letter):

    if letter == 'D':
        toneoutput6()
        time.sleep(0.1)
    elif letter == 'D\'':
        toneoutput6()
        time.sleep(0.1)
        toneoutput6()
        time.sleep(0.1)
        toneoutput6()
        time.sleep(0.1)
    elif letter == 'D2':
        toneoutput6()
        time.sleep(0.1)
        toneoutput6()
        
    if letter == 'U':
        toneoutput0()
        time.sleep(0.1)
    if letter == 'U\'':
        toneoutput0()
        time.sleep(0.1)
        toneoutput0()
        time.sleep(0.1)
        toneoutput0()
        time.sleep(0.1)
    if letter == 'U2':
        toneoutput0()
        time.sleep(0.1)
        toneoutput0()
        time.sleep(0.1)

    if letter == 'L':
        toneoutput10()
        time.sleep(0.1)
    if letter == 'L\'':
        toneoutput10()
        time.sleep(0.1)
        toneoutput10()
        time.sleep(0.1)
        toneoutput10()
        time.sleep(0.1)
    if letter == 'L2':
        toneoutput10()
        time.sleep(0.1)
        toneoutput10()
        time.sleep(0.1)

    if letter == 'R':
        toneoutput1()
        time.sleep(0.1)
    if letter == 'R\'':
        toneoutput1()
        time.sleep(0.1)
        toneoutput1()
        time.sleep(0.1)
        toneoutput1()
        time.sleep(0.1)
    if letter == 'R2':
        toneoutput1()
        time.sleep(0.1)
        toneoutput1()
        time.sleep(0.1)


    if letter == 'B':
        toneoutput2()
        time.sleep(0.1)
    if letter == 'B\'':
        toneoutput2()
        time.sleep(0.1)
        toneoutput2()
        time.sleep(0.1)
        toneoutput2()
        time.sleep(0.1)
    if letter == 'B2':
        toneoutput2()
        time.sleep(0.1)
        toneoutput2()
        time.sleep(0.1)

    if letter == 'F':
        toneoutput7()
        time.sleep(0.1)
    if letter == 'F\'':
        toneoutput7()
        time.sleep(0.1)
        toneoutput7()
        time.sleep(0.1)
        toneoutput7()
        time.sleep(0.1)
    if letter == 'F2':
        toneoutput7()
        time.sleep(0.1)
        toneoutput7()
        time.sleep(0.1)



def solve1(sequence):

        for i in range(len(sequence)):           
             Frequencies(sequence[i])
             

        start_time = time.time()     
        #rgb = Camera_Activation()
        #c = [' ']*rgb.shape[0]
       # print c ############################
        #color = [' ']*rgb.shape[0]
        #Range(rgb,c,color)
        #string = ''.join(c)
        #print string
        #string = string[:4] + 'U' + string[4:]
        #string = string[:13] + 'R' + string[13:]
        #string = string[:22] + 'F' + string[22:]
        #string = string[:31] + 'D' + string[31:]
        #string = string[:40] + 'L' + string[40:]
        #string = string[:49] + 'B' + string[49:]

        #print string

        solve_moves = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

        #solve_moves = solve_moves.split(' ')
        #Tkinter(color,solve_moves, 0,0)

        for i in range(len(solve_moves)):           
            Frequencies(solve_moves[i])
            


        end_time = time.time()

        diff = (end_time - start_time)
        Tkinter1(solve_moves, ("%.2f" % diff),1)

def solve2():

        start_time = time.time()
             
        rgb = Camera_Activation()
        c = [' ']*rgb.shape[0]
       # print c
        color = [' ']*rgb.shape[0]
        Range(rgb,c,color)

        solve_moves = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

        solve_moves = solve_moves.split(' ')
        Tkinter(color,solve_moves,0,0)

        for i in range(len(solve_moves)):           
            Frequencies(solve_moves[i])

        end_time = time.time()
        diff = (end_time - start_time)

        Tkinter(color,solve_moves,("%.2f" % diff),1)

##### MAIN #######
            

seq_file = open('mixup16.txt','r')
sequence = fix_ascii(seq_file.read())


solve1(sequence)






