import socket


def palindron(tex):
    words = tex.split()
    vocabulary = []
    for word in words:
        if word == word[::-1]:
            vocabulary.append(word)
    return vocabulary

def validate_ip(ip_address):
    if len (ip_address) < 7:
        raise Exception("The argument must contain a string longer than 7 characters")
    elif not isinstance(ip_address, str):
        raise Exception(" The argument must contain the string")
    elif socket.inet_aton(ip_address):
        return True
    else:
        return False

def get_os():
    oper_sys= platforms.system()
    if oper_sys == "Windows":
        return "Windows"
    elif oper_sys == "Linux":
        return "Linux"
    elif oper_sys == "Darwin":
        return "Mac"
    else:
        return oper_sys






