buf=''
stringi=False
fx=open("kod.html", "w")

d={
    "for":"orange",
    "if":"orange",
    "else":"orange",
    "while":"orange",
    "class":"orange",
    "int":"blue",
    "float":"blue",
    "String":"blue",
    "double":"blue",
    "bool":"blue",
    "static":"orange",
    '{':"yellow",
    '}':"yellow",
    '(':"yellow",
    ')':"yellow",
    '=':"yellow",
    '+': "yellow",
    '-': "yellow",
    '*': "yellow",
    '/': "yellow",
    '%': "yellow",
    ';': "yellow",
    ',':"yellow",
    '.':"yellow",
    ' ':"yellow"

}


def skaner(c):
    global buf
    global d
    #global stringi

    global fx

    if c in d.keys():
        if buf!="":
            fx.write("<span style=\"color: "+"black"+"\">"+buf+"</span>")
            buf = ""
        if c==' ':
            fx.write("<span style=\"color: " + d[c] + "\">&nbsp</span>")
            return
        fx.write("<span style=\"color: " + d[c] + "\">" + c + "</span>")
        return
    buf+=c
    if(buf in d.keys()):
        fx.write("<span style=\"color: " + d[buf] + "\">" + buf + "</span>")
        buf=""
    return









f=open("kod.txt", 'r')


for line in f:
    for c in line:
        skaner(c)
    print("xD")
    fx.write("<br>")


f.close()
fx.close()
