from tkinter import *
import tkinter.font
from random import *

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
ANS = 6
TEN = 10
NINE = 9

class GameBoard(Frame):
  def __init__(self):

    #Variables ---------------------------------------------------------------------------------------------------
    self.__aQuestions = []
    self.__bQuestions = []
    self.__cQuestions = []
    self.__dQuestions = []
    self.__eQuestions = []
    aQuestions = self.__aQuestions
    bQuestions = self.__bQuestions
    cQuestions = self.__cQuestions
    dQuestions = self.__dQuestions
    eQuestions = self.__eQuestions
    self.__currentAnswer = 0
    currentAnswer = self.__currentAnswer
    self.__userAns = 0
    userAnswer = self.__userAns
    self.__player1 = 0
    self.__player2 = 0
    self.__player = 1
    self.__qValue = 0
    self.__p1Name = "Player 1"
    self.__p2Name = "Player 2"
    self.__mode = 2
    self.__compLevelS = ONE
    self.__compLevelE = FOUR
    self.__compLevelChk = ONE
    


    #initialize main window --------------------------------------------------------------------------------------
    Frame.__init__(self,bg = "black")
    self.master.title("Corey & Victor's Jeopardy!")
    self.grid()
    self.master.withdraw()


    #initialize question window -----------------------------------------------------------------------------------
    #question commands
    
    def userAns():
      self.__userAns = int(answer.get())
      question.__submit["state"] = NORMAL
##      print(self.__userAns, type(self.__userAns)) #debug code
     

    def submit():
      if self.__currentAnswer == 1:
        correctAns = question.__radio1["text"]
      if self.__currentAnswer == 2:
        correctAns = question.__radio2["text"]
      if self.__currentAnswer == 3:
        correctAns = question.__radio3["text"]
      if self.__currentAnswer == 4:
        correctAns = question.__radio4["text"]
      if self.__userAns == self.__currentAnswer:
        messagebox.showwarning("CORRECT ANSWER!","YOU GOT THE ANSWER CORRECT!")
        question.withdraw()
        self.master.deiconify()
        if self.__player == 1:
          self.__player1 += self.__qValue
##          print(self.__player1) #debug code
        else:
          self.__player2 += self.__qValue
##          print(self.__player2) #debug code
      elif self.__userAns != self.__currentAnswer:
        messagebox.showerror("INCORRECT ANSWER!","YOU GOT THE WRONG ANSWER!\nThe correct answer was \"" + correctAns + "\"")
        question.withdraw()
        self.master.deiconify()
        if self.__player == 1:
          self.__player1 -= self.__qValue
##          print(self.__player1) #debug code
        else:
          self.__player2 -= self.__qValue
##          print(self.__player2) #debug code
      self.__changePlayer()

      
    self.top = Toplevel()
    question = self.top
    question.title("Question!")
    answer = IntVar()
    question.__questionPane = Frame(question,pady=5,)
    question.__answerPane = Frame(question,)
    question.__submitPane = Frame(question,)
    question.__questionPane.grid(row=0,sticky="W")
    question.__answerPane.grid(row = 1,column=0,sticky="W")
    question.__submitPane.grid(row=1,column=1,)

    #question label
    question.__qLabel = Label(question.__questionPane, text = "Please select a question",wraplength=350)
    question.__qLabel.grid(row=0,sticky="W")

    #question radio buttons
    question.__radio1 = Radiobutton(question.__answerPane, text = "answer 1",value=1,variable=answer,
                                    command = userAns)
    question.__radio2 = Radiobutton(question.__answerPane, text = "answer 2",value=2,variable=answer,
                                    command = userAns)
    question.__radio3 = Radiobutton(question.__answerPane, text = "answer 3",value=3,variable=answer,
                                    command = userAns)
    question.__radio4 = Radiobutton(question.__answerPane, text = "answer 4",value=4,variable=answer,
                                    command = userAns)
    question.__radio1.grid(row=0, sticky = "W")
    question.__radio2.grid(row=1, sticky = "W")
    question.__radio3.grid(row=2, sticky = "W")
    question.__radio4.grid(row=3, sticky = "W")

    #submit button
    question.__submit = Button(question.__submitPane,text = "Submit Answer!",state = DISABLED,
                               command = submit)
    question.__submit.grid(row=1,column=1)
    

    #do not close
    question.protocol('WM_DELETE_WINDOW',1)

    #start closed
    question.withdraw()



    #settings window ----------------------------------------------------------------------------------------------
    def mode():
      self.__mode = int(modeVar.get())
      if self.__mode == ONE:
        settings.__entry2.delete(0,END)
        settings.__entry2.insert(0,"COMPUTER (EASY)")
        settings.__entry2["state"] = DISABLED
        self.__compLevelS = ONE
        self.__compLevelE = FOUR
        self.__compLevelChk = ONE
##      print(self.__mode,type(self.__mode)) #debug code
      elif self.__mode == THREE:
        settings.__entry2.delete(0,END)
        settings.__entry2.insert(0,"COMPUTER (MEDIUM)")
        settings.__entry2["state"] = DISABLED
        self.__compLevelS = ONE
        self.__compLevelE = TWO
        self.__compLevelChk = ONE
      elif self.__mode == FOUR:
        settings.__entry2.delete(0,END)
        settings.__entry2.insert(0,"COMPUTER (HARD)")
        settings.__entry2["state"] = DISABLED
        self.__compLevelS = ONE
        self.__compLevelE = TEN
        self.__compLevelChk = NINE
      else:
        settings.__entry2["state"] = NORMAL

    def __enter():
      self.master.deiconify()
      self.__mode = int(modeVar.get())
      self.__p1Name = settings.__entry1.get()
##      print(self.__p1Name, type(self.__p1Name)) #debug code
      self.__p2Name = settings.__entry2.get()
##      print(self.__p2Name, type(self.__p2Name)) #debug code
      self.__p1Label["text"] = self.__p1Name + " = "
      self.__p2Label["text"] = self.__p2Name + " = "
      settings.withdraw()
    #initialize settings window 
    self.top2 = Toplevel()
    self.color = "black"
    modeVar = IntVar()
    settings = self.top2
    settings.title("Settings")
    settings.__labelPane = Frame(settings,)
    settings.__radioPane = Frame(settings,)
    settings.__entryPane = Frame(settings,)
    settings.__enterPane = Frame(settings,)
    settings.__labelPane.grid(row = 0)
    settings.__radioPane.grid(row = 1, column = 0, sticky = W)
    settings.__entryPane.grid(row = 1, column = 1)
    settings.__enterPane.grid(row = 2)
    settings.__label1 = Label(settings.__labelPane, text = "Please select a mode to play in, then hit submit!")
    settings.__label1.grid()

    #SETTINGS
    settings.__radio1 = Radiobutton(settings.__radioPane, text = "Play Against Computer (EASY)!", value = "1", variable = modeVar, command = mode)
    settings.__radio3 = Radiobutton(settings.__radioPane, text = "Play Against Computer (MEDIUM)!", value = "3", variable = modeVar, command = mode)
    settings.__radio4 = Radiobutton(settings.__radioPane, text = "Play Against Computer (HARD)!", value = "4", variable = modeVar, command = mode)
    settings.__radio2 = Radiobutton(settings.__radioPane, text = "Play Against Player!", value = "2", variable = modeVar, command = mode)
    settings.__radio1.grid(row = 0, pady = 10, sticky = W)
    settings.__radio3.grid(row = 1, pady = 10, sticky = W)
    settings.__radio4.grid(row = 2, pady = 10, sticky = W)
    settings.__radio2.grid(row = 3, sticky = W)

    settings.__label2 = Label(settings.__entryPane, text = "Enter player names below!")
    settings.__entry1 = Entry(settings.__entryPane, width = 22)
    settings.__entry2 = Entry(settings.__entryPane, width = 22)
    settings.__entry1.insert(0, "Player 1")
    settings.__entry2.insert(0, "Player 2")
    settings.__label2.grid(row = 0, sticky = "W")
    settings.__entry1.grid(row = 1, sticky = "W")
    settings.__entry2.grid(row = 2, sticky = "W")

    #ENTER BUTTON
    settings.__enter = Button(settings.__enterPane, text = "ENTER", width = 30,
                              command = __enter)
    settings.__enter.grid(pady = 5)


    #DISABLE WINDOW CLOSING
    settings.protocol('WM_DELETE_WINDOW',messagebox.showinfo("Settings","Please choose a mode and a color and hit submit!"))

      

    #initialize help window -------------------------------------------------------------------------------------
    self.top3 = Toplevel()
    opHelp = self.top3
    opHelp.withdraw()
    opHelp.title("HELP!")
    opHelp.__label2 = Label(opHelp, text = """Key Commands: \n<F1> : Help box \n
<ESCAPE> : Quit the game\n
Directions:\n
Please choose the difficulty of the the AI,\n
or if you wish to play with a friend\n
Then your name.
\n\n When the game board opens please input the question files\n
Then you will alternate choosing questions based on money values,
\n Correct answers add money, wrong answers subtract!\n
Person with the most money in the end wins!""")
    opHelp.__label2.grid()
    opHelp.protocol('WM_DELETE_WINDOW',1)





    #Game Window -------------------------------------------------------------------------------------------------
    #data pane
    self.__dataPane = Frame(self, bg = "black")
    self.__dataPane.grid(row = 0, column = 0)

    #labels for data pane
    self.__image = PhotoImage(file = "logo.gif")
    self.__imageLabel = Label(self.__dataPane, image = self.__image, bg = "black")
    self.__imageLabel.grid(row = 0)
    
    cFont = tkinter.font.Font(family = "Verdana",
                size = 12)
    self.__label2 = Label(self.__dataPane, font = cFont, text = " " * 50 + "Coded by Corey & Victor" + " " * 50, fg = "orange", bg = "black")
    self.__label2.grid(row = 1)

    self.__scorePane = Frame(self, bg = "black")
    self.__scorePane.grid(row = 1)
    self.__p1Label = Label(self.__scorePane, font = cFont, text = self.__p1Name + " = ", fg = "red", bg = "black")
    self.__p1Score = Label(self.__scorePane, font = cFont, text = "0", fg = "red", bg = "black")
    self.__pSpace = Label(self.__scorePane, font = cFont, text = "              ", fg = "red", bg = "black")
    self.__p2Label = Label(self.__scorePane, font = cFont, text = self.__p2Name + " = ", fg = "green", bg = "black")
    self.__p2Score = Label(self.__scorePane, font = cFont, text = "0", fg = "green", bg = "black")
    self.__playerL = Label(self.__scorePane, font = cFont, text = self.__p1Name+"\'s turn!", fg = "blue", bg = "black")
    self.__p1Label.grid(row = 0,column = 1)
    self.__p1Score.grid(row = 0,column = 2)
    self.__pSpace.grid(row = 0, column = 3)
    self.__p2Label.grid(row = 0,column = 4)
    self.__p2Score.grid(row = 0,column = 5)
    self.__playerL.grid(row = 1, column = 3)
    #button frame
    self.__buttonPane = Frame(self, bg = "black")
    for column in range(FIVE):
      self.__buttonPane.columnconfigure(column,weight = 1)
    
    for row in range(FIVE):
      self.__buttonPane.rowconfigure(row,weight = 1)
    self.__buttonPane.grid(row = 2, sticky = W+E+N+S, )

    #command initialize
    command1 = ""
    
    #buttons
    self.__topicA = Button(self.__buttonPane,text = "TOPIC1", fg = "yellow", bg = "black", state = DISABLED, wraplength=100,)
    self.__buttonA1 = Button(self.__buttonPane,text = "INPUT", fg = "yellow", bg = "blue",state = NORMAL,cursor="target",
                             command = lambda: self._choose("A",ZERO, self.__buttonA1["text"]),)
    self.__buttonA2 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("A",ONE, self.__buttonA2["text"]))
    self.__buttonA3 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("A",TWO, self.__buttonA3["text"]))
    self.__buttonA4 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("A",THREE, self.__buttonA4["text"]))
    self.__buttonA5 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("A",FOUR, self.__buttonA5["text"]))
    self.__topicA.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonA1.grid(row = 1, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonA2.grid(row = 2, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonA3.grid(row = 3, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonA4.grid(row = 4, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonA5.grid(row = 5, column = 0, sticky = W+E+N+S, padx = 10, pady = 10)
    
    self.__topicB = Button(self.__buttonPane,text= "TOPIC1", fg = "yellow", bg = "black", state = DISABLED, wraplength=100)
    self.__buttonB1 = Button(self.__buttonPane,text = "INPUT", fg = "yellow", bg = "blue",state = NORMAL,cursor="target",
                             command = lambda: self._choose("B",ZERO, self.__buttonB1["text"]),)
    self.__buttonB2 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("B",ONE, self.__buttonB2["text"]),)
    self.__buttonB3 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("B",TWO, self.__buttonB3["text"]),)
    self.__buttonB4 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("B",THREE, self.__buttonB4["text"]),)
    self.__buttonB5 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("B",FOUR, self.__buttonB5["text"]),)
    self.__topicB.grid(row = 0, column = 1, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonB1.grid(row = 1, column = 1, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonB2.grid(row = 2, column = 1, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonB3.grid(row = 3, column = 1, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonB4.grid(row = 4, column = 1, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonB5.grid(row = 5, column = 1, sticky = W+E+N+S, padx = 10, pady = 10)

    self.__topicC = Button(self.__buttonPane,text= "TOPIC1", fg = "yellow", bg = "black", state = DISABLED, wraplength=100)
    self.__buttonC1 = Button(self.__buttonPane,text = "INPUT", fg = "yellow", bg = "blue",state = NORMAL,cursor="target",
                             command = lambda: self._choose("C",ZERO, self.__buttonC1["text"]),)
    self.__buttonC2 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("C",ONE, self.__buttonC2["text"]),)
    self.__buttonC3 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("C",TWO, self.__buttonC3["text"]),)
    self.__buttonC4 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("C",THREE, self.__buttonC4["text"]),)
    self.__buttonC5 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("C",FOUR, self.__buttonC5["text"]),)
    self.__topicC.grid(row = 0, column = 2, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonC1.grid(row = 1, column = 2, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonC2.grid(row = 2, column = 2, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonC3.grid(row = 3, column = 2, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonC4.grid(row = 4, column = 2, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonC5.grid(row = 5, column = 2, sticky = W+E+N+S, padx = 10, pady = 10)

    self.__topicD = Button(self.__buttonPane,text= "TOPIC1", fg = "yellow", bg = "black", state = DISABLED, wraplength=100)
    self.__buttonD1 = Button(self.__buttonPane,text = "INPUT", fg = "yellow", bg = "blue",state = NORMAL,cursor="target",
                             command = lambda: self._choose("D",ZERO, self.__buttonD1["text"]),)
    self.__buttonD2 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("D",ONE, self.__buttonD2["text"]),)
    self.__buttonD3 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("D",TWO, self.__buttonD3["text"]),)
    self.__buttonD4 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("D",THREE, self.__buttonD4["text"]),)
    self.__buttonD5 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("D",FOUR, self.__buttonD5["text"]),)
    self.__topicD.grid(row = 0, column = 3, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonD1.grid(row = 1, column = 3, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonD2.grid(row = 2, column = 3, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonD3.grid(row = 3, column = 3, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonD4.grid(row = 4, column = 3, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonD5.grid(row = 5, column = 3, sticky = W+E+N+S, padx = 10, pady = 10)

    self.__topicE = Button(self.__buttonPane,text= "TOPIC1", fg = "yellow", bg = "black", state = DISABLED, wraplength=100)
    self.__buttonE1 = Button(self.__buttonPane,text = "INPUT", fg = "yellow", bg = "blue",state = NORMAL,cursor="target",
                             command = lambda: self._choose("E",ZERO, self.__buttonE1["text"]),)
    self.__buttonE2 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("E",ONE, self.__buttonE2["text"]),)
    self.__buttonE3 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("E",TWO, self.__buttonE3["text"]),)
    self.__buttonE4 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("E",THREE, self.__buttonE4["text"]),)
    self.__buttonE5 = Button(self.__buttonPane,text = "~~~", fg = "yellow", bg = "blue",state = DISABLED,cursor="tcross",
                             command = lambda: self._input("E",FOUR, self.__buttonE5["text"]),)
    self.__topicE.grid(row = 0, column = 4, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonE1.grid(row = 1, column = 4, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonE2.grid(row = 2, column = 4, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonE3.grid(row = 3, column = 4, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonE4.grid(row = 4, column = 4, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__buttonE5.grid(row = 5, column = 4, sticky = W+E+N+S, padx = 10, pady = 10)
    self.__qLeft = [self.__buttonA1,self.__buttonA2,self.__buttonA3,self.__buttonA4,self.__buttonA5,
                    self.__buttonB1,self.__buttonB2,self.__buttonB3,self.__buttonB4,self.__buttonB5,
                    self.__buttonC1,self.__buttonC2,self.__buttonC3,self.__buttonC4,self.__buttonC5,
                    self.__buttonD1,self.__buttonD2,self.__buttonD3,self.__buttonD4,self.__buttonD5,
                    self.__buttonE1,self.__buttonE2,self.__buttonE3,self.__buttonE4,self.__buttonE5]

    


    #DEFINE KEYPRESSES -------------------------------------------------------------------------------------
    def keyQuit(event):
      self.master.destroy()
    self.master.bind("<Escape>",keyQuit)
    self.top.bind("<Escape>",keyQuit)
    self.top2.bind("<Escape>",keyQuit)
    self.top3.bind("<Escape>",keyQuit)




    def keyHelp(event):
      if opHelp.state() == "withdrawn":
        opHelp.deiconify()
      else:
        opHelp.withdraw()
    self.master.bind("<F1>",keyHelp)
    self.top.bind("<F1>",keyHelp)
    self.top2.bind("<F1>",keyHelp)
    opHelp.bind("<F1>",keyHelp)



    
  def _choose(self,sec,num,value):
    try:
      if sec == "A":
        if self.__buttonA1["text"] == "INPUT":
          self._importQ(sec)
        else:
          self._input(sec,num,value)
      elif sec == "B":
        if self.__buttonB1["text"] == "INPUT":
          self._importQ(sec)
        else:
          self._input(sec,num,value)
      elif sec == "C":
        if self.__buttonC1["text"] == "INPUT":
          self._importQ(sec)
        else:
          self._input(sec,num,value)
      elif sec == "D":
        if self.__buttonD1["text"] == "INPUT":
          self._importQ(sec)
        else:
          self._input(sec,num,value)
      elif sec == "E":
        if self.__buttonE1["text"] == "INPUT":
          self._importQ(sec)
        else:
          self._input(sec,num,value)
    except:
      messagebox.showerror("ERROR!", "Please restart!")




  def _close(self):
    self.__buttonA3.configure(state = 'normal')




  def _hideQ(self):
    try:
      self.top.deiconify()
      self.top.__label3 = Label(self.top, text = "Hello World!2")
      self.top.__label3.grid()
    except:
      messagebox.showerror("Error!","Error, you closed the question pane, please restart the game")




  def _importQ(self,sec):
    try:
      #file dialog to get name
      filename = filedialog.askopenfilename()
##      print(filename,type(filename)) #debug code
      #open file
      f = open(filename,'r')

      #input topic into topic button-----------
      topic = f.readline()
##      print(topic,type(topic)) #debug code
      if sec == "A":
        self.__topicA["text"] = topic
      if sec == "B":
        self.__topicB["text"] = topic
      if sec == "C":
        self.__topicC["text"] = topic
      if sec == "D":
        self.__topicD["text"] = topic
      if sec == "E":
        self.__topicE["text"] = topic

      #input question monetary values, make buttons normal state----------
      num = 0
      for line in f:
        line1 = line.split(",")
        if sec == "A":
          self.__aQuestions.append(line1)
##          print(self.__aQuestions,type(aQuestions)) #debug code
          if num == 0:
            self.__buttonA1["text"] = line1[0]
          elif num == 1:
            self.__buttonA2["text"] = line1[0]
            self.__buttonA2["state"] = NORMAL
          elif num == 2:
            self.__buttonA3["text"] = line1[0]
            self.__buttonA3["state"] = NORMAL
          elif num == 3:
            self.__buttonA4["text"] = line1[0]
            self.__buttonA4["state"] = NORMAL
          elif num == 4:
            self.__buttonA5["text"] = line1[0]
            self.__buttonA5["state"] = NORMAL
        elif sec == "B":
          self.__bQuestions.append(line1)
          if num == 0:
            self.__buttonB1["text"] = line1[0]
          elif num == 1:
            self.__buttonB2["text"] = line1[0]
            self.__buttonB2["state"] = NORMAL
          elif num == 2:
            self.__buttonB3["text"] = line1[0]
            self.__buttonB3["state"] = NORMAL
          elif num == 3:
            self.__buttonB4["text"] = line1[0]
            self.__buttonB4["state"] = NORMAL
          elif num == 4:
            self.__buttonB5["text"] = line1[0]
            self.__buttonB5["state"] = NORMAL
        elif sec == "C":
          self.__cQuestions.append(line1)
          if num == 0:
            self.__buttonC1["text"] = line1[0]
          elif num == 1:
            self.__buttonC2["text"] = line1[0]
            self.__buttonC2["state"] = NORMAL
          elif num == 2:
            self.__buttonC3["text"] = line1[0]
            self.__buttonC3["state"] = NORMAL
          elif num == 3:
            self.__buttonC4["text"] = line1[0]
            self.__buttonC4["state"] = NORMAL
          elif num == 4:
            self.__buttonC5["text"] = line1[0]
            self.__buttonC5["state"] = NORMAL
        elif sec == "D":
          self.__dQuestions.append(line1)
          if num == 0:
            self.__buttonD1["text"] = line1[0]
          elif num == 1:
            self.__buttonD2["text"] = line1[0]
            self.__buttonD2["state"] = NORMAL
          elif num == 2:
            self.__buttonD3["text"] = line1[0]
            self.__buttonD3["state"] = NORMAL
          elif num == 3:
            self.__buttonD4["text"] = line1[0]
            self.__buttonD4["state"] = NORMAL
          elif num == 4:
            self.__buttonD5["text"] = line1[0]
            self.__buttonD5["state"] = NORMAL
        elif sec == "E":
          self.__eQuestions.append(line1)
          if num == 0:
           self.__buttonE1["text"] = line1[0]
          elif num == 1: 
            self.__buttonE2["text"] = line1[0]
            self.__buttonE2["state"] = NORMAL
          elif num == 2:
            self.__buttonE3["text"] = line1[0]
            self.__buttonE3["state"] = NORMAL
          elif num == 3:
            self.__buttonE4["text"] = line1[0]
            self.__buttonE4["state"] = NORMAL
          elif num == 4:
            self.__buttonE5["text"] = line1[0]
            self.__buttonE5["state"] = NORMAL
        num += 1
    except:
      messagebox.showerror("Error!","Please check the file you entered, or enter a file!")
    finally:
      f.close()

    

  def _input(self,sec,num,value):
    question = self.top
    qLeft = self.__qLeft
    print(qLeft)
    if sec == "A":
      qList = self.__aQuestions
      if num == ZERO:
        self.__buttonA1["state"] = DISABLED
        self.__qLeft.pop(self.__qLeft.index(self.__buttonA1))
      if num == ONE:
        self.__buttonA2["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonA2))
      if num == TWO:
        self.__buttonA3["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonA3))
      if num == THREE:
        self.__buttonA4["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonA4))
      if num == FOUR:
        self.__buttonA5["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonA5))
    elif sec == "B":
      qList = self.__bQuestions
      if num == ZERO:
        self.__buttonB1["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonB1))
      if num == ONE:
        self.__buttonB2["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonB2))
      if num == TWO:
        self.__buttonB3["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonB3))
      if num == THREE:
        self.__buttonB4["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonB4))
      if num == FOUR:
        self.__buttonB5["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonB5))
    elif sec == "C":
      qList = self.__cQuestions
      if num == ZERO:
        self.__buttonC1["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonC1))
      if num == ONE:
        self.__buttonC2["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonC2))
      if num == TWO:
        self.__buttonC3["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonC3))
      if num == THREE:
        self.__buttonC4["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonC4))
      if num == FOUR:
        self.__buttonC5["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonC5))
    elif sec == "D":
      qList = self.__dQuestions
      if num == ZERO:
        self.__buttonD1["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonD1))
      if num == ONE:
        self.__buttonD2["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonD2))
      if num == TWO:
        self.__buttonD3["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonD3))
      if num == THREE:
        self.__buttonD4["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonD4))
      if num == FOUR:
        self.__buttonD5["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonD5))
    elif sec == "E":
      qList = self.__eQuestions
      if num == ZERO:
        self.__buttonE1["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonE1))
      if num == ONE:
        self.__buttonE2["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonE2))
      if num == TWO:
        self.__buttonE3["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonE3))
      if num == THREE:
        self.__buttonE4["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonE4))
      if num == FOUR:
        self.__buttonE5["state"] = DISABLED
        self.__qLeft.pop(qLeft.index(self.__buttonE5))
    print(qLeft)
    try:
      if num >= ZERO and num <= FOUR and int(value) > 0:
        question.__qLabel["text"] = str(qList[num][ONE])
        question.__radio1["text"] = str(qList[num][TWO])
        question.__radio2["text"] = str(qList[num][THREE])
        question.__radio3["text"] = str(qList[num][FOUR])
        question.__radio4["text"] = str(qList[num][FIVE])
        self.__currentAnswer = int(qList[num][ANS])
        self.__qValue = int(value)
  ##      print(self.__currentAnswer,type(self.__currentAnswer)) #debug code
        self.master.withdraw()
        question.deiconify()
        print("test")
    except:
      print("")


  def __changePlayer(self):
    if self.__gameStatus():
      if self.__player == 1:
        self.__player = 2
        self.__p1Score["text"] = self.__player1
        self.__playerL["text"] = str(self.__p2Name)+"\'s turn!"
        messagebox.showinfo("CHANGE PLAYER!","It is "+self.__p2Name+"\'s turn!")
        if self.__mode == 1 or self.__mode == 3 or self.__mode == 4:
          self.__compTurn()
      else:
        self.__player = 1
        self.__p2Score["text"] = self.__player2
        messagebox.showinfo("CHANGE PLAYER!","It is "+self.__p1Name+"\'s turn!")
        self.__playerL["text"] = str(self.__p1Name)+"\'s turn!"

  def __compTurn(self):
    compQ = randint(0,(len(self.__qLeft)-1))
    if compQ  < 5:
      sec = "A"
      section = self.__topicA["text"]
    elif compQ < 10:
      sec = "B"
      section = self.__topicB["text"]
    elif compQ < 15:
      sec = "C"
      section = self.__topicC["text"]
    elif compQ < 20:
      sec = "D"
      section = self.__topicD["text"]
    elif compQ < 25:
      sec = "E"
      section = self.__topicE["text"]
    compQB = self.__qLeft[compQ]
    messagebox.showinfo("Computer's Turn!","Computer chose the $"+compQB["text"]+" in "+section)
    self.__qLeft.pop(self.__qLeft.index(compQB))
    print(self.__qLeft)
    compQB["state"] = DISABLED
    compG = randint(self.__compLevelS,self.__compLevelE)
    if compG <= self.__compLevelChk:
      messagebox.showinfo("Computer's Turn!","Computer got it RIGHT!")
      self.__player2 += int(compQB["text"])
      self.__changePlayer()
    else:
      messagebox.showerror("Computer's Turn!","Computer got it WRONG!")
      self.__player2 -= int(compQB["text"])
      self.__changePlayer()


  def __gameStatus(self):
    status = True
    if self.__qLeft == []:
      status = False
      if self.__player1 > self.__player2:
        messagebox.showinfo("GAMEOVER!","GAMEOVER!\n\n"+self.__p1Name+" wins with $"+str(self.__player1))
      else:
        messagebox.showinfo("GAMEOVER!","GAMEOVER!\n\n"+self.__p2Name+" wins with $"+str(self.__player2))
    return status
    
def main():
  GameBoard().mainloop()

main()
