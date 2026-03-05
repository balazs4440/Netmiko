from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**Router) as kapcsolat:
        
        roas = ["int g0/1"
                "no sh"
                "int g0/1.11",
                "encap dot1q 11",
                "ip add 192.168.11.11 255.255.255.0",
                "no sh",
                "int g0/1.13",
                "encap dot1q 13",
                "ip add 192.168.13.13 255.255.254.0",
                "no sh",]
        
    vlan = int(input("Adj meg egy vlan azonosítót: "))
    while(not(1 <= vlan <= 1005) or (vlan == 11) or (vlan == 13)):
        vlan = int(input("Adj meg egy vlan azonosítót(1 és 1005 között, 11 és 13 már foglalt!): "))
    ip = input("Add meg a vlan ip cimet: ")
    mask = input("Add meg a maszkot: ")
    print(vlan,ip,mask)
    
    
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")