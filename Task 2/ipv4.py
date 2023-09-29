import ipaddress

def is_valid_ipv4(ip_address):
    try:
        ip = ipaddress.IPv4Address(ip_address)
        return True
    except ipaddress.AddressValueError:
        return False

ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
