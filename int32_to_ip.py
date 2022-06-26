import ipaddress

addresses: list = [
    2149583361, # "128.32.10.1"
    32, # "0.0.0.32"
    0, # "0.0.0.0"
    2154959208, # "128.114.17.104"
    'gsdfgf', # TypeError
]

def int32_to_ip(int32: int) -> ipaddress.IPv4Address:
    try:
        ipv4_address = ipaddress.ip_address(int32)
        return ipv4_address
    except ValueError as error:
        print(error)




if __name__ == '__main__':
    for item in addresses:
        print(int32_to_ip(item))