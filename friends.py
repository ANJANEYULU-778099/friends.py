my_friends1={"6th class": ["srinu","sunil","bada","srinath"],
             "7th class": ["gopi","pavan","dasu","ajay",],
             "8th class": ["sunil","charan","pani","chanti"]}
print(my_friends1["6th class"][2]) 
smalllist={"child age": ["school","playing","sleeping"],
           "teen age": ["college","hardwork","sleeping"]}
smalllist.update({"adult age": ["jobs","shoping","sleeping"]})
print(smalllist)
for i in smalllist.values():
    print(i)
for i in smalllist.keys():
    print(i)
count=0    
for j in i:
        if j == "sleeping":
              count = count +1
              print(j)
print("count",count)
