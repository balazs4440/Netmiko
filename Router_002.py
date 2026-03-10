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
    
    while ip == "" or ip.isalpha() or len(ip.strip().split('.')) != 4:
        ip = input("Adja meg a vlan ip cimet:")
        
    valt2 = ip.strip().split('.')
    
    while not(valt2[0].isdigit() and valt2[1].isdigit() and valt2[2].isdigit() and valt2[3].isdigit()):
        ip = input("Adja meg a vlan ip cimet:")
        valt2 = ip.strip().split('.')
    
    valt3 = ip.strip().split('.')
        
    while 255 < int(valt3[0]) or 255 < int(valt3[1]) or 255 < int(valt3[2]) or 255 < int(valt3[3]):
        ip = input("Adja meg a vlan ip cimet:")
        valt3 = ip.strip().split('.')
    
    while 0 > int(valt3[0]) or 0 > int(valt3[1]) or 0 > int(valt3[2]) or 0 > int(valt3[3]):
        ip = input("Adja meg a vlan ip cimet:")
        valt3 = ip.strip().split('.')


    mask = input("Add meg a maszkot: ")

        
    while   mask == "" or  mask.isalpha() or len(mask.strip().split('.')) != 4:
        mask = input("Add meg a maszkot:")
            
    valt4 = mask.strip().split('.')
        
    while not(valt4[0].isdigit() and valt4[1].isdigit() and valt4[2].isdigit() and valt4[3].isdigit()):
        mask = input("Add meg a maszkot:")
        valt4 = mask.strip().split('.')
        
    valt5 = mask.strip().split('.')
        
    while 255 < int(valt5[0]) or 255 < int(valt5[1]) or 255 < int(valt5[2]) or 255 < int(valt5[3]):
        mask = input("Add meg a maszkot:")
        valt5 = mask.strip().split('.')
        
    while 0 > int(valt5[0]) or 0 > int(valt5[1]) or 0 > int(valt5[2]) or 0 > int(valt5[3]):
        mask = input("Add meg a maszkot:")
        valt5 = mask.strip().split('.')
    
    print(vlan,ip,mask)
    
    
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")