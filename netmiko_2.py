from netmiko import ConnectHandler
"""Router={
	"device_type": "cisco_ios",
	"ip": "sandbox-iosxe-latest-1.cisco.com",
	"username": "developer",
	"password": "C1sco12345"
}"""

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }

        net_connect = ConnectHandler(**Router)
        print('Connecting to '+IP)
        print('-'*79)
        output=net_connect.send_command('sh ip int bri')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()
