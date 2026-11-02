#jarvis level 3 -Ai assistant 
#Made by Rohit Rathee 
#Nov 2026
#Python-Basic-to-Advance
import datetime
print("Hello i'm jarvis ")
print("I'm made by master rathee")
print("what is your name")
name=input("enter name:")
print("welcome",name)
print("nice to meet you",name)

while True:
     print("How can i help you")
     print("I can do time,day,date,year,add,diff,multi,division")
     print("type stop to exit")
     problem=input("enter problem:").lower()
     if "stop" in problem or "exit" in problem:
             print("thank you",name)
             print("Have a nice day")
             break
     
     if "time" in problem:
        now=datetime.datetime.now()
        print("time:",now.strftime("%I:%M%p"))
        continue
     if "date" in problem:
         now=datetime.datetime.now()
         print("date:",now.strftime("%d-%m-%Y"))
         continue
     if "year" in problem:
         now=datetime.datetime.now()
         print("year is:",now.year)
         continue
     if "day" in problem:
         now=datetime.datetime.now()
         print("Today:",now.strftime("%A"))
         continue
     try:
          first=int(input("enter first:"))
          second=int(input("enter second:"))
          if "add" in problem:
             print(first+second)
          elif "diff" in problem:
                print(first-second)
          elif "multi" in problem:
                print("Answer:",first*second)
          elif "div" in problem:
                print(first/second)
          else:
                print("don't understand try time,add,diff")
     except:
                print("please enter only number for maths!")