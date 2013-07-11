
#!/usr/bin/env python
s=open("/proc/mounts") #this open command opens the file /proc/mounts


now we have to read the contents of the file so that we are able to make the changes to get the desired output

f=s.read() #reads the content of the file

The algorithm 
----------------------------------------
Split the file into each member with respest to "\n" so that we get each line as a member

z=f.split("\n") # splits the file
p=len(z) #coounts the lenth or the number of member in z
i=1

Here while loop is used so that now frm z each member is taken and it is again splitted into members with respect to space so that we get each word of each line as a single member

while i < p: #checks for condition for i should be less than the size of z


        a=z[i].split(" ") # it splits every member of z again into members with respect to space 

Now to bring about the changes for the desired ouput we will add "on" after every first word, add "type" after every third word, add open and close first brackets and delete the last two zeros from the file /proc/mounts

        a.insert(1," on ")# adda "on" at position 1 i.e after the firts word of each line
        a.insert(3," type ") # adds "type" at position 3 i.e after the third word of each line
        a.insert(5," (") # adds "(" at fifth position i.e before rw at each line
        a.insert(7,")")# adds ")" at 7th position 
        del a[-2]#this commands deletes the second last member
        del a[-1]# this command deleted the last member

now the members of a is joined to form a complete line and is then printed

        str="".join(a) #joins the memebr of a
        print str #prints after the changes are  made
        i+=1 # increases i by one each time

s.close() #closes the file /proc/mounts

hence the code is:

https://github.com/supriyasaha/hometaskrepo/blob/master/mount/mount.py
