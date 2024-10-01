# f=open("exam/demo","x")
# f.write("WELCOME")
# f=open("Exam/demo","r")
# f.write("\nWELCOME Guys")

f=open("Exam/demo","r")
l=len(f.readlines())
f.seek(0)
long=' '
for i in range(l):
    a=f.readline().strip()
    s=a.split(' ')
    for j in s:
        if j!='':
            if len(long)<len(j):
                long=j
print("Longest Word=",long)
