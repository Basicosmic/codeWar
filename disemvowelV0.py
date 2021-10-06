def disemvowel(string_):
    strList= []
    for i in string_:

        strList.append(i)
    for i in strList:
        if i.lower() == 'a' or i.lower() == 'o' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'u':
            strList.remove(i)
    string_ = ''.join(i for i in strList)
    return string_