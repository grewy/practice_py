

def convert_str(s):
    st = 97
    end = 122

    b= ""
    for x in s:
        if not (ord(x) >= st and ord(x) <= end):
            ord_ = ord(x)
        else:
            ord_ = ord(x)+2
            if ord_ > end:
                ord_ = ord_ % end + st -1

        b += chr(ord_)
    return b

a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

print convert_str(a)
