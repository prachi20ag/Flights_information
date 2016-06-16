#!/usr/bin/python
import requests
import bs4
import os
import sys
from selenium import webdriver

os.system('clear')

status=open('search_result.txt','a')

def flight():
    source=raw_input('Enter the code of source: ')
    dest=raw_input('Enter the code of destination: ')
    journey_type=raw_input('Enter 1 for one-way travel and 2 for both ways: ')
    if(str(journey_type)=='1'):
        sdate=raw_input('Enter the date of journey in DD/MM/YYYY format: ')
        rdate=''
        url="http://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin="+str(source)+"&originCountry=IN&destination="+str(dest)+"&destinationCountry=IN&flight_depart_date="+str(sdate)+"&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home-pg"
    	driver= webdriver.Firefox()
    	driver.get(url)
    	html2 = driver.execute_script("return document.documentElement.innerHTML;")
    	soup=bs4.BeautifulSoup(html2,"lxml")
    	rows=soup.findAll("articlewithbanner")
    	print ("\n-----------------------------------Flights available at your service-------------------------\n\n")
    	status.write ("                        Flights available at your service"+"\n\n")
    	print (" Flight\t\t\t\t\tDeaprture\t\tArrival\t\t\tTime\t\t\t\t    Price(per adult)\n")
    	status.write (" Flight\t\t\t\tDeaprture\t\tArrival\t\t\tTime\t\t\t    Price(per adult)\n")
    	for row in rows:
	 	lists = row.select('li')
         	name= lists[0].get_text("|", strip=True)
	 	time= lists[1].select("div")
	 	start_time= time[0].get_text("|", strip=True)
	 	end_time=time[1].get_text("|", strip=True)
	 	duration = time[2].get_text("|", strip=True)
	 	price1=lists[5].select('div')
         	price2=price1[0].select('label')
         	if len(price2)>0:
           	   price_temp=price2[0].select('del')
           	   price=price_temp[0].get_text(" ", strip=True)
                if(len(price)>4):
                	ans=str(" "+name.ljust(35)+"\t"+start_time.ljust(20)+"\t"+end_time.ljust(20)+"\t"+duration.ljust(35)+"\t"+price.ljust(10)+"\t\n")
                	print str(ans)
			status.write (ans)
 	print '-------------------------------------------------------------------------------------------------------------------------------'
        status.write('---------------------------------------------------------------------------------------------------------------------------------------')
    else:
	sdate=raw_input('Enter the date of start in DD/MM/YYYY format: ')
        rdate=raw_input('Enter the date of return in DD/MM/YYYY format: ')
	url="http://flight.yatra.com/air-search-ui/dom2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin="+str(source)+"&originCountry=IN&destination="+str(dest)+"&destinationCountry=IN&flight_depart_date="+str(sdate)+"&arrivalDate="+str(rdate)+"&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home-pg"
	driver= webdriver.Firefox()
    	driver.get(url)
    	html2 = driver.execute_script("return document.documentElement.innerHTML;")
    	soup=bs4.BeautifulSoup(html2,"lxml")
	frontrows = soup.select('#resultList_0 articlewithbanner')
	backrows = soup.select('#resultList_1 articlewithbanner')
    	print ("\n---------------------------------------------Flights available at your service-------------------------------\n\n")
    	status.write ("\n                        Flights available at your service"+"\n\n")
    	print (" Flight\t\t\t\t\tDeaprture\t\tArrival\t\t\tTime\t\t\t\t    Price(per adult)\n")
    	status.write (" Flight\t\t\t\t\tDeaprture\t\tArrival\t\t\tTime\t\t\t\t    Price(per adult)\n")
	print ("\n                                FROM "+str(source)+" TO "+str(dest)+"                              \n")
	status.write("\n                          FROM "+str(source)+" TO "+str(dest)+"                              \n")
    	for row in frontrows:
	 	lists = row.select('li')
		length = len(lists)
		length = length/2;
         	name= lists[0].get_text("|", strip=True)
	 	time= lists[1].select("div")
	 	start_time= time[0].get_text("|", strip=True)
	 	end_time=time[1].get_text("|", strip=True)
	 	duration = time[2].get_text("|", strip=True)
	 	price1=lists[5].select('div')
         	price2=price1[0].select('div')
		if len(price2)>0:
           	   price_temp=price2[0].select('span')
           	   price=price_temp[0].get_text("", strip=True)
                if(len(price)>4):
                	ans=str(" "+name.ljust(35)+"\t"+start_time.ljust(20)+"\t"+end_time.ljust(20)+"\t"+duration.ljust(35)+"\t"+price.ljust(10)+"\n")
			print str(ans)
			status.write (ans)
 	print ('---------------------------------------------------------------------------------------------------------------------------------------')
        status.write ('-----------------------------------------------------------------------------------------------------------------------------------------')

	print ("\n                                FROM "+str(dest)+" TO "+str(source)+"                              \n")
	status.write("\n                          FROM "+str(dest)+" TO "+str(source)+"                              \n")
	for row in backrows:
	 	lists = row.select('li')
		length = len(lists)
		length = length/2;
         	name= lists[0].get_text("|", strip=True)
	 	time= lists[1].select("div")
	 	start_time= time[0].get_text("|", strip=True)
	 	end_time=time[1].get_text("|", strip=True)
	 	duration = time[2].get_text("|", strip=True)
	 	price1=lists[5].select('div')
         	price2=price1[0].select('div')
		if len(price2)>0:
           	   price_temp=price2[0].select('span')
           	   price=price_temp[0].get_text(" ", strip=True)
                if(len(price)>4):
                	ans=str(" "+name.ljust(35)+"\t"+start_time.ljust(20)+"\t"+end_time.ljust(20)+"\t"+duration.ljust(35)+"\t"+price.ljust(10)+"\n\n")
                	print str(ans)
			status.write (ans)
 	print ('-------------------------------------------------------------------------------------------------------------------------------------')
            
        status.write ('---------------------------------------------------------------------------------------------------------------------------------------')

	 #print (duration+"\n")

print ('Get Flight Information\n')
status.write('Get Flight Information\n')
flight()


    
    
