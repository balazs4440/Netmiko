from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**Router) as kapcsolat:

        neighbor = kapcsolat.send_command("sh ip ospf neig")
        neighbor = neighbor.strip().split("\n")[1:]
        
        print(len(neighbor),"szomszéd található a hálózaton.")
        
        valt = kapcsolat.send_command("sh run | inc ospf")
        
        ospf = [valt,
                "network 172.162.219.12 0.0.0.3 area 0"
                ]
        
        kapcsolat.send_config_set(ospf)
        
        reference = int(input("Add meg a referencia sávszélességet [100, 1000, 10000]:"))
        
        while reference != 100 and reference != 1000 and reference != 10000:
            reference = int(input("Add meg a referencia sávszélességet [100, 1000, 10000]:"))
        
        reference = str(reference)
        
        ref = [valt,
                f"auto-cost refer {reference}"
               ]
        
        kapcsolat.send_config_set(ref)
        
        id = input("Adj meg a router azonosítót:")
        
        while id == "" or id.isalpha() or len(id.strip().split('.')) != 4:
            id = input("Adj meg a router azonosítót:")
            
        valt2 = id.strip().split('.')
        
        while not(valt2[0].isdigit() and valt2[1].isdigit() and valt2[2].isdigit() and valt2[3].isdigit()):
            id = input("Adj meg a router azonosítót:")
            valt2 = id.strip().split('.')
        
        valt3 = id.strip().split('.')
        
        while int(valt3[0]) and int(valt3[1]) and int(valt3[2]) and int(valt3[3]) > 255:
            id = input("Adj meg a router azonosítót:")
            valt3 = id.strip().split('.')
        
        while int(valt3[0]) and int(valt3[1]) and int(valt3[2]) and int(valt3[3]) < 0:
            id = input("Adj meg a router azonosítót:")
            valt3 = id.strip().split('.')
        
        routerid = [valt,
                  f"router-id {id}"
                 ]
        
        kapcsolat.send_config_set(routerid)
         
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")