CODE TO THE PROGRAM
--------------------

#!/usr/bin/env python
import urllib2
import sys

def get_value(nasdaq): #to get the share value of nasdaq

        url='http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1' % (nasdaq) #this the url of the nasdaq syambol extracted from yahho.finance
        con=urllib2.urlopen(url) #to open the url
        val=con.read() #to read the current share value of nasdaq symbol from yahho.finanace
        print "the cureent sharevalue is %s" % (val)

if __name__ == '__main__': #it recieves the desire coed and calls tha funtion to geth the current sharevalu
    if len(sys.argv) == 2: #condition to check whter the file name in the command line does not exceed two
      get_value(sys.argv[1]) #passe the nasdaq to the main user
    else:
      print "Give only one NASDAQ symbol at a time after command line argument!"
    sys.exit(0)



The explanation o the code
---------------------------
Here we use import urllib2 to get the current share value of symbol NASDAQ by using a function get_val.Now we open the url lin and read it to get the current sharevalue and print it.
'_main_' is used to check weather in the command line input only one input symbol  is given or more than one.If it exceed two includin the  ./shareval.py then it will exit else it will print the current sharevalue of the symbol

the link to the code is https://github.com/supriyasaha/hometaskrepo/blob/master/sharevalue/shareval.py
