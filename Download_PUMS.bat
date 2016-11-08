FOR %%A IN (2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014) DO (
    mkdir %%A
	cd %%A
	wget http://www2.census.gov/programs-surveys/acs/data/pums/%%A/csv_hal.zip
	wget http://www2.census.gov/programs-surveys/acs/data/pums/%%A/csv_hmo.zip
	wget http://www2.census.gov/programs-surveys/acs/data/pums/%%A/csv_hny.zip
	wget http://www2.census.gov/programs-surveys/acs/data/pums/%%A/csv_pal.zip
	wget http://www2.census.gov/programs-surveys/acs/data/pums/%%A/csv_pmo.zip
	wget http://www2.census.gov/programs-surveys/acs/data/pums/%%A/csv_pny.zip
	cd ..)