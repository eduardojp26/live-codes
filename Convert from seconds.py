def change(seconds):
    hours=seconds//3600
    seconds=seconds%3600
    minutes=seconds//60 
    seconds=seconds%60
    print("Hours:",hours)   #printing hours 
    print("Minutes:",minutes) #printing minutes 
    print("Seconds:",seconds) #printing seconnds
    
n=int(input())
change(n)