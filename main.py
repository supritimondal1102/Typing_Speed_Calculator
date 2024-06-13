from time import *
import random as r



def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error        

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R 
    return round(speed)


test =["The queen of the hills is a Himalayan city in the Indian state of West Bengal",
"It is internationally renowned as a tourist destination for its spectacular view of Mt",
"Kanchandzonga, along with its tea industry and the Darjeeling Himalayan Railway, a UNESCO World Heritage site",
" One can have the view of entire Singalila Range along with Mt.Kanchandzonga, Bhutan Himalaya and a part of Everest range from Darjeeling", 
"The eye caching valleys, meandering rivers and of course the lush green tea gardens are the unique features of Darjeeling",
"Beside all these the main attractions of this popular hill stations are Himalayan Mountaineering Institute (HMI) , Himalayan Zoo , Tiger Hill , Rock Garden , Batashiya Loop"]
test1 = r.choice(test)
print("     ***** typing speed *****")
print(test1)
print()
print()
time_1 = time()
testinput = input(" Enter : ")
time_2 = time()

print('speed : ', speed_time(time_1,time_2,testinput)," w/sec")
print("error :", mistake(test1,testinput))
