d=open('Image.jpg','rb').read()
f=open('ff.txt','wb').write(d)
w=open('ff.txt','rb').read()
print(len(w))  