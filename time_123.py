import time
# initial = time.time()
# print(initial)
# k=0
# while(k<100000):
#     print("life is beautifull")
#     k+=1
# print("while loop ran in ", time.time()-initial," second")
#
#
# initial2=time.time()
# for i in range (100000):
#     print("life is beautifull")
# print("for loop ran in ", time.time()-initial2," second")
#
#

localtime=time.asctime(time.localtime(time.time()))
print(localtime)