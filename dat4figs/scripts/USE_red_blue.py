#!~/bin/python
###########################################################################
###########################################################################
## Python script to make money-plot for ASASSN SN matched to ATLAS data	 ##
## Corey Mutnik - 161121												 ##
##   pulled desired portions form 'decVSmjd.py'							 ##
##   have chosen to not use color to represent magnitude				 ##
##   this plot desired point across better								 ##
###########################################################################
###########################################################################

import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from astropy.io import ascii
import matplotlib.cm as cm
#import matplotlib.colors
import numpy as np
dfile = ascii.read('../rematch_assasn.full385.txt')
mjd,dec = dfile['col1'],dfile['col3']
mag = dfile['col5'] 
s = 2**mag/200
age = dfile['col6']
peaking = mjd - age
newdat=ascii.read('../asas.snmch.awked')
newmjd,newdec,newmag,newage = newdat['col1'],newdat['col3'],newdat['col5'],newdat['col6']
newpeaking = newmjd - newage
s_fixed = 200000./s
news_fixed = news = 200000. / (2**newmag/200)


def plot2useinPaper():
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)
	plt.ylabel('Declination')
	plt.xlabel('Peak Brightness MJD')
	plt.ylim(-90,90)
	plt.xlim(56400,57800)#56410,57700
	rect_off_dec = matplotlib.patches.Rectangle((56400,-90), 1400, 60, color='black', alpha=0.5, lw=0)
	rect_off_mjd_b4_atlas = matplotlib.patches.Rectangle((56400,-30), 792, 120, color='black', alpha=0.5, lw=0)
	rect_off_mjd_bad_diff = matplotlib.patches.Rectangle((57192,-30), 145, 120, color='black', alpha=0.25, lw=0)
	ax.add_patch(rect_off_dec)
	ax.add_patch(rect_off_mjd_b4_atlas)
	ax.add_patch(rect_off_mjd_bad_diff)
	xtickvals=[56400,56600,56800,57000,57200,57400,57600,57800]# evens
	#ytickvals = [90-(m*20) for m in range(10)]# = [-90,-70,-50,-30,-10,10,30,50,70,90]
	ytickvals = [80-(m*20) for m in range(9)]
	ax.set_xticks(xtickvals)
	ax.set_xticklabels([str(n) for n in xtickvals])
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
	ax.set_yticks(ytickvals)
	ax.set_yticklabels([str(n) for n in ytickvals])
	plt.scatter(peaking,dec,s=s_fixed, marker='o', c='red')
	plt.scatter(newpeaking,newdec,s=news_fixed, marker='o', c='blue')
	#plt.savefig('plot2useinPaper.png')
	plt.show()
plot2useinPaper()