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

