from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}



try:
    with ConnectHandler(**kapcsolo) as kapcsolat:
        tftp_ip = input("Add meg a szerver IP-címét!: ")
        fajlnev = input("Add meg a mentendő fájl nevét: ")
        
        kapcsolat.send_multiline_timing(["cop ru tf", tftp_ip, fajlnev])


        
except Exception as ex:
    print(f"Hiba:{ex}")
    