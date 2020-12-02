from datetime import datetime
import datetime as dt
import os
import time,random
from time import time_ns
from tkinter import *
import tkinter as tk
import pyttsx3 as tts
from pyttsx3 import engine
import Greet
import requests,webbrowser
import py8fact
import threading


class UI:
    def __init__(self,screen):
        self.screen = screen
        self.screen.geometry("503x370")
        self.screen.title("Hackathon")
        Label(text="Work-O-Holic", bg="light goldenrod",fg="green", height="3", width="400",font=("arial", 20,'bold')).pack()
        Label(text="").pack()
        x=Listbox(self.screen,width=85,height=7)
        x.insert(1,"General Instructions:")
        x.insert(2,"1. Some functions might need Internet connection")
        x.insert(3,"2. Some functions might load slower because they might not be used directly from application")
        x.insert(4,"3. It may seem to be not responding but the app is hibernated when running.")
        x.insert(5,"4. Do not close the application before you are done working")
        x.insert(6,"5. To close application forcefully, close the command prompt opened with it.")
        x.insert(7,"6. Everything is sequential. Do not press button if not instructed.")
        x.pack()
        Label(text="").pack()
        button=Button(text="Start", height="1", width="10",font=("Helvetica",15),command=self.session)
        button.pack()
        Label(self.screen,text="If you have medicines to be taken please enter time to take it",font=("Helvetica",10)).pack()
        Label(self.screen,text="Format example: 02:00 PM",font=("Helvetica",10)).pack()
        self.medicine=StringVar()
        Entry(self.screen,textvariable=self.medicine).pack()
        
        #screen.mainloop()
    def TTS(self,text):
        self.text=text
        self.engine=tts.init()
        rate = self.engine.getProperty('rate')
        voice = self.engine.getProperty('voices')
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('voice',voice[1].id)
        self.engine.say(str(self.text))
        self.engine.runAndWait()

    def greeting(self):
        x=Greet.x
        y=Greet.t
        z=Greet.d
        self.TTS(x)
        self.TTS(y)
        self.TTS(z)
        
    
    def breathInOut(self):
        for i in range(0,5):
            self.TTS("Breath in")
            time.sleep(3)
            self.TTS("Breath Out")
            time.sleep(3)

        self.TTS("You may enjoy your Virtuo-Physical, stressfree Environment")
        self.sl(2)
        self.TTS("45 Minutes have passed, you should have a quick Stretch, Press Start stretching button")
    def sl(self,mins):
        self.mins=60*mins
        time.sleep(self.mins)

    def session(self):
        try:
            self.screen2 = Toplevel(self.screen)
            self.screen2.geometry("561x578")    
            self.screen2.resizable(width=False, height=False)
            self.screen2.title("Session")
        
            Label(self.screen2,text="Activities", bg="light goldenrod",fg="green", height="2", width="400",font=("arial", 25,'bold')).pack()

            self.greeting()
            self.TTS("Before Starting session, Lets Start with deep breaths\n Press the given button")
            Button(self.screen2, text='Start Deep Breath', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.breathInOutT).place(x=16, y=88)
            Button(self.screen2, text='Start Stretching', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.stretchingT).place(x=296, y=88)
            Button(self.screen2, text='Rotate Body Parts', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.BodyRT).place(x=296, y=158)
            Button(self.screen2, text='Start Jumping', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.JumpingT).place(x=16, y=158)
            Button(self.screen2, text='Yoga Meditation', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.YogaT).place(x=16, y=228)
            Button(self.screen2, text='Read Quotes', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.readingQuoteT).place(x=296, y=228)
            Button(self.screen2, text='Suggest Books', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.readingBookT).place(x=16, y=298)
            Button(self.screen2, text='Read A Joke', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.readingJokeT).place(x=296, y=298)
            Button(self.screen2, text='Read Facts', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.readingFactsT).place(x=16, y=368)
            Button(self.screen2, text='Super Short Nap', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.short_break).place(x=296, y=368)
            Button(self.screen2, text='Talk To Zubaani', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.StressPressT).place(x=16, y=438)
            Button(self.screen2, text='Breath stress out', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.breathExerciseT).place(x=296, y=438)

        except Exception as e:
            print(e)
        self.schedulerT()
        if self.medicine.get()!='' and self.medicine.get()[-1]=='M':
            Label(self.screen2,text=f'Time for medicine is: {self.medicine.get()}',bg='yellow',fg="green",justify=CENTER, height="2", width="40",font=("arial", 10,'bold')).place(x=113, y=508)
            self.threader(self.meds)
        
    def breathInOutT(self):
        self.threader(self.breathInOut)
    
    def stretchingT(self):
        self.threader(self.stretching)

    def BodyRT(self):
        self.threader(self.BodyR)

    def readingQuoteT(self):
        self.threader(self.readingQuote)
    
    def readingBookT(self):
        self.threader(self.readingBook)

    def readingJokeT(self):
        self.threader(self.readingJoke)

    def readingFactsT(self):
        self.threader(self.readingFacts)
    
    def short_breakT(self):
        self.threader(self.short_break)

    def StressPressT(self):
        self.threader(self.StressPress)

    def JumpingT(self):
        self.threader(self.Jumping)
    
    def YogaT(self):
        self.threader(self.Yoga)

    def breathExerciseT(self):
        self.threader(self.breathExercise)

    def Yoga(self):
        self.TTS("This activity will take around 5 minute")

        self.TTS("Sit down on floor, Press your head with, both your hands, bow down and come up 10 times")
        self.TTS("Begin")
        for i in range (10):
            self.TTS("press head, Deep breath in, bow down, and hold")
            time.sleep(2)
            self.TTS("Come Up, release head, and breath")
            time.sleep(1)
        self.TTS("Take a deep breath hold for 5 seconds and release")
        x=1
        if x!=0:        
            time.sleep(5)
        self.TTS("Hold your right ear with left palm, and stretch towards left, for 10 seconds")
        self.TTS("Begin")
        for i in range (10):
            time.sleep(1)
            
        self.TTS("Hold your left ear with right palm, and stretch towards right, for 10 seconds")
        self.TTS("Begin")
        for i in range (10):
            time.sleep(1)

        self.TTS("Take a deep breath hold for 5 seconds and release")
        if x!=0:        
            time.sleep(5)
        self.TTS("Hold your hands behind your head, stretch neck downwards, for 10 seconds")
        for i in range (10):
            self.sleep(1)

        self.TTS("Take a deep breath hold for 5 seconds and release")
        if x!=0:        
            time.sleep(5)
        self.TTS("Join your hands in prayer position, Hold your chin with your thumbs, push your head upwards, for 10 seconds")
        for i in range (10):
            time.sleep(1)
            
        self.TTS("Take a deep breath hold for 5 seconds and release")
        self.TTS("Sit down Straight")
        self.TTS("Now Hold your left elbow, with your right arm, and hold head with right palm, and twist your back to right, do it for 20 seconds")
        self.TTS("Begin")
        for i in range(10):
            self.TTS("breath in")
            time.sleep(1)
            self.TTS("breath out")
            time.sleep(1)

        self.TTS("Sit down Straight")
        self.TTS("Now Hold your right elbow, with your left arm, and hold head with left palm, and twist your back to left, do it for 20 seconds")
        self.TTS("Begin")
        for i in range(10):
            self.TTS("breath in")
            time.sleep(1)
            self.TTS("breath out")
            time.sleep(1)

        self.TTS("Take a deep breath hold for 5 seconds and release")
        if x!=0:        
            time.sleep(5)
        self.TTS("Find a wall and lean on your back")
        self.TTS("Make sure, both your legs are stretched, towards cealing at 90 degree, with support of wall")
        self.TTS("hold for 40 seconds,,,Begin")
        for i in range (10):
            self.TTS("Deep breath in")
            time.sleep(2)
            self.TTS("Exhale from mouth")
            time.sleep(2)

        self.TTS("Take a deep breath hold for 5 seconds and release")
        self.TTS("Take a towel, Lean on your back")
        self.TTS("Loop a strap around the arch of the left foot and hold the strap in both hands. Stretch left leg towards cealing")
        self.TTS("hold for 15 seconds,,,Begin")
        for i in range (10):
            self.TTS("Deep breath in")
            time.sleep(1)
            self.TTS("Exhale from mouth")
            time.sleep(1)

        self.TTS("Relax,...Take a deep breath hold for 5 seconds and release")
        if x!=0:        
            time.sleep(5)
        self.TTS("Loop a strap around the arch of the right foot and hold the strap in both hands. Stretch right leg towards cealing")
        self.TTS("hold for 15 seconds,,,Begin")
        for i in range (10):
            self.TTS("Deep breath in")
            time.sleep(1)
            self.TTS("Exhale from mouth")
            time.sleep(1)

        self.TTS("Take a deep breath hold for 5 seconds and release")

        if x!=0:        
            time.sleep(5)
        self.TTS("Loop a strap around the arch of the left foot and hold the strap in both hands. Stretch left towards cealing")
        self.TTS("hold for 15 seconds,,,Begin")
        for i in range (10):
            self.TTS("Deep breath in")
            time.sleep(1)
            self.TTS("Exhale from mouth")
            time.sleep(1)

        self.TTS("Take a deep breath hold for 5 seconds and release")
        time.sleep(5)
        self.TTS("Sit Straight, close your eyes, focus on your breath and start meditating for one minute")

        if x!=0:
            self.sl(1)
            self.TTS("Warm your palms, by rubbing them against each other, and put it on your eyes ")   
        
    def Zubaani(self):

        webbrowser.open('https://www.instagram.com/zubaani___/')
    def StressPress(self):
        try:
            x=random.randint(0,100)
            
            self.screen6=Toplevel(self.screen2)
            self.screen6.geometry("400x400")    
            self.screen6.title("Session")
            Label(self.screen6,text='Zubaani', bg="light goldenrod",fg="green", height="2", width="40",font=("arial", 20,'bold')).pack()
            x=Listbox(self.screen6,width=85,height=7)
            x.insert(1,"Instructions:")
            x.insert(2,"1. This is an instagram page.")
            x.insert(3,"2. Please be polite, real person will be assisting you.")
            x.insert(4,"3. If you click the button below, it will redirect to the ")
            x.insert(5,"   page so make sure you have internet connection.")
            x.insert(6,"4. Sometimes it might take a while to reply so please patient.")
            x.pack()
            Button(self.screen6, text='Visit Zubaani', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.Zubaani).pack()
            
            #return self.TTS(f'Book of the day is {book}\n written by {author}')
            
        except:
            self.TTS("Make sure you have an active internet Connection")

        
    def Jumping(self):
        self.TTS("This will take only a minute")
        time.sleep(1)
        self.TTS("Push wall while running against it, for 15 seconds")
        self.TTS("Begin")
        for i in range(15):
            self.TTS(i+1)
            time.sleep(1)

        self.TTS("Hands overhead, start jumping on spot for 15 seconds, don't go deep")
        self.TTS("Begin")
        for i in range(15):
            self.TTS(i+1)
            time.sleep(1)

        self.TTS("start Jumping Jacks for 10 seconds")
        self.TTS("Begin")
        for i in range(10):
            self.TTS(i+1)
            time.sleep(1)

        self.TTS("Start rocket jumping, for 10 counts, high right knee, jump on left leg and, swing left hand as high as you can, land on both legs")
        self.TTS("Begin")
        for i in range(10):
            self.TTS(i+1)
            time.sleep(1)

        self.TTS("Start rocket jumping, for 10 counts, high left knee jump on right leg and, swing left hand as high as you can, land on both legs")
        self.TTS("Begin")
        for i in range(10):
            self.TTS(i+1)
            time.sleep(1)
        
    def threader(self,t):
        self.t=t
        self.threads=threading.Thread(target=self.t)
        self.threads.start()
        
    def breathExercise(self):
        try:
            self.TTS("It will take only, 1 minute and 30 seconds, to breath out your, body stress out!")
            self.Body="Sit down on floor comfortably, sit in padmasana if possible"
            self.TTS(self.Body)
            self.TTS("Start with deep breathing for 10 seconds")
            self.TTS("Begin")
            for i in range(10):
                self.TTS('breath in,')
                self.sleep(3)
                self.TTS('Breath out,')
                self.sleep(3)

            self.Body="Start Anulom vilom, press your left nose with left thumb, breath in with a nostrills, and breath out with other, for 6 sets"
            self.TTS(self.Body)
            self.TTS("Begin")

            for i in range(6):
                self.TTS('breath in with right')
                self.sleep(3)
                self.TTS('Breath out with left')
                self.sleep(3)
                self.TTS('breath in with left')
                self.sleep(3)
                self.TTS('Breath out with right')
                self.sleep(3)

            self.Body="Start kapal bharti, Force the air in and out rapidly for 15 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(15):
                self.TTS(i+1)

        except Exception as e:
            print(e)

        self.TTS("You have x more minutes of energy to go on")
    
    def stretching(self):
        try:
            self.TTS("It will take only, 1 minute and 30 seconds, to stretch out your, body stress out!")
            self.Body="Stretch your both Hands up, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Bend down and Stretch your both hands, towards your legs, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Press fists of both hands to itself, and then stretch fingers outwards, for 10 times"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Stretch your left palm, with right palm, upwards, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Stretch your left palm, with right palm, downwards, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Stretch your right palm, with left palm, upwards, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Stretch your right palm, with left palm, downwards, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Spread your legs, touch your toes alternatively rapidly, for 30 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(30):
                self.TTS(i+1)

            self.Body="Take on boxing stance with left leg and fist at front, Start kicking high with right leg for 5 times, Shout High"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(5):
                self.TTS(i+1)
                self.sl(1/30)

            self.Body="Take on boxing stance with right leg and fist at front, Start kicking high with left leg for 5 times, Shout High"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(5):
                self.TTS(i+1)
                self.sl(1/30)

            self.Body="Well Done !!!"
            self.TTS(self.Body)

        except Exception as e:
                print(e)
        self.TTS("After this activity You have x more minutes of energy to work")
        
    
    def book(self):

        webbrowser.open("https://openlibrary.org"+self.id)
    def readingBook(self):
        try:
            x=random.randint(0,100)
            url='http://openlibrary.org/search.json?q=motivation'
            book=requests.get(url).json()['docs'][x]['title']
            author=requests.get(url).json()['docs'][x]['author_name'][0]
            self.id=requests.get(url).json()['docs'][x]['seed'][0]
            self.screen4=Toplevel(self.screen2)
            self.screen4.geometry("400x400")    
            self.screen4.title("Session")
            Label(self.screen4,text='Books to keep UP!', bg="light goldenrod",fg="green", height="2", width="40",font=("arial", 20,'bold')).pack()
            Label(self.screen4,text='',wraplength=310, justify=CENTER,font=("arial", 15)).pack()
            Label(self.screen4,text=book,wraplength=310, justify=CENTER,font=("arial", 20)).pack()
            Label(self.screen4,text='',wraplength=250, justify=LEFT,font=("arial", 15)).pack()
            Label(self.screen4,text=author,wraplength=250, justify=CENTER,font=("arial", 15)).pack()
            Label(self.screen4,text='',wraplength=250, justify=LEFT,font=("arial", 15)).pack()
            Button(self.screen4, text='Visit book Site', bg='#BFEFFF',width=14, font=('helvetica', 20, 'normal'), command=self.book).pack()
            
            return self.TTS(f'Book of the day is {book}\n written by {author}')
            
        except:
            return self.TTS("Make sure you have an active internet Connection")

        

    def readingQuote(self):
        try:
            url="http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
            self.TTS("After this activity You have x more minutes of energy to work")
            Quote= requests.get(url).json()['quoteText']
            self.screen4=Toplevel(self.screen2)
            self.screen4.geometry("400x400")    
            self.screen4.title("Session")
            Label(self.screen4,text='Quote Positivity', bg="light goldenrod",fg="green", height="2", width="40",font=("arial", 20,'bold')).pack()
            Label(self.screen4,text=Quote,wraplength=250, justify=LEFT,font=("arial", 20)).pack()
            self.TTS(Quote)
            
        except:
            self.TTS("Make sure you have an active internet Connection")
        self.TTS("After this activity You have x more minutes of energy to work")
    
    def readingJoke(self):
        try:
            url="http://api.icndb.com/jokes/random"
            
            joke= requests.get(url).json()['value']['joke']
            self.screen3=Toplevel(self.screen2)
            self.screen3.geometry("400x400")    
            self.screen3.title("Joke")
            Label(self.screen3,text='Chuck Norris Joke for you', bg="light goldenrod",fg="green", height="2", width="40",font=("arial", 20,'bold')).pack()
            Label(self.screen3,text=joke,wraplength=310, justify=LEFT,font=("arial", 20)).pack()
            self.TTS(joke)
            
        except:
            self.TTS("Make sure you have an active internet Connection")
        self.TTS("After this activity You have more than x minutes of energy to work")
    def readingFacts(self):
        self.screen5=Toplevel(self.screen2)
        self.screen5.geometry("400x400")    
        self.screen5.title("Fact")
        self.fact=py8fact.random_fact()
        Label(self.screen5,text='Chuck Norris Joke for you', bg="light goldenrod",fg="green", height="2", width="40",font=("arial", 20,'bold')).pack()
        Label(self.screen5,text=self.fact,wraplength=315, justify=LEFT,font=("arial", 20)).pack()
        self.TTS(self.fact)

    def BodyR(self):
        try:
            self.TTS("It will take only, 1 minute and 30 seconds, to twist out your, body stress out!")
            self.Body="Rotate your both Hands, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Rotate your both hands, on Opposite side, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Rotate both of your wrists, Outwards, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Rotate both of your wrists, Inwards, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Rotate Hips, Clockwise, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Sit on the floor, Stretch your legs outwards,  Rotate both of your Ankles, Clockwise, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Sit on the floor, Stretch your legs outwards, Rotate both of your Ankles, Anti-Clockwise, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Rotate your head, clock-wise, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Rotate your head, Anti-clock-wise, for 10 seconds"
            self.TTS(self.Body)
            self.TTS("Begin")
            for i in range(10):
                self.TTS(i+1)

            self.Body="Well Done !!!"
            self.TTS(self.Body)

        except Exception as e:
                print(e)
        self.TTS("After this activity You have x more minutes of energy to work")
    def short_break(self):
        self.TTS("Take a short break.... You are amazing when you work with full energy")
        self.sl(15)
        self.TTS("After this activity You have x more minutes of energy to work")

    
    def meds(self):
        
        self.timer=self.medicine.get()

        if self.timer != '' and self.timer[-1]=='M':
            
            while True:
            
                x=datetime.now().strftime("%I:%M %p")
                if x ==self.timer:
                    self.TTS("Its Medicine time")
                    break



    def Music(self):
        self.TTS("Why don't you listen to your favorite songs while you go for a walk outside")

    def relief(self):
        self.TTS("Press a soft ball or join your hands and crush your own fists, for next 1 minutes")
        self.sl(1)
        self.TTS("You have great strength, now you can do more with more energy")
    def schedulerT(self):
        self.threader(self.scheduler)
    def scheduler(self):
        self.sl(15)
        self.TTS("You should be hydrated, Have some water")
        self.sl(25)
        self.TTS("Get your body stretched, press Start Stretching button")
        self.sl(25)
        self.TTS("You should be hydrated, Have some water")
        self.sl(30)
        self.TTS("You are getting cold, start jumping exercise, press Start Stretching Button")
        self.sl(25)
        self.TTS("You should be hydrated, Have some water")
        self.sl(25)
        self.TTS("You should have a break, read some books, or go for a walk, with some music")
        self.sl(25)
        self.TTS("You should be hydrated, Have some water")
        self.sl(25)
        self.TTS("Relax your mind, perform yoga, Press Yoga Medition button")
        self.sl(25)
        self.TTS("You should be hydrated, Have some water")
        self.sl(35)
        self.TTS("Do keep your calm, take a breath, press Breath Stress Out button")
        self.sl(40)
        self.TTS("You should Talk to someone, if you need some assistance, regarding your mental health, talk to us via Zubaani")

screen = Tk()
screenUI=UI(screen)
screen.mainloop()
