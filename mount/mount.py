#!/usr/bin/env python
s=open("/proc/mounts") #opens he file mount.py

f=s.read() #reads the content of the file /proc/mounts
z=f.split("\n") #split the content into each member with respect to "\n"
p=len(z) #counts the total number of member
i=1
while i < p:    #conditon to check

        a=z[i].split(" ") #split each member of z further into members  
        a.insert(1," on ") #adds "on" at  position 1
        a.insert(3," type ") #adds "type" at position 3 
        a.insert(5," (") #add (
        a.insert(7,")")# adds )
        del a[-2] #delete second last element
        del a[-1] #deletes the last element
        str="".join(a) #joins the member of a
        print str #print 
        i+=1 #increase i by 1

s.close() #close the file /proc/mounts

