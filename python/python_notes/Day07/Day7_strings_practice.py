#Strings in Python
name="Krishnaveni"
print(name)
print(type(name),id(name))

#operations on string
#Concatenation(+)
k="Krishna"
v="Veni"
print(k+v)


a="Code"
b="Gnan"
print(a+b)

#Repeatation(*)

print(k*5)
print(a*3,b*2,k*5)

#Accessing string elements by using index

print(k[0])
print(v[2])
print(a[2],b[2])

#Slicing (To Extract portion of string)

print(k[-1])
print(k[1:4:1])
print(k[5:1:1])
#membership(in,not in)
print('veni' in name)
print('veni' not in name)


#Build in Functions in string
#Length
print(len(k))

#min() function

print(min(k))
print(max(k))
print(sorted(k))
print(chr(99))
print(ord('A'))


#Build in methods in python
#Case converting methods

print(k.upper())
print(k.lower())
print(k.islower())
print(k.isupper())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print(name.casefold())


#Aligment and formatting methods

l="Venky"
print(l.center(20,'*'))
print(l.ljust(9,'+'))
print(l.rjust(10,'-'))
print(l.zfill(10))

#Search and Find Methods

m="ChinTuchinni"
print(m.find('c'))
print(m.rfind('n'))
print(m.index('C'))
print(m.count('n'))

#String Testing Methods

print(m.startswith("Chi"))
print(m.endswith("nni"))
print(m.isalpha())
print(m.isalnum())
print(m.istitle())
print(m.isidentifier())
print(m.islower())
print(m.isupper())
print(m.isspace())


#Splitting methods

print(m.split(","))
print(m.strip())
print(m.encode())




output:

================================== RESTART: C:/Users/chinn/OneDrive/Desktop/pythonfullstack/python_notes/Day7_strings_practice.py =================================
Krishnaveni
<class 'str'> 1563233457776
KrishnaVeni
CodeGnan
KrishnaKrishnaKrishnaKrishnaKrishna
CodeCodeCode GnanGnan KrishnaKrishnaKrishnaKrishnaKrishna
K
n
d a
a
ris

True
False
7
K
s
['K', 'a', 'h', 'i', 'n', 'r', 's']
c
65
KRISHNA
krishna
False
False
Krishnaveni
Krishnaveni
kRISHNAVENI
krishnaveni
*******Venky********
Venky++++
-----Venky
00000Venky
6
10
0
3
True
True
True
True
False
True
False
False
False
['ChinTuchinni']
ChinTuchinni
b'ChinTuchinni'

