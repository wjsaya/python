from multiprocessing import Pool
import time
def myFun(i):
    print (i+100)
    

p = Pool(5)

# print(p.map(myFun,range(10))) 
for i in range(10):
    p.apply_async(func=myFun,args=(i,))

print("end")
p.close()
print ("ss")
p.join()
