string="she is beautiful and she is a good dancer"

#replace()
print(string.replace("is","was",2))

#find()
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)

#center()
name=input("enter your name: ")
print(name.center(len(name)+8,"*"))
