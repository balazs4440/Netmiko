from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


def vlan(ssh):
    vlanok = ("vlan 10",
              "name Tanulo",
              "vlan 20",
              "name Oktato",
              "vlan 30",
              "name Pedagogus",
              "vlan 100",
              "name Ugyvitel"
             )
    ssh.send_config_set(vlanok)


def jelszoallitas(jelszo):
    konpass = ("line console 0",
               "password konJelszo"
               )
    jelszo.send_config_set(konpass)

def intdb(ssh):
    intlista2 = []
    intlista3 = []
    intlista4 = []
    interface = ssh.send_command("sh run | inc Ethernet")
    interfacelista = interface.split("\n")
    for i in range(len(interfacelista)):
        intlista2.append(interfacelista[i].split(" ")[1])
    for i in range(len(intlista2)):
        intlista3.append(intlista2[i].split("/")[0])
    for i in range(len(intlista3)):
        intlista4.append(intlista3[i][:-1])
    #print(intlista4)
    asd = intlista4[1]
    db = 0
    for i in range(len(intlista4)):
        if intlista4[i] == asd:
            db += 1
        else:
            print(asd,db)
            asd = intlista4[i]
            db = 1
    print(asd,db)


try:
    with ConnectHandler(**login_adatok)as kapcsolat:
        vlan(kapcsolat)
        print(kapcsolat.send_command("sh vl br"))
        
        jelszoallitas(kapcsolat)
        print(kapcsolat.send_command("sh run"))

        intdb(kapcsolat)

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")

def konzol_jelszo():
    with open("konzol.txt")as runconf:
        