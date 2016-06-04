import urllib
from BeautifulSoup import *

beg = int(raw_input("Enter starting regno"))
end = int(raw_input("Enter ending regno"))
print "ENGINEERING MATHEMATICS-IV\nSYSTEM PROGRAMMING\nSOFTWARE ENGINEERING\nCOMPUTER GRAPHICS\nDATABASE MANAGEMENT SYSTEMS\nMICROPROCESSOR BASED SYSTEM DESIGN\nMICROPROCESSOR LABORATORY\nCOMPUTER GRAPHICS LABORATORY"
subj = raw_input("Enter Subject")
#parameters to be passed in the url
param = {
	'regno' : 12140600,
	'deg_name' : 'B.Tech',
	'semester' : 5,
	'month' : 'November',
	'year' : 2015,
	'result_type': 'Regular',

}
for i in range(beg, end + 1):
	param['regno'] = i
	flag = 0
	dflag = 0
	mainurl='http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result?'
	url = mainurl + urllib.urlencode(param)
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('td')
	for tag in tags:
		if tag.contents[0] == str(i):
			dflag = 1
			continue
		if dflag == 1:
			print tag.contents[0]
			dflag = 0
			continue
		if tag.contents[0] == subj.strip():
			flag = 1
			continue
		if flag == 1:
			print tag.contents[0].strip()
			flag = 2
			continue
		if flag == 2:
			print tag.contents[0].strip()
			print "\n"
			flag = 0
