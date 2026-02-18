from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}



try:
    with ConnectHandler(**kapcsolo) as kapcsolat:
        kapcsolat.send_config_set("login block-for 600 attempts 3 within 60")

        user = kapcsolat.send_command("sh run | sec username")
        userpwd = user.split(" ")[-1]
        if (len(userpwd) == 0):
            print("nincs user jelszó")
        else:
            print(userpwd)

        ena = kapcsolat.send_command("sh run | sec enable password")
        enapwd = ena.split(" ")[-1]
        if (len(enapwd) == 0):
            print("nincs enable jelszó")
        else:
            print(enapwd)
        
        if (len(userpwd) < 8):
            reuserpass = input("A felhasználó jelszó túl rövid adj meg újat: ")
        elif(len(enapwd) < 8):
            reenapass = input("Az enable jelszó túl rövid adj meg újat: ")
            
except Exception as ex:
    print(f"Hiba:{ex}")

