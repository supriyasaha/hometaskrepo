 already installed virtual environment

Now to work in a virtual environment we use

step
----
      [supriya@localhost] ~ $  cd virtual

  virtual $  source virt1/bin/activate

 (virt1) $  vim b.py

  (virt1)$  

The code is about printing the title and the author name of each blog post from the blog site 'http://planet.fedoraproject.org'


now if we run the file using ./b.py we output

(virt1)$ ./b.py

output:
--------

  title: CatN | CentOS Dojo 
 author: Richard W.M. Jones

 title: Daily log July 11th 2013 
 author: Dave Jones



Code of the program

.. code:: python

 #!/usr/bin/env python
 from bs4 import BeautifulSoup
 import requests
 import urllib2

 url = 'http://planet.fedoraproject.org'

 html_doc = urllib2.urlopen(url) #extract the html document frm the website
 data=html_doc.read() #reads the file

 soup = BeautifulSoup(data) #parse the data

 title = soup.findAll('div', attrs={'class' : 'blog-entry-title'}) #this extracts the title of each blog post with attribut class='blog-entry-title' and tag 'div'
 author = soup.findAll('div', attrs={'class' : 'blog-entry-author'})#this extracts the author name of each blog post with attribute class='blog-entry-author' and tag='d iv'

 length=len(author) #to get the total number of post in the blog

  for x in range(length):

    print "title: %s " % title[x].find('a').string #to print the title of each post
    print "author: %s" % author[x].find('a').string #to print the name of each  post

  html_doc.close()


the link to the code is: https://github.com/supriyasaha/hometaskrepo/blob/master/planetparser/planetparser.py


