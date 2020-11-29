def ipv4(address):
    segs = address.split('.')
    if len(segs) != 4:
        return False
    for seg in segs:
        if int(seg) < 0 or int(seg) > 255:
            return False
    return True

address = input()
while address != '':
    print(ipv4(address))
    address = input()