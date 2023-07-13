import tkinter as tk
from PIL import Image,ImageTk
from random import randint
import time


game = tk.Tk()
game.title("STINY GAMES")
game.configure(background="deepskyblue")
class rock_paper_scissor:
    def __init__(self):
        self.back_ground = ImageTk.PhotoImage(Image.open("black.jpg"))
        self.title_image = ImageTk.PhotoImage(Image.open("1686910307677.jpeg"))
        self.top_image = ImageTk.PhotoImage(Image.open("images.png"))
        self.vs_image = ImageTk.PhotoImage(Image.open("vs-41932 (1).png"))
        self.vs_image1 = ImageTk.PhotoImage(Image.open("vs-41932 (1).png"))
        self.small_hand_image =ImageTk.PhotoImage(Image.open("1686910307649(1).png"))
        self.small_hand_image1 = ImageTk.PhotoImage(Image.open("1686910307662 (2).png"))
        self.small_hand_image2 = ImageTk.PhotoImage(Image.open("1686910307669 (2).png"))
        self.small_image1 = ImageTk.PhotoImage(Image.open("images (1) (1).png"))
        self.small_image2 = ImageTk.PhotoImage(Image.open("images (1) (1).png"))
        self.small_user_image=ImageTk.PhotoImage(Image.open("computer_rock(1).png"))
        self.small_vs_image = ImageTk.PhotoImage(Image.open("vs-41932 (1) (1).png"))
        self.small_computer_image = ImageTk.PhotoImage(Image.open("computer_scissor(1).png"))
        self.cup_image = ImageTk.PhotoImage(Image.open("1687187580136.png"))
        #for user
        self.rock_img = ImageTk.PhotoImage(Image.open("rock_image.png"))
        self.paper_img = ImageTk.PhotoImage(Image.open("paper_image.png"))
        self.scissor_img = ImageTk.PhotoImage(Image.open("sissor_image.png"))
        #for computer
        self.computer_rock_img = ImageTk.PhotoImage(Image.open("computer_rock.png"))
        self.computer_paper_img = ImageTk.PhotoImage(Image.open("computer_paper.png"))
        self.computer_scissor_img = ImageTk.PhotoImage(Image.open("computer_scissor.png"))
        #for hand user
        self.user_hand_paper = ImageTk.PhotoImage(Image.open("1686910307662 (3).png"))
        self.user_hand_rock = ImageTk.PhotoImage(Image.open("1686910307649(3).png"))
        self.user_hand_scissor = ImageTk.PhotoImage(Image.open("1686910307669 (3).png"))
        #for hand computer
        self.computer_hand_paper = ImageTk.PhotoImage(Image.open("computer_hand_paper.png"))
        self.computer_hand_rock = ImageTk.PhotoImage(Image.open("computer_hand_rock.png"))
        self.computer_hand_scissor = ImageTk.PhotoImage(Image.open("compuer_hand_scossor.png")) 
        self.title = tk.Label(text="",font="Helvetica 18 bold",bg="black",fg="yellow")
        self.title.place(x=580,y=40)
        
    def tab1(self):
        self.back_label = tk.Label(game,image=self.back_ground)
        self.back_label.place(x=0,y=0)
        self.how_to = tk.Label(game,text="",font="Helvetica 20 bold",bg="black",fg="yellow")
        self.how_to.place(x=500,y=30)
        self.rock_paper_scissor = tk.Label(game,text="",font="Helvetica 20 bold",bg="black",fg="yellow")
        self.rock_paper_scissor.place(x=50,y=100)
        self.line1 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line1.place(x=80,y=130)
        self.line2 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line2.place(x=80,y=160)
        self.line3 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line3.place(x=80,y=190)
        self.line4 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line4.place(x=80,y=220)
        self.line5 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line5.place(x=80,y=250)
        self.line6 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line6.place(x=80,y=280)
        self.line7 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line7.place(x=80,y=310)
        self.line8 = tk.Label(game,text="",font="Helvetica 20 bold",bg="black",fg="yellow")
        self.line8.place(x=50,y=500)
        self.line9 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="deeppink")
        self.line9.place(x=80,y=530)
        self.line10 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="deeppink")
        self.line10.place(x=80,y=560)
        self.line11 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="deeppink")
        self.line11.place(x=80,y=590)
        self.line12 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.line12.place(x=80,y=620)
        self.home = tk.Button(text="",height=1,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home.tab1())
        self.home.place(x=1100,y=660)
        self.replay = tk.Button(text="",height=1,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home.tab1())
        self.replay.place(x=1100,y=660)
        self.small = tk.Label(game,height=150,width=150,bg="black")
        self.small.place(x=300,y=340)
        self.small_title = tk.Label(text="",font="Helvetica 12 bold",bg="black",fg="deeppink")
        self.small_title.place(x=300,y=490)
        self.small1 = tk.Label(game,height=150,width=150,bg="black")
        self.small1.place(x=600,y=340)
        self.small_title1 = tk.Label(text="",font="Helvetica 12 bold",bg="black",fg="deeppink")
        self.small_title1.place(x=600,y=490)
        self.small2 = tk.Label(game,height=150,width=150,bg="black")
        self.small2.place(x=900,y=340)
        self.small_title2 = tk.Label(text="",font="Helvetica 12 bold",bg="black",fg="deeppink")
        self.small_title2.place(x=900,y=490)
        self.title_label = tk.Label(image=self.title_image,height=415,width=739,bg="white")
        self.title_label.place(x=300,y=80)
        self.name = tk.Label(text="ENTER YOUR NAME HERE:",font="Helvetica 18 bold",bg="black",fg="white")
        self.name.place(x=310,y=520)
        self.input = tk.StringVar()
        self.my_text = tk.Entry(game,textvariable=self.input,font="Helvetica 18 bold")
        self.my_text.place(x=630,y=519)
        self.thulasi1 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        self.thulasi1.place(x=180,y=60)
        self.start = tk.Button(text="PLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home.secondpage())
        self.start.place(x=317,y=570)
        self.mode = tk.Button(text="MODE",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.modes())
        self.mode.place(x=502,y=570)
        self.exit = tk.Button(text="EXIT",height=2,width=15,command=lambda:game.quit(),bg="red",fg="white",font="Helvetica 12 bold")
        self.exit.place(x=687,y=570)
        self.how = tk.Button(text="HOW TO PLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.how_play())
        self.how.place(x=877,y=570)

    def secondpage(self):
        self.name.destroy()
        self.my_text.destroy()
        self.start.destroy()
        self.exit.destroy()
        self.mode.destroy()
        self.how.destroy()
        self.home.destroy()
        self.replay.destroy()
        print(self.input.get())
        self.title_label.destroy()
        self.thulasi1.configure(text=self.input.get())
        self.cup_label = tk.Label(game,height=400,width=350,bg="black")
        self.cup_label.place(x=520,y=100)
        self.user_label = tk.Label(image=self.rock_img,bg="black",height=350,width=350)
        self.user_label.place(x=150,y=200)
        self.computer_label = tk.Label(image=self.computer_scissor_img,bg="black",height=350,width=350)
        self.computer_label.place(x=950,y=200)
        self.top_label = tk.Label(image=self.top_image,height=160,width=470,bg="darkblue")
        self.top_label.place(x=450,y=10)
        self.user_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
        self.computer_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
        self.user_score.place(x=400,y=60)
        self.computer_score.place(x=1200,y=60)
        self.score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 18 bold")
        self.score1.place(x=960,y=60)
        self.vs_label = tk.Label(image=self.vs_image,height=150,width=150,bg="black")
        self.vs_label.place(x=640,y=300)
        self.user_win = tk.Label(text="",bg="black",fg="white",font="Helvetica 18 bold")
        self.user_win.place(x=530,y=500)
        thulasi = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        thulasi.place(x=1250,y=60)

        def count():
            t= 10
            while t:
                mins = t//60
                secs = t%60
                timer = '{:02d}:{:02d}'.format(mins,secs)
                print(timer,end="\r")
                t -= 1
                thulasi.config(text=timer)
                game.update()
                time.sleep(1) 
            print(timer)
            if timer == "00:01":
                self.user_score["text"] = int(self.user_score["text"])
                self.computer_score["text"] = int(self.computer_score["text"])
                if self.user_score["text"] < self.computer_score["text"]:
                    computer_win()
                if self.computer_score["text"] < self.user_score["text"]:
                    win()
                

        #for computer win
        def computer_win():
            self.title_label.destroy()
            self.name.destroy()
            self.start.destroy()
            self.exit.destroy()
            self.mode.destroy()
            self.how.destroy()
            thulasi.destroy()
            self.my_text.destroy()
            self.computer_label.destroy()
            self.user_label.destroy()
            self.top_label.destroy()
            self.vs_label.destroy()
            rock.destroy()
            paper.destroy()
            scissor.destroy()
            self.cup_label.configure(image=self.cup_image)
            self.title.configure(text="CONGRATULATION")
            self.user_win = tk.Label(text="SORRY COMPUTER IS A WIN 👎",bg="black",fg="white",font="Helvetica 18 bold")
            self.user_win.place(x=530,y=500)
            self.replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.secondpage())
            self.replay.place(x=470,y=610)
            self.home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
            self.home.place(x=720,y=610)

        def win():
            self.title_label.destroy()
            self.name.destroy()
            self.start.destroy()
            self.exit.destroy()
            self.my_text.destroy()
            self.mode.destroy()
            self.how.destroy()
            thulasi.destroy()
            self.computer_label.destroy()
            self.user_label.destroy()
            self.top_label.destroy()
            self.vs_label.destroy()
            rock.destroy()
            paper.destroy()
            scissor.destroy()
            self.cup_label.configure(image=self.cup_image)
            self.title.configure(text="CONGRATULATION")
            self.user_win = tk.Label(text="YOU ARE A WIN 👍",bg="black",fg="white",font="Helvetica 18 bold")
            self.user_win.place(x=530,y=500)
            self.replay = tk.Button(text="REPLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.secondpage())
            self.replay.place(x=480,y=610)
            self.home = tk.Button(text="HOME",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
            self.home.place(x=720,y=610)
        #updateuserscore
        def update_score():
            score = int(self.user_score["text"])
            score += 1
            self.user_score["text"] = str(score)
            mark = self.user_score["text"]
        #updatecomputerscore
        def update_computer_score():
            score = int(self.computer_score["text"])
            score += 1
            self.computer_score["text"] = str(score)

        #checkwinner
        def checkwinner(player,computer,):
            if player == computer:
                pass
            if player == "ROCK":
                if computer == "PAPER":
                    update_computer_score()
            if player == "ROCK":
                if computer == "SCISSOR":
                    update_score()
            if player == "PAPER":
                if computer == "ROCK":
                    update_score()
            if player == "PAPER":
                if computer == "SCISSOR":
                    update_computer_score()
            if player == "SCISSOR":
                if computer == "PAPER":
                    update_score()
            if player == "SCISSOR":
                if computer == "ROCK":
                    update_computer_score() 
            else:
                pass
        choice = ["ROCK","SCISSOR","PAPER"]
        def user(x):
            #FOR COMPUTER
            computerChoice = choice[randint(0,2)]
            if computerChoice == "ROCK":
                self.computer_label.configure(image=self.computer_rock_img)
            elif computerChoice == "SCISSOR":
                self.computer_label.configure(image=self.computer_scissor_img)
            elif computerChoice == "PAPER":
                self.computer_label.configure(image=self.computer_paper_img)

            #FOR USER
            if x == "ROCK":
                self.user_label.configure(image=self.rock_img)
            elif x == "SCISSOR":
                self.user_label.configure(image=self.scissor_img)
            elif x == "PAPER":
                self.user_label.configure(image=self.paper_img)
            checkwinner(x,computerChoice)
        rock = tk.Button(text="ROCK",height=1,width=10,command=lambda:user("ROCK"),bg="deepskyblue",font="Helvetica 18 bold",fg="white")
        rock.place(x=430,y=590)
        scissor = tk.Button(text="SCISSOR",height=1,width=10,command=lambda:user("SCISSOR"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
        scissor.place(x=630,y=590)
        paper = tk.Button(text="PAPER",height=1,width=10,command=lambda:user("PAPER"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
        paper.place(x=830,y=590)
        count()
    def modes(self):
        self.title_label.destroy()
        self.name.destroy()
        self.my_text.destroy()
        self.start.destroy()
        self.exit.destroy()
        self.mode.destroy()
        self.how.destroy()
        self.top_label1 = tk.Label(image=self.top_image,height=160,width=470,bg="darkblue")
        self.top_label1.place(x=450,y=10)
        self.selection = tk.Label(text="SELECTION MODES",bg="black",fg="lime",font="Helvetica 18 bold")
        self.selection.place(x=578,y=190)
        object = tk.Button(text="OBJECT MODE",height=1,width=15,bg="deeppink",fg="white",font="Helvetica 12 bold",command=lambda:home1())
        object.place(x=300,y=630)
        hands = tk.Button(text="HAND MODE",height=1,width=15,command=lambda:hand(),bg="deeppink",fg="white",font="Helvetica 12 bold")
        hands.place(x=895,y=630)
        self.box = tk.Label(game,height=25,width=85,bg="green")
        self.box.place(x=70,y=230)
        self.small_lebel1 = tk.Label(image=self.small_image1,height=90,width=150,bg="black")
        self.small_lebel1.place(x=300,y=250)
        self.small_user_score = tk.Label(text="USER SCORE",font="Helvetica 7 bold")
        self.small_user_score.place(x=150,y=280)
        self.small_user_score_text = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        self.small_user_score_text.place(x=225,y=280)
        self.small_computer_score = tk.Label(text="COMPUTER SCORE",font="Helvetica 7 bold")
        self.small_computer_score.place(x=510,y=280)
        self.small_computer_score_text = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        self.small_computer_score_text.place(x=610,y=280)
        self.small_user_label = tk.Label(image=self.small_user_image,bg="green",height=150,width=150)
        self.small_user_label.place(x=105,y=365)
        self.small_vs_label = tk.Label(image=self.small_vs_image,height=50,width=50,bg="black")
        self.small_vs_label.place(x=340,y=420)
        self.small_computer_label = tk.Label(image=self.small_computer_image,height=150,width=150,bg="green")
        self.small_computer_label.place(x=480,y=365)
        self.box1 = tk.Label(game,height=25,width=85,bg="green")
        self.box1.place(x=700,y=230)
        self.small_top_label = tk.Label(image=self.small_image2,height=90,width=150,bg="black")
        self.small_top_label.place(x=930,y=250)
        self.small_user_score1 = tk.Label(text="USER SCORE",font="Helvetica 7 bold")
        self.small_user_score1.place(x=780,y=280)
        self.small_user_score_text1 = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        self.small_user_score_text1.place(x=855,y=280)
        self.small_computer_score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 7 bold")
        self.small_computer_score1.place(x=1140,y=280)
        self.small_computer_score_text1 = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        self.small_computer_score_text1.place(x=1240,y=280)
        self.small_hand_label = tk.Label(image=self.small_hand_image,height=150,width=150,bg="green")
        self.small_hand_label.place(x=735,y=365)
        self.small_hand_label1 = tk.Label(image=self.small_hand_image1,height=150,width=150,bg="green")
        self.small_hand_label1.place(x=1110,y=365)
        self.small_vs_label1 = tk.Label(image=self.small_vs_image,height=50,width=50,bg="black")
        self.small_vs_label1.place(x=970,y=420)
        thulasi = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        thulasi.place(x=1250,y=60)

        def home1():
            self.top_label1.destroy()
            self.selection.destroy()
            object.destroy()
            hands.destroy()
            self.box.destroy()
            self.small_user_label.destroy()
            self.small_user_score.destroy()
            self.small_lebel1.destroy()
            self.small_user_score1.destroy()
            self.small_user_score_text.destroy()
            self.small_user_score_text1.destroy()
            self.small_computer_score.destroy()
            self.small_computer_score1.destroy()
            self.small_computer_score_text.destroy()
            self.small_computer_score_text1.destroy()
            self.small_user_label.destroy()
            self.small_vs_label.destroy()
            self.small_vs_label1.destroy()
            self.small_top_label.destroy()
            self.small_hand_label.destroy()
            self.small_hand_label1.destroy()
            self.small_computer_label.destroy()
            self.box1.destroy()
            self.title = tk.Label(game,font="Helvetica 18 bold",bg="black",fg="yellow")
            self.title.place(x=580,y=40)
            self.cup_label = tk.Label(game,height=400,width=350,bg="black")
            self.cup_label.place(x=520,y=100)
            self.user_label = tk.Label(image=self.rock_img,bg="black",height=350,width=350)
            self.user_label.place(x=150,y=200)
            self.computer_label = tk.Label(image=self.computer_scissor_img,bg="black",height=350,width=350)
            self.computer_label.place(x=950,y=200)
            self.top_label = tk.Label(image=self.top_image,height=160,width=470,bg="darkblue")
            self.top_label.place(x=450,y=10)
            user_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            computer_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            user_score.place(x=400,y=60)
            computer_score.place(x=1200,y=60)
            score = tk.Label(text="USER SCORE",font="Helvetica 18 bold")
            score.place(x=230,y=60)
            self.score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 18 bold")
            self.score1.place(x=940,y=60)
            self.vs_label = tk.Label(image=self.vs_image,height=150,width=150,bg="black")
            self.vs_label.place(x=640,y=300)
            
            def count():
                t= 10
                while t:
                    mins = t//60
                    secs = t%60
                    timer = '{:02d}:{:02d}'.format(mins,secs)
                    print(timer,end="\r")
                    t -= 1
                    thulasi.config(text=timer)
                    game.update()
                    time.sleep(1) 

                print(timer)
                if timer == "00:01":
                    user_score["text"] = int(user_score["text"])
                    computer_score["text"] = int(computer_score["text"])
                    if user_score["text"] < computer_score["text"]:
                        computer_win()
                    if computer_score["text"] < user_score["text"]:
                        win()
                    

            #for computer win
            def computer_win():
                self.top_label.destroy()
                self.name.destroy()
                self.my_text.destroy()
                self.start.destroy()
                self.exit.destroy()
                self.mode.destroy()
                self.how.destroy()
                self.thulasi.destroy()
                self.thulasi1.destroy()
                self.user_label.destroy()
                self.computer_label.destroy()
                user_score.destroy()
                self.vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                self.cup_label.configure(image=self.cup_image)
                self.title.configure(text="CONGRATULATION")
                self.user_win = tk.Label(text="SORRY COMPUTER IS A WIN 👍",bg="black",fg="white",font="Helvetica 18 bold")
                self.user_win.place(x=530,y=500)
                replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home1())
                replay.place(x=470,y=610)
                home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
                home.place(x=720,y=610)

            def win():
                self.top_label.destroy()
                self.name.destroy()
                self.my_text.destroy()
                self.start.destroy()
                self.exit.destroy()
                self.mode.destroy()
                self.how.destroy()
                self.thulasi.destroy()
                self.thulasi1.destroy()
                self.user_label.destroy()
                self.computer_label.destroy()
                self.vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                self.cup_label.configure(image=self.cup_image)
                self.title.configure(text="CONGRATULATION")
                self.user_win = tk.Label(text="YOUR ARE A WIN 👍",bg="black",fg="white",font="Helvetica 18 bold")
                self.user_win.place(x=530,y=500)
                replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home1())
                replay.place(x=480,y=610)
                home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
                home.place(x=720,y=610)
                
            #updateuserscore
            def update_score():
                score = int(user_score["text"])
                score += 1
                user_score["text"] = str(score)

            #updatecomputerscore
            def update_computer_score():
                score = int(computer_score["text"])
                score += 1
                computer_score["text"] = str(score)

            #checkwinner
            def checkwinner(player,computer,):
                if player == computer:
                    pass
                if player == "ROCK":
                    if computer == "PAPER":
                        update_computer_score()
                if player == "ROCK":
                    if computer == "SCISSOR":
                        update_score()
                if player == "PAPER":
                    if computer == "ROCK":
                        update_score()
                if player == "PAPER":
                    if computer == "SCISSOR":
                        update_computer_score()
                if player == "SCISSOR":
                    if computer == "PAPER":
                        update_score()
                if player == "SCISSOR":
                    if computer == "ROCK":
                        update_computer_score() 
                else:
                    pass
            choice = ["ROCK","SCISSOR","PAPER"]
            def user(x):
                #FOR COMPUTER
                computerChoice = choice[randint(0,2)]
                if computerChoice == "ROCK":
                    self.computer_label.configure(image=self.computer_rock_img)
                elif computerChoice == "SCISSOR":
                    self.computer_label.configure(image=self.computer_scissor_img)
                elif computerChoice == "PAPER":
                    self.computer_label.configure(image=self.computer_paper_img)

                #FOR USER
                if x == "ROCK":
                    self.user_label.configure(image=self.rock_img)
                elif x == "SCISSOR":
                    self.user_label.configure(image=self.scissor_img)
                elif x == "PAPER":
                    self.user_label.configure(image=self.paper_img)
                checkwinner(x,computerChoice)   
            rock = tk.Button(text="ROCK",height=1,width=10,command=lambda:user("ROCK"),bg="deepskyblue",font="Helvetica 18 bold",fg="white")
            rock.place(x=430,y=590)
            scissor = tk.Button(text="SCISSOR",height=1,width=10,command=lambda:user("SCISSOR"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            scissor.place(x=630,y=590)
            paper = tk.Button(text="PAPER",height=1,width=10,command=lambda:user("PAPER"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            paper.place(x=830,y=590)
            count()


        def hand():
            self.top_label1.destroy()
            self.selection.destroy()
            object.destroy()
            hands.destroy()
            self.small_vs_label1.destroy()
            self.small_vs_label.destroy()
            self.small_top_label.destroy()
            self.small_lebel1.destroy()
            self.small_computer_label.destroy()
            self.small_user_label.destroy()
            self.small_user_score.destroy()
            self.small_computer_score.destroy()
            self.small_user_score_text.destroy()
            self.small_user_score_text1.destroy()
            self.small_computer_score_text.destroy()
            self.small_computer_score_text1.destroy()
            self.small_computer_score.destroy()
            self.small_user_score1.destroy()
            self.small_computer_score1.destroy()
            self.small_user_score1.destroy()
            self.small_computer_score1.destroy()
            self.box.destroy()
            self.box1.destroy()
            self.small_hand_label.destroy()
            self.small_hand_label1.destroy()
            self.title = tk.Label(game,font="Helvetica 18 bold",bg="black",fg="yellow")
            self.title.place(x=580,y=40)
            self.user_win = tk.Label(game,bg="black",fg="white",font="Helvetica 18 bold")
            self.user_win.place(x=530,y=500)
            self.cup_label = tk.Label(game,height=400,width=350,bg="black")
            self.cup_label.place(x=520,y=100)
            self.user_label = tk.Label(image=self.user_hand_paper,bg="black",height=350,width=350)
            self.user_label.place(x=150,y=200)
            self.computer_label = tk.Label(image=self.computer_hand_scissor,bg="black",height=350,width=350)
            self.computer_label.place(x=950,y=200)
            self.top_label = tk.Label(image=self.top_image,height=160,width=470,bg="darkblue")
            self.top_label.place(x=450,y=10)
            user_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            computer_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            user_score.place(x=400,y=60)
            computer_score.place(x=1200,y=60)
            self.score = tk.Label(text="USER SCORE",font="Helvetica 18 bold")
            self.score.place(x=230,y=60)
            self.score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 18 bold")
            self.score1.place(x=960,y=60)
            self.vs_label = tk.Label(image=self.vs_image,height=150,width=150,bg="black")
            self.vs_label.place(x=640,y=300)

            def count():
                t= 10
                while t:
                    mins = t//60
                    secs = t%60
                    timer = '{:02d}:{:02d}'.format(mins,secs)
                    print(timer,end="\r")
                    t -= 1
                    thulasi.config(text=timer)
                    game.update()
                    time.sleep(1) 

                print(timer)
                if timer == "00:01":
                    user_score["text"] = int(user_score["text"])
                    computer_score["text"] = int(computer_score["text"])
                    if user_score["text"] < computer_score["text"]:
                        computer_win()
                    if computer_score["text"] < user_score["text"]:
                        win()
                    

            #for computer win
            def computer_win():
                self.top_label.destroy()
                self.name.destroy()
                self.my_text.destroy()
                self.start.destroy()
                self.exit.destroy()
                self.mode.destroy()
                self.how.destroy()
                self.thulasi.destroy()
                self.thulasi1.destroy()
                self.user_label.destroy()
                self.computer_label.destroy()
                self.vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                self.cup_label.configure(image=self.cup_image)
                self.title.configure(text="CONGRATULATION")
                self.user_win = tk.Label(text="SORRY COMPUTER IS A WIN 👍",bg="black",fg="white",font="Helvetica 18 bold")
                self.user_win.place(x=530,y=500)
                replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:hand())
                replay.place(x=470,y=610)
                home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
                home.place(x=720,y=610)

            def win():
                self.top_label.destroy()
                self.name.destroy()
                self.my_text.destroy()
                self.start.destroy()
                self.exit.destroy()
                self.mode.destroy()
                self.how.destroy()
                self.thulasi.destroy()
                self.thulasi1.destroy()
                self.user_label.destroy()
                self.computer_label.destroy()
                self.vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                self.cup_label.configure(image=self.cup_image)
                self.title.configure(text="CONGRATULATION")
                self.user_win = tk.Label(text="YOUR ARE A WIN 👍",bg="black",fg="white",font="Helvetica 18 bold")
                self.user_win.place(x=530,y=500)
                replay = tk.Button(text="REPLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:hand())
                replay.place(x=480,y=610)
                home = tk.Button(text="HOME",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
                home.place(x=720,y=610)




            #updateuserscore
            def update_score():
                score = int(user_score["text"])
                score += 1
                user_score["text"] = str(score)

            #updatecomputerscore
            def update_computer_score():
                score = int(computer_score["text"])
                score += 1
                computer_score["text"] = str(score)

            #checkwinner
            def checkwinner(player,computer,):
                if player == computer:
                    pass
                if player == "ROCK":
                    if computer == "PAPER":
                        update_computer_score()
                if player == "ROCK":
                    if computer == "SCISSOR":
                        update_score()
                if player == "PAPER":
                    if computer == "ROCK":
                        update_score()
                if player == "PAPER":
                    if computer == "SCISSOR":
                        update_computer_score()
                if player == "SCISSOR":
                    if computer == "PAPER":
                        update_score()
                if player == "SCISSOR":
                    if computer == "ROCK":
                        update_computer_score() 
                else:
                    pass
            choice = ["ROCK","SCISSOR","PAPER"]
            def user(x):
                #FOR COMPUTER
                computerChoice = choice[randint(0,2)]
                if computerChoice == "ROCK":
                    self.computer_label.configure(image=self.computer_hand_rock)
                elif computerChoice == "SCISSOR":
                    self.computer_label.configure(image=self.computer_hand_scissor)
                elif computerChoice == "PAPER":
                    self.computer_label.configure(image=self.computer_hand_paper)

                #FOR USER
                if x == "ROCK":
                    self.user_label.configure(image=self.user_hand_rock)
                elif x == "SCISSOR":
                    self.user_label.configure(image=self.user_hand_scissor)
                elif x == "PAPER":
                    self.user_label.configure(image=self.user_hand_paper)
                checkwinner(x,computerChoice)
        
            rock = tk.Button(text="ROCK",height=1,width=10,command=lambda:user("ROCK"),bg="deepskyblue",font="Helvetica 18 bold",fg="white")
            rock.place(x=430,y=590)
            scissor = tk.Button(text="SCISSOR",height=1,width=10,command=lambda:user("SCISSOR"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            scissor.place(x=630,y=590)
            paper = tk.Button(text="PAPER",height=1,width=10,command=lambda:user("PAPER"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            paper.place(x=830,y=590)
            count()
    def how_play(self):
        self.title_label.destroy()
        self.name.destroy()
        self.my_text.destroy()
        self.start.destroy()
        self.exit.destroy()
        self.mode.destroy()
        self.how.destroy()
        self.how_to.configure(text="HOW TO PLAY THIS GAME")
        self.rock_paper_scissor.configure(text="ROCK PAPER SCISSOR")
        self.line1.config(text="Rock-Paper-Scissors is a game played to settle disputes between two people.")
        self.line2.config(text="Thought to be a game of chance that depends on random luck similar to flipping coins drawing straws.")
        self.line3.config(text="The game is often taught to children to help them adult intervention.")
        self.line4.config(text="However, the game actually can be a game that  skill that requires quick thinking and perceptive reasoning.")
        self.line5.config(text="The game is played with three possible hand signals that represent a rock, paper, and scissors.")
        self.line6.config(text="The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward.")
        self.line7.config(text="Scissors is a fist with the index and middle fingers fully extended toward the opposing player.")
        self.line8.config(text="RULES")
        self.line9.config(text="Rock wins against Scissors")
        self.line10.config(text="Paper wins against Rock")
        self.line11.config(text="Scissors wins against Paper")
        self.line12.config(text="If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner.")
        home = tk.Button(text="HOME",height=1,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:self.tab1())
        home.place(x=1100,y=660)
        self.small.configure(image=self.small_hand_image)
        self.small1.configure(image=self.small_hand_image1)
        self.small2.configure(image=self.small_hand_image2)
        self.small_title.configure(text="ROCK")
        self.small_title1.configure(text="PAPER")
        self.small_title2.configure(text="SCISSOR")


home = rock_paper_scissor()
home.tab1()
game.mainloop()