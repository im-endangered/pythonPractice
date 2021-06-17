# 1 for rock 2 for scissor 3 for paper ok?
import random
characters=[
    '''                                           
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  ''',
'''8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                 ''',
'''                                                                              
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                              '''
]
num=random.randint(0,2)
user_input=int(input("Enter what is your choice.\n0 for rock\n1 for paper\n2 for scissors\n"))
if user_input>2 or user_input<0:
    print("Madafaka. Type correct input")
else:
    print(f"\nYou chose\n{characters[user_input]}")
    print(f"\nComputer chose\n\n{characters[num]}")
    if user_input==0:
        if num==0:
            print("\nDraw.")
        elif num==1:
            print("\nYou lose.")
        else:
            print("\nYou win.")
    elif user_input==1:
        if num==0:
            print("\nYou win")
        elif num==1:
            print("\nDraw.")
        else:
            print("\nYou lose.")
    else:
        if num==0:
            print("\nYou lose")
        elif num==1:
            print("\nYou win.")
        else:
            print("\nDraw.")
