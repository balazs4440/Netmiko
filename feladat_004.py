from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**kapcsolo) as kapcsolat:
        
        kapcsolat.send_config_set(["login block-for 600 attempts 3 within 180"])
        print(kapcsolat.send_command("show run | include password"))
        
        jelszavak = []
        
        ena = kapcsolat.send_command("show run")
        if "enable password" in ena:
            if len(kapcsolat.send_command("show run | include enable password").split(' ')[-1]) < 8:
                print("A privilegizált jelszó nem megfelelő hosszúságú.")
                enajelszo = input("ADj meg egy legalább 8 karakter hosszú jelszót: ")
                kapcsolat.send_config_set(f"enable password {enajelszo}")
        
        ena = kapcsolat.send_command("show run")
        if "username" in ena:
            val = kapcsolat.send_command("show run | include username").split('\n')
            print(val)
            
            for felh in val:
                if len(felh.split(' ')[-1]) < 8:
                    print(f"A {felh.split(' ')[1]} felhasználó jelszava nem megfelelő hosszúságú.")
                    usejelszo = input("Adj meg egy legalább 8 karakter hosszú jelszót: ")
                    while len(usejelszo) < 8:
                        usejelszo = input("Adj meg egy legalább 8 KARAKTER HOSSZÚ jelszót!: ")
                    osszerakott = ''
                    for szo in felh.split(' ')[:-2]:
                        osszerakott += szo + ' '
                    kapcsolat.send_config_set(f"{osszerakott}{usejelszo}")
                    print("A jelszó beállítása megtörtént.(°_,°)")
            
                    
            
                
            

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")

"""try:
    with ConnectHandler(**kapcsolo) as kapcsolat:

    
        valasz = kapcsolat.send_command("show run")
        if "enable password" in valasz:
            jelszo = kapcsolat.send_command("show run | include enable password").split(' ')[-1]
            print(jelszo)
            if len(jelszo) < 8:
                print("Az enable jelszó nem megfelelő hosszúságú.")
                ujjelszo = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                while len(ujjelszo) < 8:
                    ujjelszo = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                kapcsolat.send_config_set(f"enable password {ujjelszo}")
                print("A jelszó beéllítása megtörtént.")
            else:
                print("Megfelelő az enable jelszó")
                
        konzol = kapcsolat.send_command("sh run | section line con")
        konzol = konzol.split("\n")
        print(konzol)
        for i in konzol:
            if i.strip().startswith('password'):
                if len(i.split(' ')[-1]) < 8:
                    print("A konzol jelszó nem megfelelő hosszúságú.")
                    
                    ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    while len(ujjelszo2) < 8:
                        ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    kapcsolat.send_config_set(["line con 0" , f"password {ujjelszo2}"])
                    print("A jelszó beállítása megtörtént.")
                else:
                    print("Megfelelő a konzol jelszó")   
        #--------------------
        vty = kapcsolat.send_command("sh run | section line vty")
        vty = vty.split("\n")
        print(vty)
        for i in vty:
            if i.strip().startswith('password'):
                if len(i.split(' ')[-1]) < 8:
                    print("A vty jelszó nem megfelelő hosszúságú.")
                    
                    ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    while len(ujjelszo2) < 8:
                        ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    kapcsolat.send_config_set(["line con 0" , f"password {ujjelszo2}"])
                    print("A jelszó beállítása megtörtént.")
                else:
                    print("Megfelelő a vty jelszó")
        
            
except Exception as ex:
    print(f"Hiba: {ex}")




try:
    with ConnectHandler(**kapcsolo) as kapcsolat:
        kapcsolat.send_config_set("login block-for 600 attempts 3 within 60")

        user = kapcsolat.send_command("sh run | inc username")
        userpwd = user.split(" ")[-1]
        if (len(userpwd) == 0):
            print("nincs user jelszó")
        else:
            print(userpwd)

        ena = kapcsolat.send_command("sh run | inc enable password")
        enapwd = ena.split(" ")[-1]
        if (len(enapwd) == 0):
            print("nincs enable jelszó")
        else:
            print(enapwd)
        
        if(len(userpwd) < 8):
            reuserpass = input("A felhasználó jelszó túl rövid adj meg újat: ")
        elif(len(enapwd) < 8):
            reenapass = input("Az enable jelszó túl rövid adj meg újat: ")
        else:print("Minden jól van beállítva!")
            
except Exception as ex:
    print(f"Hiba:{ex}")

"""