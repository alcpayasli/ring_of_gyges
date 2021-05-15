# -*- coding: utf-8 -*- 
from my_modules.my_mac_changer import My_Mac_Changer
from my_modules.my_print_colored import print_style

while True:
    print(print_style.CYELLOW + """
WELCOME TO RING OF GYGES 
!!! THIS APP MAC CHANGER FOR ETHICAL HACKING ON KALI!!!
*********************************
OPERATIONS:
1-RANDOM MAC
2-PRIVATE MAC
3-RETURN ORGINAL MAC
4-SHOW CURRENT MAC
0-QUIT
********************************* 

""" + print_style.CYELLOW)
    #start operation block
    operation = input( print_style.CYELLOW + "\nChoice Operation:" + print_style.CYELLOW)
    if operation == "0":
        print( print_style.CRED + "Exciting......" + print_style.CRED)
        break
    elif operation == "1" or operation == "2" or operation == "3" or operation == "4":
        while True:
            #start interface choice block
            inter_face = input(print_style.CYELLOW+ "\tChoice Interface\n\t1.Wlan0\n\t2.Eth0\n\t0.Return Main Menu\n\n\tChoice:" + print_style.CYELLOW)
            if inter_face == "1":
                my_mac_app = My_Mac_Changer("wlan0")
                if operation == "1":
                    try:
                        my_mac_app.random_mac()
                        print(print_style.CGREEN + "Your mac changed successfully"+ print_style.CGREEN)                        
                        break
                    except:
                        print(print_style.CRED + "Error" + print_style.CRED)
                elif operation == "2":
                    private_mac = input(print_style.CYELLOW+"Input new mac address:"+ print_style.CYELLOW)
                    if len(private_mac)!= 17:
                        print(print_style.CRED + "Please input valid macaddress Example: a1:b2:cc:dd:ee:ff" + print_style.CRED)
                    else:
                        try:
                            
                            my_mac_app.private_mac(private_mac)
                            print(print_style.CGREEN + "Your mac changed successfully"+ print_style.CGREEN)
                            break
                        except:
                             print(print_style.CRED + "Error" + print_style.CRED)
                elif operation == "3":
                    try:
                        
                        my_mac_app.orginal_mac()   
                        print(print_style.CGREEN+ "Your mac returned orginal mac successfully" + print_style.CGREEN)                     
                        break
                    except:
                        print(print_style.CRED + "Error" + print_style.CRED)
                elif operation == "4":
                    try:
                        my_mac_app.show_mac_address()
                        break
                    except:
                        print(print_style.CRED + "Error" + print_style.CRED)
            elif inter_face == "2":
                my_mac_app = My_Mac_Changer("eth0")
                if operation == "1":
                    try:
                        
                        my_mac_app.random_mac()
                        print(print_style.CGREEN + "Your mac changed successfully"+ print_style.CGREEN)                        
                        break
                    except:
                        print(print_style.CRED + "Error" + print_style.CRED)
                elif operation == "2":
                    private_mac = input(print_style.CYELLOW+"Input new mac address:"+ print_style.CYELLOW)
                    if len(private_mac)!= 17:
                        print(print_style.CRED + "Please input valid macaddress Example: a1:b2:cc:dd:ee:ff" + print_style.CRED)
                    else:
                        try:
                            my_mac_app.private_mac(private_mac)
                            print(print_style.CGREEN + "Your mac changed successfully"+ print_style.CGREEN)
                            break
                        except:
                             print(print_style.CRED + "Error" + print_style.CRED)
                elif operation == "3":
                    try:
                        
                        my_mac_app.orginal_mac()                 
                        print(print_style.CGREEN+ "Your mac returned orginal mac successfully" + print_style.CGREEN)       
                        break
                    except:
                        print(print_style.CRED + "Error" + print_style.CRED)
                elif operation == "4":
                    try:
                        my_mac_app.show_mac_address()
                        break
                    except:
                        print(print_style.CRED + "Error" + print_style.CRED)
            elif inter_face == "0":
                print(print_style.CYELLOW + "Returning main menu" + print_style.CYELLOW)
                break
            else:
                print(print_style.CRED + "Please choice 1,2 or 0" + print_style.CRED)
            #stop interface choice block                                    

            
       
            
    else:
        print(print_style.CRED + "Invalıd operation. Please choice valid operation." + print_style.CRED)
    #stop operation choice block
