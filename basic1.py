import os as s
import subprocess as sub 
import pyttsx3 as ps
import datetime as dt
import pywhatkit as wt
import smtplib as smt
import requests as rs
from bs4 import BeautifulSoup
import speech_recognition as sr
from PyDictionary import PyDictionary as pd
pt=ps.init()
pt.setProperty('rate',180)
pt.say("How May I Help You Sir...!")
pt.runAndWait()
while(True):
    print("How may i Help You sir...?")
    r=sr.Recognizer()
    r.pause_threshold=1
    print("Listening...!")
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            print("Recognizing..!")
            text=r.recognize_google(audio)
    
    #user_input=(input('How may i Help you sir..?').lower())
    user_input=text.lower()
    if ("hi" in user_input or "hello" in user_input):
        pt.say("Hello sir,How are You")
        pt.runAndWait()
        print("Hello sir,How are You..?")
        
        
        
    elif ("fine" in user_input):
        if( ("what about you" in user_input) or ("How are you" in user_input)):
            pt.say("I'm also fine sir")
            pt.runAndWait()
            print("i am also fine sir..!")
        
        else:
            pass
        
        
        
        
        
        
    
    
    
    elif (("open" in user_input) or ("launch" in user_input)  or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or ("start" in user_input)) and (("notepad" in user_input)) or ("notepad" in user_input):
        
        if  (("dont" in user_input) or ("don't" in user_input)) and ("notepad" in user_input) :
            pt.say("Anything else sir...!")
            pt.runAndWait()
            print("Anything Else sir :)",end="\n")
        
        
        else:
            print("opening notepad for you...!",end="\n")
            pt.say("Opening Notepad for You")
            pt.runAndWait()
            s.system("notepad")
            s.system("cls")
        
    elif(("open" in user_input) or ("launch" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or ("start" in user_input)) and  (("chrome" in user_input) or ("broswer" in user_input)) or (("chrome" in user_input) or ("browser" in user_input)):
        
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("chrome" in user_input) or ("broswer" in user_input)):
            pt.say("Anything else sir...!")
            pt.runAndWait()
            print("Anything Else sir :)",end="\n")
            s.system("cls")
            
        else:
            print("""
            Enter The number of Website or  Enter Any Website You want to visit:-
            
            1:-Stackoverflow \t\t 2:-Github \t\t 3:-Geeksforgeeks \t 4:-Wikipedia 
            
            5:-Youtube \t\t\t 6:-Twitter \t\t 7:- Facebook \t\t 8:-Instagram
            
            9:-LinkedIn \t\t 10:-Indeed \t\t 11:-Naukri.com \t 12:-Monster.com
            
            13:-Amazon \t\t\t 14:-Flipkart \t\t 15:-Zomato \t\t 16:-Swiggy
            
            17:-TimesofIndia \t\t 18:-NDTV \t\t 19:-Cricbuzz \t\t 20:-Gadgets 360
            
            """)
            pt.say("Enter The number of Website or  Enter Any Website You want to visit")
            pt.runAndWait()
            
            search=input("Enter The number of Website or  Enter Any Website You want to visit:-")
            
            if search=='1':
                print("opening stackoverflow for you..!",end="\n")
                pt.say("opening stackoverflow for you")
                pt.runAndWait()
                s.system("chrome stackoverflow.com ")
                s.system("cls")
            
            elif search=='2':
                print("opening github for you..!",end="\n")
                pt.say("opening github for you")
                pt.runAndWait()
                s.system(" chrome github.com")
                s.system("cls")
                
            elif search=='3':
                print("opening Geeksforgeeks for you..!",end="\n")
                pt.say("opening Geeksforgeeks for you")
                pt.runAndWait()
                s.system(" chrome geeksforgeeks.org")
                s.system("cls")
                
                
            elif search=='4':
                print("opening Wikipedia for you..!",end="\n")
                pt.say("opening wikipedia for you")
                pt.runAndWait()
                s.system(" chrome wikipedia.org")
                s.system("cls")
                
            elif search=='5':
                print("opening Youtube for you..!",end="\n")
                pt.say("opening youtube for you")
                pt.runAndWait()
                s.system("chrome youtube.com")
                s.system("cls")
                
                
            elif search=='6':
                print("opening Twitter for you..!",end="\n")
                pt.say("opening twitter for you")
                pt.runAndWait()
                s.system(" chrome twitter.com")
                s.system("cls")
                
                
            elif search=='7':
                print("opening Facebook for you..!",end="\n")
                pt.say("opening facebook for you")
                pt.runAndWait()
                s.system("chrome facebook.com")
                s.system("cls")
                
                
            elif search=='8':
                print("opening Instagram for you..!",end="\n")
                pt.say("opening instagram for you")
                pt.runAndWait()
                s.system(" chrome instagram.com")
                s.system("cls")
                
                
            elif search=='9':
                print("opening Linkedin for you..!",end="\n")
                pt.say("opening linkedin  for you")
                pt.runAndWait()
                s.system(" chrome https://www.linkedin.com/")
                s.system("cls")
                
                
                
            elif search=='10':
                print("opening indeed for you..!",end="\n")
                pt.say("opening Indeed for you")
                pt.runAndWait()
                s.system(" chrome Indeed.co.in")
                s.system("cls")
                
                
                
            elif search=='11':
                print("opening Naukri.com for you..!",end="\n")
                pt.say("opening Naukri.com for you")
                pt.runAndWait()
                s.system(" chrome Naukri.com")
                s.system("cls")
                
                
            elif search=='12':
                print("opening Monster.com for you..!",end="\n")
                pt.say("opening MOnster.com for you")
                pt.runAndWait()
                s.system(" chrome Monster.com")
                s.system("cls")
                
                
                
            elif search=='13':
                print("opening Amazon for you..!",end="\n")
                pt.say("opening Amazon for you")
                pt.runAndWait()
                s.system(" chrome Amazon.in")
                s.system("cls")
                
                
                
                
            elif search=='14':
                print("opening Flipkart for you..!",end="\n")
                pt.say("opening Flipkart for you")
                pt.runAndWait()
                s.system(" chrome flipkart.com")
                s.system("cls")
                
                
                
                
            elif search=='15':
                print("opening Zomato for you..!",end="\n")
                pt.say("opening Zomato for you")
                pt.runAndWait()
                s.system("chrome zomato.com")
                s.system("cls")
                
                
                
            elif search=='16':
                print("opening Swiggy for you..!",end="\n")
                pt.say("opening Swiggy for you")
                pt.runAndWait()
                s.system(" chrome swiggy.com")
                s.system("cls")
                
                
                
            elif search=='17':
                print("opening TimesOfIndia for you..!",end="\n")
                pt.say("opening TimesOfIndia for you")
                pt.runAndWait()
                s.system(" chrome timesofindia.indiatimes.com")
                s.system("cls")
                
                
            elif search=='18':
                print("opening NDTV for you..!",end="\n")
                pt.say("opening NDTV for you")
                pt.runAndWait()
                s.system(" chrome ndtv.com")
                s.system("cls")
            
            elif search=='19':
                print("opening cricbuzz for you..!",end="\n")
                pt.say("opening cricbuzz for you")
                pt.runAndWait()
                s.system(" chrome cricbuzz.com")
                s.system("cls")
                
                
                
            elif search=='20':
                print("opening Gadgets.ndtv  for you..!",end="\n")
                pt.say("opening gadgets.ndtv for you")
                pt.runAndWait()
                s.system(" chrome gadgets.ndtv.com")
                s.system("cls")
                
            else:
                
                pt.say("opening {}for you".format(search))
                pt.runAndWait()
                print("opening {} for you..!".format(search),end="\n")
                s.system("chrome {0}".format(search))
                s.system("cls")
            
            
        
        
        
    elif (("open" in user_input) or ("launch" in user_input)  or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and (("window" in user_input) or ("window media player" in user_input)) or (("window" in user_input) or ("window media player" in user_input)):
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("window" in user_input) or ("window media player" in user_input)):
                pt.say("Anything else sir...!")
                pt.runAndWait()
                print()
                print("Anything Else sir :)",end="\n")
        else:
                print("opening window media player for you...!",end="\n")
                pt.say("opening window media player for you...!")
                pt.runAndWait()
                s.system("wmplayer")
                input("Enter to continue...!")
                s.system("cls")
                
      
    
    
    
    
    
    
             
    elif (("open" in user_input) or ("launch" in user_input)  or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and (("sublime" in user_input) or ("text editor" in user_input) or ("sublime text editor" in user_input)) or (("sublime" in user_input) or ("text editor" in user_input) or ("sublime text editor" in user_input)):
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("sublime" in user_input) or ("text editor" in user_input) or ("sublime text editor" in user_input)) :
                pt.say("Anything else sir...!")
                pt.runAndWait()
                print("Anything Else sir :)",end="\n")
        else:
                print("opening sublime text editor for you...!",end="\n")
                pt.say("opening sublime text editor for you...!")
                pt.runAndWait()
                sub.Popen("E:\software\sublime textr\sublime_text.exe")
                input("Enter to continue...!")
                s.system("cls")
                
                
    
    
    
    
    
    elif (("open" in user_input) or ("launch" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and (("vs code" in user_input)   or ("vs" in user_input)  or ("visual studio code " in user_input)) or (("vs code" in user_input) or ("vs" in user_input) or ("visual studio code " in user_input)):
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("vs code" in user_input)  or  ("vs" in user_input)  or ("visual studio code " in user_input)):
            pt.say("Anything else sir...!")
            pt.runAndWait()
            print("Anything Else sir :)",end="\n")
            
            
        else:
            print("opening visual studio code for you...!",end="\n")
            pt.say("opening Visual studio code for you...!")
            pt.runAndWait()
            sub.Popen(r"C:\Users\iNsEcT0R DeViL\AppData\Local\Programs\Microsoft VS Code\Code.exe") 
            input("Enter to continue...!")
            s.system("cls")
             
    
    
    
    
    elif (("run" in user_input) and ("date" in user_input) or ("time" in user_input)) or (("date" in user_input) or ("time" in user_input)):
            
        if (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input))  and ("date" in user_input):
                pt.say("Anything else sir...!")
                print("Anything Else sir :)",end="\n")
            
            
        else:
            date=dt.datetime.now()
            print ("The time is now: = {0}:{1}:{2}".format(date.hour, date.minute, date.second))
            pt.say("Time is {0} pm {1} Minute {2} Seconds".format(date.hour, date.minute, date.second))
            pt.runAndWait()
            print("Date is = {0}:{1}:{2}".format(date.day,date.month,date.year))
            pt.say("Date is {0} Date {1} Month  {2} Year ".format(date.day,date.month,date.year))
            pt.runAndWait()
            input("Enter to continue...!")
            s.system("cls")

           
        
        
        
        
        
    elif ("send message" in user_input) or ("whatsapp" in user_input):
        
        if (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input))  and (("send" in user_input) or ("message" in user_input)  or ("whatsapp" in user_input)):
                pt.say("Anything else sir...!")
                pt.runAndWait()
                print("Anything Else sir :)",end="\n")
                
                
                
                
                
        else:
            number_input=input("whom  do you want to send message..?")
            if(("quit" in number_input) or ("exit" in number_input) or ("bie" in number_input) or ("close" in number_input) or ("stop" in number_input)):
                pt.say("Quitting")
                pt.runAndWait()
                print("quitting...!")
                break

            message_input=input("Enter your message here:-")
            time_hour_input=int(input("What hour do you want to send the message:-"))
            time_miute_input=int(input("what time do you want to send message:-"))
            print("sending message to {} \n".format(number_input))
            pt.say("Sending message to {}".format(number_input))
            pt.runAndWait()
            wt.sendwhatmsg(number_input,message_input,time_hour_input,time_miute_input)
            input("Enter to continue...!")
            s.system("cls")
    
    
    elif (("send mail to gmail" in user_input) or ("send mail" in user_input) or ("send gmail" in user_input)) or ("gmail" in user_input):
        
        
        if (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input))  and (("send mail to gmail" in user_input) or ("send mail" in user_input)):
            
            pt.say("Anything else sir...!")
            print("\nAnything Else sir :)",end="\n")
            
            
        else:
            
            user_email="mytest.test922@gmail.com"
            user_passwd="12@mytest.test"
            email_rece=input("whom do You want to send Email type Gmail Address:-")
            
            if(("quit" in email_rece) or ("exit" in email_rece) or ("bie" in email_rece) or ("close" in email_rece) or ("stop" in email_rece)):
                pt.say("Quitting")
                pt.runAndWait()
                print("Quitting...!")
                break
                
                
            email_message=input("type your message here:-")
            st=smt.SMTP("smtp.gmail.com",587)
            st.starttls()
            st.login(user_email,user_passwd)
            result=st.sendmail(user_email,email_rece,email_message)
            
            if(result!=None):
                print("Mail has been sented..!")
                pt.say("Mail has been sented to {}".format(email_rece))
                pt.runAndWait()
                st.quit()
                input("Enter to continue...!")
                s.system("cls")
                
                
            else:
                print("Try Again..!")
            
     
    
    elif "help" in user_input:
        print("""
           Which Task would You like to Perform,Enter its name:-
            
            1:-Sublime text editor \t\t 2:-Window Media Player \t 3:-visual studio code 
            
            4:-Notepad \t\t\t  \t 5:-Send Whatsapp message \t 6:-Send email
            
            7:-Date \t\t\t\t 8:-chrome \t\t \t9:-Show me latest news 
            
            10:-Entertain me
            
            """)
        pt.say(" Which Task would You like to Perform,Enter its name")
        pt.runAndWait()

        
        
        
        
    elif (("show me latest news" in user_input) or ("latest news" in user_input)):
        list_news=[]
        url='https://www.ndtv.com/latest?pfrom=home-mainnavgation'
        page=rs.get(url)
        soup=BeautifulSoup(page.content,'html.parser')
        result=soup.find(id='ins_storylist')
        news1=result.find('div',class_='nstory_intro')
        news=result.find_all('div',class_='nstory_intro')
            
        for latest_news in news:
            list_news.append((latest_news.text).strip())
                
        rows_show=int(len(list_news)/2)
        
        for i in range(rows_show):
            print(list_news[i],end="\n\n")
        
        pt.say(news1.text)
        pt.runAndWait()
        
        
      
    elif ("play music" in user_input):
        print("Opening Playlist")
        pt.say("Opening Playlist")
        pt.runAndWait()
        s.system("chrome https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbUhuZUdJdnVBQ25XcmhMUHpkMTRRVA%3D%3D")
        
        
    elif("dictionary" in user_input):
        dict_input=input("Enter Any word:-")
        print()
        pt.say("Searching..!")
        pt.runAndWait()
        dict_=pd.meaning(dict_input)
        for statement,statement1 in dict_.items():
            for j in statement1:
                print(statement +" : " +j,end="\n")
                
        input("Enter to continue..!")
        s.system("cls")
    
    elif ("Entertain me" in user_input):
        
        url1='http://randomfactgenerator.net/'
        page=rs.get(url1)
        soup=BeautifulSoup(page.content,'html.parser')
        result=soup.find_all(id='z')
        for random in result:
            print(random.text,end="\n\n")
            pt.say(random.text)
            pt.runAndWait()
        input("Enter to continue..!")    
        s.system("cls")
        
    
    
    elif "weather" in user_input:
        weather_input=input("Enter Your city Name:-")
        change="https://www.accuweather.com/en/search-locations?query={0}".format(weather_input)
        print("Getting cloud Together")
        pt.say("Getting Cloud Together")
        pt.runAndWait()
        s.system("chrome {}".format(change))
        s.system("cls")

    elif (("quit" in user_input) or ("exit" in user_input) or ("bie" in user_input) or ("close" in user_input) or ("stop" in user_input)):
        
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("quit" in user_input) or ("exit" in user_input) or ("bie" in user_input) or ("close" in user_input) or ("stop" in user_input)):
            pt.say("Anything else sir...!")
            pt.runAndWait()
            print("Anything Else sir :)",end="\n")
            
            
        else:
            pt.say("Quitting")
            pt.runAndWait()
            print("quitting...!",end="\n")
            s.system("cls")
            break
        
    else:
        print("\n Command not recognized try Help")
        pt.say(" Command not recognized Try Help")
        pt.runAndWait()
        
