pmt = [0,0,0,0,0]
symv = [0,0]
from tkinter import *

code = """
!10
%!5
%*Сет скрипт сношался с обамой?(0-да,1-нет)
#.
%>
%* Это правда
%>
%* Не правда

%<
@,
[
%>
]
#.


"""
x = 0
z_x = 0
z_y = 0
xx = 0
ccode = code.split("\n")
nd = ""
tabes = 0
nd += "pmt = [0,0,0,0,0]\n"
nd += "symv = [0,0]\n"
for line in ccode:
    
    try:
        if line[0]=="@":
            if line[1]=="+":
                nd += "    "*tabes + "pmt[x] += 1 \n"
                pmt[x] += 1
            if line[1]=="-":
                nd += "    "*tabes + "pmt[x] -= 1 \n"
                pmt[x] -= 1
            if line[1]==">":
                nd += "    "*tabes + "x += 1 \n"
                x += 1
            if line[1]=="<":
                nd += "    "*tabes + "x -= 1 \n"
                x -= 1
            if line[1]=="=":
                nd += "    "*tabes + "pmt[x] = " + (line+" ")[2:-1].replace(" ","") + "\n"
                pmt[x] = (line+" ")[2:-1]
            if line[1]==",":
                nd += "    "*tabes + "pmt[x] = int(input(':'))\n" 
        if line[0]=="!":
            
            for i in range(int((line+" ")[1:-1])):
                nd += "    "*tabes + "pmt.append(0) \n"
        if line[0:2]=="%!":
            #print((line+" ")[2:-1])
            for i in range(int((line+" ")[2:-1])):
                nd += "    "*tabes + "symv.append(0) \n"
        if line[0:2]=="%*":
            #print((line+" ")[2:-1])
            symv[xx] = (line+" ")[2:-1]
            nd += "    "*tabes + 'symv[xx] = "' + (line+" ")[2:-1] + '"\n'
        if line[0:2]=="#*":
            #print((line+" ")[2:-1])
            
            nd += "    "*tabes + 'print(pmt[xx],end="")\n'
        if line[0:2]=="#.":
            #print((line+" ")[2:-1])
            
            nd += "    "*tabes + 'print(symv[xx],end="")\n'
        if line[0:2]=="#/":
            nd += "    "*tabes + 'print("""\n""",end="")\n'

        if line[0:2]=="%>":
            xx += 1
            nd += "    "*tabes + "xx += 1 \n"
            
        if line[0:2]=="%<":
            xx -= 1
            nd += "    "*tabes + "xx -= 1 \n"
        if line[0:2]=="%,":
            nd += "    "*tabes + "symv[xx] = str(input(':'))\n" 
        if line[0] == "#":
            if line[1]=="/":
                nd += "    "*tabes + "pmt[x] = 0\n"
        if line[0] == "[":
            nd += "    "*tabes + "for i in range(pmt[x]):\n"
            tabes += 1
        if line[0] == "]":
            tabes -= 1
        
 
    except:
        pass
#print(nd)
print("",end="")
exec(nd)
        
 
