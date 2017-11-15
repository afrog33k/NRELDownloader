#coding: utf-8

# This is the combination of several scripts that download data from the NREL NSRDB database
# Greg Jackson AESE Labs Imperial College. gr3gario on twitter and gregario on github
# Greg Jackson 29/11/2016 V2 - Updating to reflect new paper format, included ENO algorithm

import pandas as pd
import sys, os, io
import time
from datetime import date, datetime, timedelta
import calendar
from termcolor import colored
import csv
from NREL import *

def downloadNREL(location,lat,lon):
	if not os.path.exists('datasets'):
		os.makedirs('datasets')
		if debug: print "Directory Created"
	if os.path.exists('datasets/{}_NRELData_Raw.csv'.format(location)) is False:
		for key in years:
			flag = True
			attempts  = 0
			while flag and attempts < 10:
				attempts += 1 
				try:	
					time.sleep(1)
					if debug: print colored('started downloading %s data from the  year %d' %(location,key),'cyan')
					if key == 1998:
						print 'http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={key}&leap_day=false&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(key=key, lat=lat, lon=lon, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)

						df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={key}&leap_day=false&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(key=key, lat=lat, lon=lon, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=2)
						df.to_csv('datasets/{}_NRELData_Raw.csv'.format(location),mode='w')
					
					elif calendar.isleap(key) is True:
						if debug: print colored('And as %d is a leap year, make appropriate adjustments' %key,'blue')
						df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={key}&leap_day=true&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(key=key, lat=lat, lon=lon, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=3)
						df.to_csv('datasets/{}_NRELData_Raw.csv'.format(location), mode='a')
					
					else:
						df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={key}&leap_day=false&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(key=key, lat=lat, lon=lon, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=3)
						df.to_csv('datasets/{}_NRELData_Raw.csv'.format(location),mode='a')
					
					if debug: print colored('Finished downloading %s data  from the  year %d' %(location,key)	, 'green')
					flag = False 
					break

				except IOError as e:
					flag = True
					if debug: print colored('I/O error({0}): {1}'.format(e.errno, e.strerror),'red')
				
				except:
					if debug: print 'Unexpected error:', sys.exc_info()[0]
					flag = True 

def main():
	for (location,lat,lon) in locations:
		downloadNREL(location,lat,lon)

main()