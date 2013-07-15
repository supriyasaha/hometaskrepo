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

