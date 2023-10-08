users=['dave','renson', 'gitonga']
data=['dave',42,'true']
emptylist=[]
print ("dave" in data)
print(users [0])
print(users[1] )
print(users[2] )
print(users[-2] )
print(users.index('gitonga'))
print(users[1:])
print (len(users))
users.append('embian')
print(users)
users +=(['besty'])
print(users)
users.extend(['shorty','blacky'])
print(users)

users.insert(0, 'smily babe')
print(users)
users[1:1]=(['one of a kind'])
print(users)
users.remove('shorty')
print(users)

print((users).pop())
print(users)

del users[0]
print(users)


data.clear()
print(data)

users.sort()
print(users)
users[1:2]=['Swee']
users.sort()
print(users)