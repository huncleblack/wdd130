
# this is a compound list
nunbers= [1,2,3,['a', 'b', 'c']]
alph=nunbers[3]
print(alph[2])



#this is a dictionary list
book={'name': '1st john', 'chapter': 20, 'verse' :10}
book['vilage']= "amachi"
print(book)

del book['vilage']
print(book)

#this is a new variable code
fabric=[]

fabric.append("cutton")
fabric.append("cashmere")
fabric.append("wool")
fabric.insert(0, "plasma")
fabric.insert(2, "satin")


print(fabric)

if "satin" in fabric:
    print("satin is in list ")

else:
    print("satin is not in list")

fabric.pop([1])
print(fabric)