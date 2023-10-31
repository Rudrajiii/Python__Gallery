with open ('toy.txt','r') as f1:
    content=f1.read()
# with open ('paradox.txt','a') as f2 :
t= open ('paradox.txt','a')  
    # f2.write(content)
for i in range(1,21):
  source_range="\n\n"+str(i)
  t.write(source_range)
t.write(content)
t.close()
    
# f=open("paradox.txt",'w')
# for i in range(1,21):
#     source_range="\n"+str(i)
#     f.write(source_range)
# f.close()
f=open("rudra.txt", 'a')
li=[2,3,4,5,6,8]
fog='\n\n'+str(li)
f.write(fog)
f.close()



         
