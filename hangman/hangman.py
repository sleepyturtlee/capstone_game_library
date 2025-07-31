import random
import tkinter
from tkinter import *
import tkinter.font as tkFont



#a really long list of words
listofwords = [
    "electricity","donkey","hardware","xerox","transistor","computer","desktop","engineering","hangman","circuit","imagination","robot","memory","power","submarine","chess","resistance","matrix","function","laser","mechanism","bodyguard","titanic","global","ozone","bridge","technology","spider","pyramid","sphere","member","warning","yourself","screen","language","system","internet","parameter","traffic","network","filter","nucleus","automatic","microphone","cassette","operation","country","beautiful","picture","teacher","superman","undertaker","alarm","process","keyboard","electron","certificate","grandfather","landmark","relativity","eraser","ambivalent","design","football","human","musician","egyptian","elephant","queen","record","message","wallpaper","nationality","answer","wrong","statement","forest","puzzle","voltage","current","mathematics","wisdom","dream","supermarket","database","collection","barrier","project","sunlight","figure","graph","battle","hundred","signal","thousand","transformation","daughter","flower","communication","microwave","electronic","peace","wireless","delete","wind","brain","control","prophet","freedom","harbour","confidence","positive","harvest","hunger","woman","children","stranger","garden","pleasure","laugh","between","recognition","tomorrow","autumn","monkey","spring","winter","classification","typewriter","success","difference","acoustics","astronomy","agreement","sorrow","christmas","silver","birthday","championship","friend","comfortable","diffusion","policeman","science","desert","basketball","blood","funeral","silence","garment","merchant","spirit","punishment","measurement","ocean","digital","illusion","tyrant","castle","passion","magician","remedy","knowledge","threshold","number","vision","expectation","absence","mystery","morning","device","thoughts","spirit","future","import","mountain","treasure","machine","whispering","eternity","reflection","occupation","achievement","lightning","secret","environment","shepherd","confusion","grave","promise","honor","reward","temple","distance","eagle","saturn","finger","belief","crystal","fashion","direction","captain","moment","permission","logic","analysis","password","english","equalizer","simulation","emotion","battle","expression","scissors","trousers","glasses","department","dictionary","chemistry","induction","detail","widow","wealth","health","disaster","volcano","poverty","limitation","perfect","intelligence","failure","ignorance","destination","source","resort","satisfaction","exam","frequency","selection","substitution","kingdom","pattern","management","situation","multiply","treatment","dollar","intuition","chapter","magnet", "desire","command","action","consciousness","enemy","security","object","happen","happiness","worry","method","tolerance","error","hesitation","record","tongue","supply","vibration","stress","despair","restaurant","television","video","audio","layer","mixture","doorbell","cousin","beard","finance","production","invisible","excitement","afternoon","office","alpha","illustration","valley","apartment","necessary","shortage","almost","furniture","blanket","suggestion","overflow","demonstration","challenge","compact","tower","question","problem","pressure","beast","encouragement","afraid","cavity","appearance","wonderful","matter","dimension","business","doubt","conversation","reaction","psychology","superstition","smash","horseshoe","surprise","nothing","ladder","opposite","reality","genius","string","destruction","expensive","painting","chicken","wishing","profession","hatred","possession","criticism","zebra","harmony","personality","overcompensate","addition","subtraction","cipher","encryption","compression","extension","blessing","meeting","difficulty","weapon","against","external","internal","legend","servant","secondary","license","directory","statistics","generation","attraction","sensitivity","magnification","someone","symptom","recipe","service","family","island","planet","butterfly","diving","strength","extreme","opportunity","illumination","cable","conflict","interference","receiver","transmitter","channel","company","grocery","devil","angel","exactly","document","tutorial","sound","voice","abbreviation","abdomen","abrupt","absolute","absorption","abstract","academy","acceleration","accident","account","acidification","actress","adaptation","addiction","adjustment","admiration","adoption","advanced","adventure","advertisement","agenda","airport","algorithm","allocation","aluminum","ambiguity","amphibian","anesthesia","analogy","anchor","animation","anode","cathode" ,"apparent","appendix","approval","approximation","arbitrary","architecture", "arithmetic","arrangement","article","ascending","ashamed","asleep","assembly","astonishment","atmosphere","awful","bachelor","backbone","bacteria","balance","balloon","banana","barbecue","baseball","beaker","beggar","behavior","benefit","bidirectional","biology","blackboard","bladder","bleeding","blender","bonus","bottle","bracket","branch","bubble","bucket","budget","burglar","butcher","bypass","calculator","calibration","campaign","cancellation","candidate","candle","carpenter","carriage","cartoon","cascade","casual","catalyst","category","cement","ceremony","chairman","checkout","chimney","chocolate","circumference","civilization","classroom","clearance","client","coconut","coincidence","colleague","comfortable","competition","kangaroo","kidnap","journal","jockey","iteration","isometric","isolation","invitation","institution","injection","humanity","housekeeper","history","heaven","greenhouse","glory","foundation","formula","fluctuation","fiction","emission","elasticity","earthquake","dynamic","doctorate","divorce","nightmare","virtue","description","baguette","photosynthesis",]
tempanswer = random.choice(listofwords)
answer = tempanswer.upper()
wordbycharacter = list(answer)
formatforcensor = len(tempanswer) * "_"

censor = ""
currentwordstatus = list(formatforcensor)
formatcurrentwordstatus = ""
tempindex = int(0)
guessedletters = []
livesleft = 10

print(answer)

main = tkinter.Tk()
main.geometry("750x750")
main.title("Hangman")


from PIL import Image, ImageTk

image0 = Image.open("hangman/assets/frame0.png")  
image0 = image0.resize((300,300))  
tk_image0 = ImageTk.PhotoImage(image0)
image0.save("frame0.png")

image1 = Image.open("hangman/assets/frame1.png")  
image1 = image1.resize((300,300)) 
tk_image1 = ImageTk.PhotoImage(image1)
image1.save("frame1.png")

image2 = Image.open("hangman/assets/frame2.png")  
image2 = image2.resize((300,300))  
tk_image2 = ImageTk.PhotoImage(image2)
image2.save("frame2.png")

image3 = Image.open("hangman/assets/frame3.png")  
image3 = image3.resize((300,300))  
tk_image3 = ImageTk.PhotoImage(image3)
image3.save("frame3.png")

image4 = Image.open("hangman/assets/frame4.png")  
image4 = image4.resize((300,300)) 
tk_image4 = ImageTk.PhotoImage(image4)
image4.save("frame4.png")

image5 = Image.open("hangman/assets/frame5.png")  
image5 = image5.resize((300,300))  
tk_image5 = ImageTk.PhotoImage(image5)
image5.save("frame5.png")

image6 = Image.open("hangman/assets/frame6.png")  
image6 = image6.resize((300,300))  
tk_image6 = ImageTk.PhotoImage(image6)
image6.save("frame6.png")

image7 = Image.open("hangman/assets/frame7.png")  
image7 = image7.resize((300,300))  
tk_image7 = ImageTk.PhotoImage(image7)
image7.save("frame7.png")

image8 = Image.open("hangman/assets/frame8.png")  
image8 = image8.resize((300,300))  
tk_image8 = ImageTk.PhotoImage(image8)
image8.save("frame8.png")

image9 = Image.open("hangman/assets/frame9.png") 
image9 = image9.resize((300,300))  
tk_image9 = ImageTk.PhotoImage(image9)
image9.save("frame9.png")

image10 = Image.open("hangman/assets/frame10.png") 
image10 = image10.resize((300,300))  
tk_image10 = ImageTk.PhotoImage(image10)
image10.save("frame10.png")

def run():
    def on_button_click():
        global livesleft
        global tk_image1, tk_image2, tk_image3, tk_image4, tk_image5, tk_image6, tk_image7, tk_image8, tk_image9, tk_image10
        guess = guessentry.get()
        guess = guess.upper()
        if guessentry.get().isalpha() == False or len(guessentry.get()) > 1:
            tempdisclaimer.delete(0,END)
            tempdisclaimer.insert(END,"Invalid Guess")
        else:
            guessentry.delete(0,END)
            tempindex = 0
            if guess in wordbycharacter:
                tempdisclaimer.delete(0,END)
                tempdisclaimer.insert(END,f"Yes, {guess} is in the phrase.")
                # change currentwordstatus by letter through index, which gets formatted through formatcurrentwordstatus
                for letter in wordbycharacter:
                    if guess == letter:
                        currentwordstatus[int(tempindex)] = guess
                    tempindex += 1
                formatcurrentwordstatus = ""
                for x in currentwordstatus:  # reformats the censor
                    formatcurrentwordstatus += x
                wordstatus.delete(0, END)
                wordstatus.insert(END, string=formatcurrentwordstatus)
                livesleftstatus.delete(0, END)
                livesleftstatus.insert(END, f"You have {livesleft} lives left. ")
            else:
                tempdisclaimer.delete(0,END)
                tempdisclaimer.insert(END,f"Nope,{guess} is not in the phrase.")
                livesleftstatus.delete(0, END)
                livesleft -= 1
                livesleftstatus.insert(END, f"You have {livesleft} lives left. ")
                formatcurrentwordstatus = ""
                for x in currentwordstatus:  # reformats the censor
                    formatcurrentwordstatus += x

            guessedlettersentry.delete(0, END)
            guessedletters.append(guess)
            guessedlettersentry.insert(END, guessedletters)
        if livesleft ==9:
            print("yes")
            picture.config(image=tk_image1)
        if livesleft ==8:
            picture.config(image=tk_image2)
        if livesleft ==7:
            picture.config(image=tk_image3)
        if livesleft ==6:
            picture.config(image=tk_image4)
        if livesleft ==5:
            picture.config(image=tk_image5)
        if livesleft ==4:
            picture.config(image=tk_image6)
        if livesleft ==3:
            picture.config(image=tk_image7)
        if livesleft ==2:
            picture.config(image=tk_image8)
        if livesleft ==1:
            picture.config(image=tk_image9)
        if livesleft <= 0:
            disclaimer.insert(END,"You ran out of lives.")
            main.config(background="red")
            picture.config(image=tk_image10)
            open_lose_window()
        if answer == formatcurrentwordstatus:
            disclaimer.insert(END,f"YOU GUESSED IT!") 
            main.config(background="green")
            open_win_window()
            disclaimer.insert(END,f"The phrase was {answer}")


    def open_win_window():
        new_window = tkinter.Toplevel(main)  
        new_window.title("YOU WON HANGMAN")
        new_window.geometry("400x400") 

        label = tkinter.Label(new_window, text="YOU WON HANGMAN!",font=custom_font)
        label.pack(pady=20,anchor=CENTER)

    def open_lose_window():
        new_window = tkinter.Toplevel(main)  
        new_window.title("You lost.")
        new_window.geometry("400x400")
        label = tkinter.Label(new_window, text="You lost.",font=custom_font)
        label.pack(pady=20,anchor=CENTER)



    #omg everything is so cluttered

    custom_font = tkFont.Font(family="Arial", size=35)
    guessentry = Entry(main)

    picture = Label(main, width=400, height=400, background="grey",image=tk_image0)


    button = tkinter.Button(main, text="Guess", command=on_button_click)

    heading = tkinter.Label(main, text="Welcome to Hangman!")
    heading.pack(anchor="center")

    livesleftstatus = Entry(main, state="normal", justify="center")
    livesleftstatus.pack()
    livesleftstatus.insert(END, f"You have {livesleft} lives left. ")
    letterstatus = Label(main, text=f"There are {len(currentwordstatus)} letters in this word.").pack()

    wordstatus = Entry(main, state="normal", justify="center", bd=5, font=custom_font)
    wordstatus.pack()
    wordstatus.insert(END, formatforcensor)

    guesscaption = Label(main, text="You have guessed:").pack()

    guessedlettersentry = Entry(main)
    guessedlettersentry.pack()

    tempdisclaimer = Entry(main)
    tempdisclaimer.pack()

    picture.pack( pady=30, padx=30, fill=tkinter.X)


    tkinter.Label(main, text="Type a letter and press the 'Guess' button.").pack()

    guessentry.pack()

    button.pack()

    disclaimer = Text(main,font= custom_font)
    disclaimer.pack(side="bottom")

    main.mainloop()
