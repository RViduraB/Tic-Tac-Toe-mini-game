#importing the tkinter library, messagebox and random
import sys;#importing the interpreter exit
from tkinter import *;
from tkinter import messagebox;#importing messagebox
import random;#importing random


#-----------------------------------------------------------------------------------------------------------------------
#function for nextTurn---------------------EXPLANATION-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#the function take the button as a parameter and check whether there is already marked or win.
#if it is, a message box pop up and display to the user about that whether it is already selected.
#if not player variable set as "x" or "o" as playing mode.
#then checking after perform a click, whether it is a win or tie
#if it is a win a message will display in label as relevant player won or tie
#also it is adjusted to show the turn on each relevant player with a colored patten in player 1 and player 2 labels.
#if the player is the other one, same will apply with different player settings. as per described above.
#-----------------------------------------------------------------------------------------------------------------------
def nextTurn(row, column):
    global player;#global player will be act as whole variable which can access by the whole program.
    if buttons[row][column]['text'] !="" and checkWin() is False:#if passed row and column particular button is empty and not declared as won
        messagebox.showerror("Tic Tac Toe", "The Button already Selected by the Other user")

    if buttons[row][column]['text'] == "" and checkWin() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player;

            if checkWin() is False:
                player = players[1];
                playName2.config(bg='red', fg='yellow');
                playName1.config(bg='white', fg='black');

            elif checkWin() is True:
                dispScreen.config(text='Player 1 Win!');

            elif checkWin() == "Tie":
                dispScreen.config(text='Game is a Tie');

        else:
            buttons[row][column]['text'] = player;

            if checkWin() is False:
                player = players[0];
                playName1.config(bg='red', fg='yellow');
                playName2.config(bg='white', fg='black');

            elif checkWin() is True:
                dispScreen.config(text='Player 2 Win!');

            elif checkWin() == "Tie":
                dispScreen.config(text='Game is a Tie');

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#function for checkWin---------------------EXPLANATION-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#starting a two for loops with th rang of 3 index.
#here we are matching the certain patterns to check if these are occurred we declared it as a winner
#the winning squares(buttons) will be highlighted.
#at the end we ar checking whether there are any spaces left, if the game didnt declared a winner and there are no any spaces left
# we can consider that as a Tie/ Draw situation indicating a red color.
#also if nothing above wont happened, will return a False indicating that there is no winner yet.
#-----------------------------------------------------------------------------------------------------------------------
def checkWin():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg='green');
            buttons[row][1].config(bg='green');
            buttons[row][2].config(bg='green');
            return True;

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] !="":
            buttons[0][column].config(bg='green');
            buttons[1][column].config(bg='green');
            buttons[2][column].config(bg='green');
            return True;

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        buttons[0][0].config(bg='green');
        buttons[1][1].config(bg='green');
        buttons[2][2].config(bg='green');
        return True;

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        buttons[0][2].config(bg='green');
        buttons[1][1].config(bg='green');
        buttons[2][0].config(bg='green');
        return True;
    elif check_emptSpac() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='red');
        return "Tie";

    else:
        return False;

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#function for check_emptySpac---------------------EXPLANATION-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#we early count spaces as 9, clearly we know buttons are 9
#running two for loops we are checking how many empty/not selected buttons there are, and will deduct
# from 9 as per the results.
#if spaces are 0, the False return
#if not True will return
#-----------------------------------------------------------------------------------------------------------------------
def check_emptSpac():
    spaces =9;
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] !="":
                spaces = spaces-1;


    if spaces ==0:
        return False;
    else:
        return True;
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#function for newGame---------------------EXPLANATION-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#this will change the player mode/ which player in randomly.
#the new player changed, the color of the labels will change due to that.
#also the displayable which indicate the winner will also get blank and ready for the game start.
#further any colors highlighted with previous time, will clear to default color.
#-----------------------------------------------------------------------------------------------------------------------
def newGame():
    global player;
    player = random.choice(players);

    if player == players[0]:
        playName1.config(bg='red', fg='yellow');
        playName2.config(bg='white', fg='black');
    else:
        playName2.config(bg='red', fg='yellow');
        playName1.config(bg='white', fg='black');

    dispScreen.config(text="");

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg='#00FFFF');

#-----------------------------------------------------------------------------------------------------------------------
#function for gameQuit---------------------EXPLANATION-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#once the button called, message box will pop up in the screen asking the confirmation of the quit,
#if the response yes means will execute the exit command and terminate the program.
#"no" will continue to the program

#-----------------------------------------------------------------------------------------------------------------------
def gameQuit():
    response = messagebox.askquestion("Confirm", "Are sure You want to Quit from the Game?")
    if response =='yes':
        sys.exit();
#-----------------------------------------------------------------------------------------------------------------------




#starting the Main window for the game interface
#-----------------------------------------------------------------------------------------------------------------------
gameWindow = Tk();#making an instance from tkinter
gameWindow.title("Tic Tac Toe 1.0");#title as the game name
gameWindow.geometry("1000x570");#adjusting the width and height of the window
gameWindow.resizable(width=False, height=False);#Falsing the capability of resizing horizontally and vertically.
gameWindow.config(bg='lightgreen');#background color set as light green in the main window

players =["X", "O"];#making an array with two player modes inside of it.
# player = players[0];#able to make manual and set player changes with enabling this.
player = random.choice(players);#picking randomly the players.
buttons = [[0,0,0],#creating a 2d array withing places to make buttons
          [0,0,0],
          [0,0,0]]

#-----------------------------------------------------------------------------------------------------------------------
disFrame =Frame(gameWindow, bg='yellow', width=350, height=80)#creating a frame to hold the title
disFrame.place(x=320, y=10)#adjusting frame sizes
titleName = Label(disFrame, font=('Arial',20), fg='black', bg='orange', text='**TIC TAC PLAY** 2025**');#making a label and put in to the frame
titleName.pack();#packing and finish the label in the frame

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
dispPanel = Frame(gameWindow, bg='gray', width=465, height=350);#frame to hold the player name labels
dispPanel.place(x=525, y=70);#adjsuting frame sizes

playName1 = Label(dispPanel, font=('Arial',25), fg='purple', text='PLAYER 1 : X', bg='lightblue');#player name labels
playName1.place(x=5,y=10);
playName2 = Label(dispPanel, font=('Arial',25), fg='purple', text='PLAYER 2 : O',);
playName2.place(x=232,y=10);

dispScreen =Label(dispPanel, font=('Arial',45), fg='BLUE', text='',width=12,height=2, bg='white');#label for displaying wining statue
dispScreen.place(x=20, y=100);#adjusting the location via coordination/Cartesian plane in the assigned frame

restBtn = Button(dispPanel, font=('Arial',25), text='RESET', command=newGame);#making reset button
restBtn.place(x=30,y=270);#location

quitButton = Button(dispPanel, font=('Arial', 25), text='Quit', command=gameQuit);#making quit button
quitButton.place(x=350, y=270);

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
btnFrame = Frame(gameWindow, width=500, height=450);#frame for buttons
btnFrame.place(x=10,y=65);#coordinated location in the game window

for row in range(3):#for loop to initialize the buttons with necessary command and textures and assigned them in to the previous created 2d array
    for column in range(3):
        buttons[row][column] = Button(btnFrame, text="", font=('Arial', 40), bg='#00FFFF', width=5, height=2, command=lambda row=row, column = column:nextTurn(row,column));
        buttons[row][column].grid(row=row,column=column);#assigned buttons to array locations and adjust the 2d aray positions to the frame as same as similar in grid

#after creating the whole window we are making highlighted color to select which player in the playing state with red color
if player==players[0]:
    playName1.config(bg='red', fg='yellow');
else:
    playName2.config(bg='red', fg='yellow');



messagebox.showinfo("tic tac toe","The player turn will randomly get selected with each startup")
gameWindow.mainloop();#the whole program will terminate at the end of loop and this loop wil initiate the program,rendering the textures and GUI and will terminate at the end.
