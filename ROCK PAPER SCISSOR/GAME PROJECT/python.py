import tkinter as tk
from PIL import Image,ImageTk
from random import randint
import time


game = tk.Tk()

game.title("STINY GAMES")
game.configure(background="black")
title_image = ImageTk.PhotoImage(Image.open("1686910307677.jpeg"))
top_image = ImageTk.PhotoImage(Image.open("images.png"))
vs_image = ImageTk.PhotoImage(Image.open("vs-41932 (1).png"))
vs_image1 = ImageTk.PhotoImage(Image.open("vs-41932 (1).png"))
small_hand_image =ImageTk.PhotoImage(Image.open("1686910307649(1).png"))
small_hand_image1 = ImageTk.PhotoImage(Image.open("1686910307662 (2).png"))
small_hand_image2 = ImageTk.PhotoImage(Image.open("1686910307669 (2).png"))
small_image1 = ImageTk.PhotoImage(Image.open("images (1) (1).png"))
small_image2 = ImageTk.PhotoImage(Image.open("images (1) (1).png"))
small_user_image=ImageTk.PhotoImage(Image.open("computer_rock(1).png"))
small_vs_image = ImageTk.PhotoImage(Image.open("vs-41932 (1) (1).png"))
small_computer_image = ImageTk.PhotoImage(Image.open("computer_scissor(1).png"))
cup_image = ImageTk.PhotoImage(Image.open("1687187580136.png"))
#for user
rock_img = ImageTk.PhotoImage(Image.open("rock_image.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_image.png"))
scissor_img = ImageTk.PhotoImage(Image.open("sissor_image.png"))
#for computer
computer_rock_img = ImageTk.PhotoImage(Image.open("computer_rock.png"))
computer_paper_img = ImageTk.PhotoImage(Image.open("computer_paper.png"))
computer_scissor_img = ImageTk.PhotoImage(Image.open("computer_scissor.png"))
#for hand user
user_hand_paper = ImageTk.PhotoImage(Image.open("1686910307662 (3).png"))
user_hand_rock = ImageTk.PhotoImage(Image.open("1686910307649(3).png"))
user_hand_scissor = ImageTk.PhotoImage(Image.open("1686910307669 (3).png"))
#for hand computer
computer_hand_paper = ImageTk.PhotoImage(Image.open("computer_hand_paper.png"))
computer_hand_rock = ImageTk.PhotoImage(Image.open("computer_hand_rock.png"))
computer_hand_scissor = ImageTk.PhotoImage(Image.open("compuer_hand_scossor.png")) 

def tab1():
    cup_label = tk.Label(game,height=400,width=350,bg="black")
    cup_label.place(x=520,y=100)
    title = tk.Label(text="",font="Helvetica 18 bold",bg="black",fg="yellow")
    title.place(x=580,y=40)
    user_win = tk.Label(text="",bg="black",fg="white",font="Helvetica 18 bold")
    user_win.place(x=530,y=500)
    how_to = tk.Label(game,text="",font="Helvetica 20 bold",bg="black",fg="yellow")
    how_to.place(x=500,y=30)
    rock_paper_scissor = tk.Label(game,text="",font="Helvetica 20 bold",bg="black",fg="yellow")
    rock_paper_scissor.place(x=50,y=100)
    line1 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line1.place(x=80,y=130)
    line2 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line2.place(x=80,y=160)
    line3 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line3.place(x=80,y=190)
    line4 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line4.place(x=80,y=220)
    line5 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line5.place(x=80,y=250)
    line6 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line6.place(x=80,y=280)
    line7 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line7.place(x=80,y=310)
    line8 = tk.Label(game,text="",font="Helvetica 20 bold",bg="black",fg="yellow")
    line8.place(x=50,y=500)
    line9 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="deeppink")
    line9.place(x=80,y=530)
    line10 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="deeppink")
    line10.place(x=80,y=560)
    line11 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="deeppink")
    line11.place(x=80,y=590)
    line12 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    line12.place(x=80,y=620)
    home = tk.Button(text="",height=1,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
    home.place(x=1100,y=660)
    small = tk.Label(game,height=150,width=150,bg="black")
    small.place(x=300,y=340)
    small_title = tk.Label(text="",font="Helvetica 12 bold",bg="black",fg="deeppink")
    small_title.place(x=300,y=490)
    small1 = tk.Label(game,height=150,width=150,bg="black")
    small1.place(x=600,y=340)
    small_title1 = tk.Label(text="",font="Helvetica 12 bold",bg="black",fg="deeppink")
    small_title1.place(x=600,y=490)
    small2 = tk.Label(game,height=150,width=150,bg="black")
    small2.place(x=900,y=340)
    small_title2 = tk.Label(text="",font="Helvetica 12 bold",bg="black",fg="deeppink")
    small_title2.place(x=900,y=490)

    title_label = tk.Label(image=title_image,height=415,width=739,bg="white")
    title_label.place(x=300,y=80)
    name = tk.Label(text="ENTER YOUR NAME HERE:",font="Helvetica 18 bold",bg="black",fg="white")
    name.place(x=310,y=520)
    input = tk.StringVar()
    my_text = tk.Entry(game,textvariable=input,font="Helvetica 18 bold")
    my_text.place(x=630,y=519)
    thulasi = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    thulasi.place(x=1250,y=60)
    thulasi1 = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
    thulasi1.place(x=180,y=60)

    def secondpage():
        name.destroy()
        my_text.destroy()
        start.destroy()
        exit.destroy()
        mode.destroy()
        how.destroy()
        print(input.get())
        thulasi1.configure(text=input.get())
        title_label.destroy()
        user_label = tk.Label(image=rock_img,bg="black",height=350,width=350)
        user_label.place(x=150,y=200)
        computer_label = tk.Label(image=computer_scissor_img,bg="black",height=350,width=350)
        computer_label.place(x=950,y=200)
        top_label = tk.Label(image=top_image,height=160,width=470,bg="darkblue")
        top_label.place(x=450,y=10)
        user_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
        computer_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
        user_score.place(x=400,y=60)
        computer_score.place(x=1200,y=60)
        score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 18 bold")
        score1.place(x=960,y=60)
        vs_label = tk.Label(image=vs_image,height=150,width=150,bg="black")
        vs_label.place(x=640,y=300)

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
            title_label.destroy()
            name.destroy()
            my_text.destroy()
            start.destroy()
            exit.destroy()
            mode.destroy()
            how.destroy()
            thulasi.destroy()
            thulasi1.destroy()
            computer_label.destroy()
            user_label.destroy()
            top_label.destroy()
            vs_label.destroy()
            rock.destroy()
            paper.destroy()
            scissor.destroy()
            cup_label.configure(image=cup_image)
            title.configure(text="CONGRATULATION")
            user_win.configure(text="SORRY COMPUTER IS WIN 👎")
            replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:secondpage())
            replay.place(x=470,y=610)
            home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
            home.place(x=720,y=610)

        def win():
            title_label.destroy()
            name.destroy()
            my_text.destroy()
            start.destroy()
            exit.destroy()
            mode.destroy()
            how.destroy()
            thulasi.destroy()
            thulasi1.destroy()
            computer_label.destroy()
            user_label.destroy()
            top_label.destroy()
            vs_label.destroy()
            rock.destroy()
            paper.destroy()
            scissor.destroy()
            cup_label.configure(image=cup_image)
            title.configure(text="CONGRATULATION")
            user_win.configure(text="SORRY COMPUTER IS WIN 👎")
            replay = tk.Button(text="REPLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:mode.home1())
            replay.place(x=480,y=610)
            home = tk.Button(text="HOME",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
            home.place(x=720,y=610)
        #updateuserscore
        def update_score():
            score = int(user_score["text"])
            score += 1
            user_score["text"] = str(score)
            mark = user_score["text"]
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
                computer_label.configure(image=computer_rock_img)
            elif computerChoice == "SCISSOR":
                computer_label.configure(image=computer_scissor_img)
            elif computerChoice == "PAPER":
                computer_label.configure(image=computer_paper_img)

            #FOR USER
            if x == "ROCK":
                user_label.configure(image=rock_img)
            elif x == "SCISSOR":
                user_label.configure(image=scissor_img)
            elif x == "PAPER":
                user_label.configure(image=paper_img)
            checkwinner(x,computerChoice)
        rock = tk.Button(text="ROCK",height=1,width=10,command=lambda:user("ROCK"),bg="deepskyblue",font="Helvetica 18 bold",fg="white")
        rock.place(x=430,y=590)
        scissor = tk.Button(text="SCISSOR",height=1,width=10,command=lambda:user("SCISSOR"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
        scissor.place(x=630,y=590)
        paper = tk.Button(text="PAPER",height=1,width=10,command=lambda:user("PAPER"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
        paper.place(x=830,y=590)
        count()

    def modes():
        title_label.destroy()
        name.destroy()
        my_text.destroy()
        start.destroy()
        exit.destroy()
        mode.destroy()
        how.destroy()
        top_label1 = tk.Label(image=top_image,height=160,width=470,bg="darkblue")
        top_label1.place(x=450,y=10)
        selection = tk.Label(text="SELECTION MODES",bg="black",fg="lime",font="Helvetica 18 bold")
        selection.place(x=578,y=190)
        object = tk.Button(text="OBJECT MODE",height=1,width=15,bg="deeppink",fg="white",font="Helvetica 12 bold",command=lambda:home1())
        object.place(x=300,y=630)
        hands = tk.Button(text="HAND MODE",height=1,width=15,command=lambda:hand(),bg="deeppink",fg="white",font="Helvetica 12 bold")
        hands.place(x=895,y=630)
        box = tk.Label(game,height=25,width=85,bg="green")
        box.place(x=70,y=230)
        small_lebel1 = tk.Label(image=small_image1,height=90,width=150,bg="black")
        small_lebel1.place(x=300,y=250)
        small_user_score = tk.Label(text="USER SCORE",font="Helvetica 7 bold")
        small_user_score.place(x=150,y=280)
        small_user_score_text = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        small_user_score_text.place(x=225,y=280)
        small_computer_score = tk.Label(text="COMPUTER SCORE",font="Helvetica 7 bold")
        small_computer_score.place(x=510,y=280)
        small_computer_score_text = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        small_computer_score_text.place(x=610,y=280)
        small_user_label = tk.Label(image=small_user_image,bg="green",height=150,width=150)
        small_user_label.place(x=105,y=365)
        small_vs_label = tk.Label(image=small_vs_image,height=50,width=50,bg="black")
        small_vs_label.place(x=340,y=420)
        small_computer_label = tk.Label(image=small_computer_image,height=150,width=150,bg="green")
        small_computer_label.place(x=480,y=365)
        box1 = tk.Label(game,height=25,width=85,bg="green")
        box1.place(x=700,y=230)
        small_top_label = tk.Label(image=small_image2,height=90,width=150,bg="black")
        small_top_label.place(x=930,y=250)
        small_user_score1 = tk.Label(text="USER SCORE",font="Helvetica 7 bold")
        small_user_score1.place(x=780,y=280)
        small_user_score_text1 = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        small_user_score_text1.place(x=855,y=280)
        small_computer_score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 7 bold")
        small_computer_score1.place(x=1140,y=280)
        small_computer_score_text1 = tk.Label(text=0,font="Helvetica 7 bold",bg="green",fg="white")
        small_computer_score_text1.place(x=1240,y=280)
        small_hand_label = tk.Label(image=small_hand_image,height=150,width=150,bg="green")
        small_hand_label.place(x=735,y=365)
        small_hand_label1 = tk.Label(image=small_hand_image1,height=150,width=150,bg="green")
        small_hand_label1.place(x=1110,y=365)
        small_vs_label1 = tk.Label(image=small_vs_image,height=50,width=50,bg="black")
        small_vs_label1.place(x=970,y=420)
        thulasi = tk.Label(game,text="",font="Helvetica 18 bold",bg="black",fg="white")
        thulasi.place(x=1250,y=60)

        def home1():
            top_label1.destroy()
            selection.destroy()
            object.destroy()
            hands.destroy()
            box.destroy()
            small_user_label.destroy()
            small_user_score.destroy()
            small_lebel1.destroy()
            small_user_score1.destroy()
            small_user_score_text.destroy()
            small_user_score_text1.destroy()
            small_computer_score.destroy()
            small_computer_score1.destroy()
            small_computer_score_text.destroy()
            small_computer_score_text1.destroy()
            small_user_label.destroy()
            small_vs_label.destroy()
            small_vs_label1.destroy()
            small_top_label.destroy()
            small_hand_label.destroy()
            small_hand_label1.destroy()
            small_computer_label.destroy()
            box1.destroy()
            title = tk.Label(game,font="Helvetica 18 bold",bg="black",fg="yellow")
            title.place(x=580,y=40)
            user_win = tk.Label(game,bg="black",fg="white",font="Helvetica 18 bold")
            user_win.place(x=530,y=500)
            cup_label = tk.Label(game,height=400,width=350,bg="black")
            cup_label.place(x=520,y=100)
            user_label = tk.Label(image=rock_img,bg="black",height=350,width=350)
            user_label.place(x=150,y=200)
            computer_label = tk.Label(image=computer_scissor_img,bg="black",height=350,width=350)
            computer_label.place(x=950,y=200)
            top_label = tk.Label(image=top_image,height=160,width=470,bg="darkblue")
            top_label.place(x=450,y=10)
            user_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            computer_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            user_score.place(x=400,y=60)
            computer_score.place(x=1200,y=60)
            score = tk.Label(text="USER SCORE",font="Helvetica 18 bold")
            score.place(x=230,y=60)
            score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 18 bold")
            score1.place(x=940,y=60)
            vs_label = tk.Label(image=vs_image,height=150,width=150,bg="black")
            vs_label.place(x=640,y=300)
            
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
                top_label.destroy()
                name.destroy()
                my_text.destroy()
                start.destroy()
                exit.destroy()
                mode.destroy()
                how.destroy()
                thulasi.destroy()
                thulasi1.destroy()
                user_label.destroy()
                computer_label.destroy()
                user_score.destroy()
                vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                cup_label.configure(image=cup_image)
                title.configure(text="CONGRATULATION")
                user_win.configure(text="SORRY COMPUTER IS WIN 👎")
                replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home1())
                replay.place(x=470,y=610)
                home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
                home.place(x=720,y=610)

            def win():
                top_label.destroy()
                name.destroy()
                my_text.destroy()
                start.destroy()
                exit.destroy()
                mode.destroy()
                how.destroy()
                thulasi.destroy()
                thulasi1.destroy()
                user_label.destroy()
                computer_label.destroy()
                vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                cup_label.configure(image=cup_image)
                title.configure(text="CONGRATULATION")
                user_win.configure(text="SORRY COMPUTER IS WIN 👎")
                replay = tk.Button(text="REPLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home1())
                replay.place(x=480,y=610)
                home = tk.Button(text="HOME",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
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
                    computer_label.configure(image=computer_rock_img)
                elif computerChoice == "SCISSOR":
                    computer_label.configure(image=computer_scissor_img)
                elif computerChoice == "PAPER":
                    computer_label.configure(image=computer_paper_img)

                #FOR USER
                if x == "ROCK":
                    user_label.configure(image=rock_img)
                elif x == "SCISSOR":
                    user_label.configure(image=scissor_img)
                elif x == "PAPER":
                    user_label.configure(image=paper_img)
                checkwinner(x,computerChoice)   
            rock = tk.Button(text="ROCK",height=1,width=10,command=lambda:user("ROCK"),bg="deepskyblue",font="Helvetica 18 bold",fg="white")
            rock.place(x=430,y=590)
            scissor = tk.Button(text="SCISSOR",height=1,width=10,command=lambda:user("SCISSOR"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            scissor.place(x=630,y=590)
            paper = tk.Button(text="PAPER",height=1,width=10,command=lambda:user("PAPER"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            paper.place(x=830,y=590)
            count()


        def hand():
            top_label1.destroy()
            selection.destroy()
            object.destroy()
            hands.destroy()
            small_vs_label1.destroy()
            small_vs_label.destroy()
            small_top_label.destroy()
            small_lebel1.destroy()
            small_computer_label.destroy()
            small_user_label.destroy()
            small_user_score.destroy()
            small_computer_score.destroy()
            small_user_score_text.destroy()
            small_user_score_text1.destroy()
            small_computer_score_text.destroy()
            small_computer_score_text1.destroy()
            small_computer_score.destroy()
            small_user_score1.destroy()
            small_computer_score1.destroy()
            small_user_score1.destroy()
            small_computer_score1.destroy()
            box.destroy()
            box1.destroy()
            small_hand_label.destroy()
            small_hand_label1.destroy()
            title = tk.Label(game,font="Helvetica 18 bold",bg="black",fg="yellow")
            title.place(x=580,y=40)
            user_win = tk.Label(game,bg="black",fg="white",font="Helvetica 18 bold")
            user_win.place(x=530,y=500)
            cup_label = tk.Label(game,height=400,width=350,bg="black")
            cup_label.place(x=520,y=100)
            user_label = tk.Label(image=user_hand_paper,bg="black",height=350,width=350)
            user_label.place(x=150,y=200)
            computer_label = tk.Label(image=computer_hand_scissor,bg="black",height=350,width=350)
            computer_label.place(x=950,y=200)
            top_label = tk.Label(image=top_image,height=160,width=470,bg="darkblue")
            top_label.place(x=450,y=10)
            user_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            computer_score = tk.Label(game,text=0,font="Helvetica 18 bold",bg="black",fg="white")
            user_score.place(x=400,y=60)
            computer_score.place(x=1200,y=60)
            score = tk.Label(text="USER SCORE",font="Helvetica 18 bold")
            score.place(x=230,y=60)
            score1 = tk.Label(text="COMPUTER SCORE",font="Helvetica 18 bold")
            score1.place(x=960,y=60)
            vs_label = tk.Label(image=vs_image,height=150,width=150,bg="black")
            vs_label.place(x=640,y=300)

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
                top_label.destroy()
                name.destroy()
                my_text.destroy()
                start.destroy()
                exit.destroy()
                mode.destroy()
                how.destroy()
                thulasi.destroy()
                thulasi1.destroy()
                user_label.destroy()
                computer_label.destroy()
                user_score.destroy()
                vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                cup_label.configure(image=cup_image)
                title.configure(text="CONGRATULATION")
                user_win.configure(text="SORRY COMPUTER IS WIN 👎")
                replay = tk.Button(text="REPLAY",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home1())
                replay.place(x=470,y=610)
                home = tk.Button(text="HOME",height=2,width=20,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
                home.place(x=720,y=610)

            def win():
                top_label.destroy()
                name.destroy()
                my_text.destroy()
                start.destroy()
                exit.destroy()
                mode.destroy()
                how.destroy()
                thulasi.destroy()
                thulasi1.destroy()
                user_label.destroy()
                computer_label.destroy()
                vs_label.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                rock.destroy()
                paper.destroy()
                scissor.destroy()
                cup_label.configure(image=cup_image)
                title.configure(text="CONGRATULATION")
                user_win.configure(text="SORRY COMPUTER IS WIN 👎")
                replay = tk.Button(text="REPLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:home1())
                replay.place(x=480,y=610)
                home = tk.Button(text="HOME",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
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
                    computer_label.configure(image=computer_hand_rock)
                elif computerChoice == "SCISSOR":
                    computer_label.configure(image=computer_hand_scissor)
                elif computerChoice == "PAPER":
                    computer_label.configure(image=computer_hand_paper)

                #FOR USER
                if x == "ROCK":
                    user_label.configure(image=user_hand_rock)
                elif x == "SCISSOR":
                    user_label.configure(image=user_hand_scissor)
                elif x == "PAPER":
                    user_label.configure(image=user_hand_paper)
                checkwinner(x,computerChoice)
        
            rock = tk.Button(text="ROCK",height=1,width=10,command=lambda:user("ROCK"),bg="deepskyblue",font="Helvetica 18 bold",fg="white")
            rock.place(x=430,y=590)
            scissor = tk.Button(text="SCISSOR",height=1,width=10,command=lambda:user("SCISSOR"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            scissor.place(x=630,y=590)
            paper = tk.Button(text="PAPER",height=1,width=10,command=lambda:user("PAPER"),bg="deepskyblue",fg="white",font="Helvetica 18 bold")
            paper.place(x=830,y=590)
            count()

    def how_play():
        title_label.destroy()
        name.destroy()
        my_text.destroy()
        start.destroy()
        exit.destroy()
        mode.destroy()
        how.destroy()
        how_to.configure(text="HOW TO PLAY THIS GAME")
        rock_paper_scissor.configure(text="ROCK PAPER SCISSOR")
        line1.config(text="Rock-Paper-Scissors is a game played to settle disputes between two people.")
        line2.config(text="Thought to be a game of chance that depends on random luck similar to flipping coins drawing straws.")
        line3.config(text="The game is often taught to children to help them adult intervention.")
        line4.config(text="However, the game actually can be a game that  skill that requires quick thinking and perceptive reasoning.")
        line5.config(text="The game is played with three possible hand signals that represent a rock, paper, and scissors.")
        line6.config(text="The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward.")
        line7.config(text="Scissors is a fist with the index and middle fingers fully extended toward the opposing player.")
        line8.config(text="RULES")
        line9.config(text="Rock wins against Scissors")
        line10.config(text="Paper wins against Rock")
        line11.config(text="Scissors wins against Paper")
        line12.config(text="If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner.")
        home = tk.Button(text="HOME",height=1,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:tab1())
        home.place(x=1100,y=660)
        small.configure(image=small_hand_image)
        small1.configure(image=small_hand_image1)
        small2.configure(image=small_hand_image2)
        small_title.configure(text="ROCK")
        small_title1.configure(text="PAPER")
        small_title2.configure(text="SCISSOR")

    start = tk.Button(text="PLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:secondpage())
    start.place(x=317,y=570)
    mode = tk.Button(text="MODE",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:modes())
    mode.place(x=502,y=570)
    exit = tk.Button(text="EXIT",height=2,width=15,command=lambda:game.quit(),bg="red",fg="white",font="Helvetica 12 bold")
    exit.place(x=687,y=570)
    how = tk.Button(text="HOW TO PLAY",height=2,width=15,bg="red",fg="white",font="Helvetica 12 bold",command=lambda:how_play())
    how.place(x=877,y=570)

tab1()
game.mainloop()
