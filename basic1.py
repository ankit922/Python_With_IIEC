import os as s
import subprocess as sub 
import pyttsx3 as ps
import datetime as dt
import pywhatkit as wt
import smtplib as smt

while(True):
    #ps.speak("How May I Help You Sir...!")
    user_input=(input("How May I Help You Sir...?")).lower()
    if (("open" in user_input) or ("launch" in user_input) or ("load" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and ("notepad" in user_input) or ("notepad" in user_input) :
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and ("notepad" in user_input):
            #pt.speak("Anything else sir...!")
            print("Anything Else sir :)",end="\n")
        else:
            print("opening notepad for you...!",end="\n")
            s.system("notepad")
            s.system("cls")
            
        
    elif(("open" in user_input) or ("launch" in user_input) or ("load" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or ("start" in user_input)) and  (("chrome" in user_input) or ("broswer" in user_input)) or (("chrome" in user_input) or ("browser" in user_input)):
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("chrome" in user_input) or ("broswer" in user_input)):
            #pt.speak("Anything else sir...!")
            print("Anything Else sir :)",end="\n")
            s.system("cls")
            
        else:
            print("""
            Which Website would You like to open:-
            
            1:-Stackoverflow \t\t 2:-Github \t\t 3:-Geeksforgeeks \t 4:-Wikipedia 
            
            5:-Youtube \t\t\t 6:-Twitter \t\t 7:- Facebook \t\t 8:-Instagram
            
            9:-LinkedIn \t\t 10:-Indeed \t\t 11:-Naukri.com \t 12:-Monster.com
            
            13:-Amazon \t\t\t 14:-Flipkart \t\t 15:-Zomato \t\t 16:-Swiggy
            
            17:-TimesofIndia \t\t 18:-NDTV \t\t 19:-Cricbuzz \t\t 20:-Gadgets 360
            
            """)
            search=input("Enter Website No. You want to visit:-")
            if search=='1':
                print("opening Chrome for you..!",end="\n")
                s.system("chrome stackoverflow.com ")
                s.system("cls")
            
            elif search=='2':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome github.com")
                s.system("cls")
                
            elif search=='3':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome geeksforgeeks.org")
                s.system("cls")
                
                
            elif search=='4':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome wikipedia.org")
                s.system("cls")
                
            elif search=='5':
                print("opening Chrome for you..!",end="\n")
                s.system("chrome youtube.com")
                s.system("cls")
                
                
            elif search=='6':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome twitter.com")
                s.system("cls")
                
                
            elif search=='7':
                print("opening Chrome for you..!",end="\n")
                s.system("chrome facebook.com")
                s.system("cls")
                
                
            elif search=='8':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome instagram.com")
                s.system("cls")
                
                
            elif search=='9':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome https://www.linkedin.com/")
                s.system("cls")
                
                
                
            elif search=='10':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome Indeed.co.in")
                s.system("cls")
                
                
                
            elif search=='11':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome Naukri.com")
                s.system("cls")
                
                
            elif search=='12':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome Monster.com")
                s.system("cls")
                
                
                
            elif search=='13':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome Amazon.in")
                s.system("cls")
                
                
                
                
            elif search=='14':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome flipkart.com")
                s.system("cls")
                
                
                
                
            elif search=='15':
                print("opening Chrome for you..!",end="\n")
                s.system("chrome zomato.com")
                s.system("cls")
                
                
                
            elif search=='16':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome swiggy.com")
                s.system("cls")
                
                
                
            elif search=='17':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome timesofindia.indiatimes.com")
                s.system("cls")
                
                
            elif search=='18':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome ndtv.com")
                s.system("cls")
            
            elif search=='19':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome cricbuzz.com")
                s.system("cls")
                
                
                
            elif search=='20':
                print("opening Chrome for you..!",end="\n")
                s.system(" chrome gadgets.ndtv.com")
                s.system("cls")
                
            else:
                print("Inavlid Number..!",end="\n")
                search_input=input("Enter Website You want  to visit:-")
                print("opening Chrome for you..!",end="\n")
                s.system("chrome"+search_input)
                s.system("cls")
            
            
            
            
            
            
            
                
    elif (("quit" in user_input) or ("exit" in user_input) or ("bie" in user_input) or ("close" in user_input) or ("stop" in user_input)):
        
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("quit" in user_input) or ("exit" in user_input) or ("bie" in user_input) or ("close" in user_input) or ("stop" in user_input)):
            #pt.speak("Anything else sir...!")
            print("Anything Else sir :)",end="\n")
            
            
        else:
            print("quiting...!",end="\n")
            s.system("cls")
            break
        
        
        
        
        
        
        
        
        
    elif (("open" in user_input) or ("launch" in user_input) or ("load" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and (("window" in user_input) or ("window media player" in user_input)) or (("window" in user_input) or ("window media player" in user_input)):
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("window" in user_input) or ("window media player" in user_input)):
                #pt.speak("Anything else sir...!")
                print()
                print("Anything Else sir :)",end="\n")
        else:
                print("opening window media player for you...!",end="\n")
                s.system("wmplayer")
                input("Enter to continue...!")
                s.system("cls")
                
      
    
    
    
    
    
    
             
    elif (("open" in user_input) or ("launch" in user_input) or ("load" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and (("sublime" in user_input) or ("text editor" in user_input) or ("sublime text editor" in user_input)) or (("sublime" in user_input) or ("text editor" in user_input) or ("sublime text editor" in user_input)):
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("sublime" in user_input) or ("sublime text editor" in user_input)):
                #pt.speak("Anything else sir...!")
                print("Anything Else sir :)",end="\n")
        else:
                print("opening sublime text editor for you...!",end="\n")
                sub.Popen("E:\software\sublime textr\sublime_text.exe")
                input("Enter to continue...!")
                s.system("cls")
                
                
    
    
    
    
    
    elif (("open" in user_input) or ("launch" in user_input) or ("load" in user_input) or ("run" in user_input) or ("execute" in user_input) or ("exec" in user_input) or "start" in user_input) and (("vs code" in user_input)   or ("vs" in user_input)  or ("visual studio code " in user_input)) or (("vs code" in user_input) or ("vs" in user_input) or ("visual studio code " in user_input)):
    
        if  (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input)) and (("vs code" in user_input)  or  ("vs" in user_input)  or ("visual studio code " in user_input)):
            #pt.speak("Anything else sir...!")
            print("Anything Else sir :)",end="\n")
            
            
        else:
            print("opening visual studio code for you...!",end="\n")
            sub.Popen(r"C:\Users\iNsEcT0R DeViL\AppData\Local\Programs\Microsoft VS Code\Code.exe") 
            input("Enter to continue...!")
            s.system("cls")
             
    
    
    
    
    elif (("run" in user_input) and ("date" in user_input)) or ("date" in user_input):
            
        if (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input))  and ("date" in user_input):
                #pt.speak("Anything else sir...!")
                print("Anything Else sir :)",end="\n")
            
            
        else:
            date=dt.datetime.now()
            print ("The time is now: = {0}:{1}:{2}".format(date.hour, date.minute, date.second))
            print("Date is = {0}:{1}:{2}".format(date.day,date.month,date.year))
            input("Enter to continue...!")
            s.system("cls")

           
        
        
        
        
        
    elif ("send message" in user_input) or ("whatsapp" in user_input):
        
        if (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input))  and (("send" in user_input) or ("message" in user_input)  or ("whatsapp" in user_input)):
                #pt.speak("Anything else sir...!")
                print("Anything Else sir :)",end="\n")
                
                
                
                
                
        else:
            number_input=input("whom  do you want to send message..?")
            if(("quit" in number_input) or ("exit" in number_input) or ("bie" in number_input) or ("close" in number_input) or ("stop" in number_input)):
                print("exiting...!")
                break

            message_input=input("Enter your message here:-")
            time_hour_input=int(input("What hour do you want to send the message:-"))
            time_miute_input=int(input("what time do you want to send message:-"))
            print("sending message to {} \n".format(number_input))
            wt.sendwhatmsg(number_input,message_input,time_hour_input,time_miute_input)
            input("Enter to continue...!")
            s.system("cls")
    
    
    elif (("send mail to gmail" in user_input) or ("send mail" in user_input) or ("send gmail" in user_input)) or ("gmail" in user_input):
        
        
        if (("no" in user_input) or ("dont" in user_input) or ("don't" in user_input))  and (("send mail to gmail" in user_input) or ("send mail" in user_input)):
            
            #pt.speak("Anything else sir...!")
            print("\nAnything Else sir :)",end="\n")
            
            
        else:
            
            user_email="mytest.test922@gmail.com"
            user_passwd="12@mytest.test"
            email_rece=input("whom do You want to send Email type Gmail Address:-")
            
            if(("quit" in email_rece) or ("exit" in email_rece) or ("bie" in email_rece) or ("close" in email_rece) or ("stop" in email_rece)):
                print("exiting...!")
                break
                
                
            email_message=input("type your message here:-")
            st=smt.SMTP("smtp.gmail.com",587)
            st.starttls()
            st.login(user_email,user_passwd)
            result=st.sendmail(user_email,email_rece,email_message)
            
            if(result!=None):
                print("Mail has been sented..!")
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
            
            7:-Date \t\t\t\t 8:-chrome
            
            """)

                 
        
    else:
        
        print("\nCommand not recognized try Help")
        
