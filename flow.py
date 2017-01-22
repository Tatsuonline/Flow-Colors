from Tkinter import *
import math
import tkMessageBox
import tkFileDialog

fileInput = open("sample.txt", "r")

rowCounter = 0
columnCounter = 0

currentScore = 100

for line in fileInput:
	rowCounter += 1
	number = line.split(",")
	columnCounter = len(number)

matrixOfValues = [[0 for i in range(rowCounter)] for j in range(columnCounter)]
rowNumber = 0
columnNumber = 0

fileInput.seek(0)
for line in fileInput:
	number = line.split(",")
	while columnNumber < columnCounter:
		matrixOfValues[rowNumber][columnNumber] = int(number[columnNumber])
		columnNumber += 1
	columnNumber = 0
	rowNumber += 1

print matrixOfValues

def set_color(chooser):
    if chooser == 1:
        return "blue"
    elif chooser == 2:
        return "yellow"
    elif chooser == 3:
        return "purple"
    else:
        return "white"

#def check_if_complete(grid):
    

class App:
    def __init__(self, master):
        self.selected_color = 2 
        self.last_clicked = None

        frame = Frame(master)
        frame.pack()

        self.toolbar = {
                "exitButton": None, "loadButton": None, "saveButton": None, "scoreBoard": None, "infoButton": None
        }

	toolFrame = Frame(frame)
	toolFrame.pack()

	self.toolbar["scoreBoard"] = Label(toolFrame, text = "Score: %d" % currentScore)
	self.toolbar["scoreBoard"].pack(side=LEFT, padx = 2, pady = 3)

	self.toolbar["loadButton"] = Button(toolFrame, text="LOAD", activebackground="red", command=self.loadGame, bg="red")
        self.toolbar["loadButton"].pack(side=LEFT, padx = 2, pady = 3)

	self.toolbar["saveButton"] = Button(toolFrame, text="SAVE", activebackground="orange", command=self.saveGame, bg="orange")
        self.toolbar["saveButton"].pack(side=LEFT, padx = 2, pady = 3)

	self.toolbar["infoButton"] = Button(toolFrame, text="INFO", activebackground="gray", command=self.info, bg="gray")
        self.toolbar["infoButton"].pack(side=LEFT, padx = 2, pady = 3)

	self.toolbar["exitButton"] = Button(toolFrame, text="EXIT", activebackground="green", command=frame.quit, bg="green")
        self.toolbar["exitButton"].pack(side=RIGHT, padx = 2, pady = 3)

        self.bGrid = []

        x = 0
        for row in matrixOfValues:
            rowFrame = Frame(frame)
            rowFrame.pack()
            y = 0
            for i in row:
                button = Button(rowFrame, text=str(i), bg=set_color(i), activebackground=set_color(i))
                button.uservals = {"color": i, "initials": False, "coords": (x,y)}
                if i != 0:
                    button.uservals["initials"] = True
                button.config(command=lambda b=button:
                        self.gbutton_click(b, self.selected_color, self.last_clicked))
                button.pack(side=LEFT)
                self.bGrid.append(button)
                y += 1
            x += 1


    def loadGame(self):
	    #tkMessageBox.askquestion("Load Game", "Which game would you like to load?")
	     tkFileDialog.askopenfile("r")

    def saveGame(self):
	    #tkMessageBox.showinfo("Save Game", "Your game was saved!")
	    tkFileDialog.asksaveasfile("w")

    def success(self):
	    tkMessageBox.showinfo("Success!", "You won!")

    def info(self):
	    tkMessageBox.showinfo("Information", "The scoring system works backwards! Try to use the least amount of clicks possible!")

    def gbutton_click(self, button, selected_color, last_clicked):
        if button.uservals["initials"]:
            self.selected_color = button.uservals["color"]
            self.last_clicked = button
            
        elif last_clicked is not None:
            x = button.uservals["coords"][0]
            y = button.uservals["coords"][1]
            oldx = last_clicked.uservals["coords"][0]
            oldy = last_clicked.uservals["coords"][1]

            if((math.fabs(x - oldx) == 1 and (oldy - y) == 0)
                or (math.fabs(y - oldy) == 1 and (oldx - x) == 0)):
                button.config(bg=set_color(self.selected_color))
                button.uservals["color"] = self.selected_color
                self.last_clicked = button

       # check_if_complete(self.bGrid)

root = Tk()
root.wm_title("Flow Colors")
app = App(root)

root.mainloop()

fileInput.close()
