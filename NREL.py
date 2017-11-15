#coding: utf-8

# Configuration file for NREL data call 
# This file sets up the calls for data from NREL. 
# 26/05/2016 Greg Jackson AESE Labs Imperial College 
from datetime import date, datetime, timedelta

debug = True

# Location variables, determines locations from which calls will be made 
# locations = [("New York",40.7127837, -74.0059413),("Haiti", 18.5790242, -72.3544683 ),("Seattle", 47.6147628,-122.4759903 ),("Toronto", 43.7181557,-79.5181432 ),("Brazilia",-15.7217175,-48.0783247)]
locations = [("New York",40.7127837, -74.0059413)]

#Set collection variables 
api_key= # API Key here
attributes = 'ghi,dhi,dni,wind_speed_10m_nwp,surface_air_temperature_nwp,solar_zenith_angle,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,fill_flag,surface_pressure_background,surface_relative_humidity_nwp,wind_direction_10m_nwp,total_precipitable_water_nwp'
years = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]	
interval = '30'
utc = 'false'
your_name = # Name here
reason_for_use = 'beta+testing'
your_affiliation = 'Fantastic'
your_email = #Email Here
mailing_list = 'false'

# Function calls for determining length of data collection
start = datetime(1998,1,1)
end = datetime(2015,1,1)
