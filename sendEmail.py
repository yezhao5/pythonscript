# sendEmail.py
# Joanna Xu
# Send grade reports to the students' ucsd emails

import smtplib
from email.mime.text import MIMEText

#Get students' emails
rosterlist = []
rosterf = open('Roster - Sheet1.tsv', 'rU') # student info
for line in rosterf:
	cells = line.rstrip('\n').split('\t')
	if cells[3] == '':
		continue
	if cells[3] == 'not on roster':
		continue
	rosterlist.append((cells[3], cells[2])) # change indices here
roster = dict(rosterlist)
#print (roster)

# Get graders' emails
graderslist = []
gradersf = open('CS8A tutor sheet - Sheet1.tsv' , 'rU') # grader info
for line in gradersf:
	cells = line.rstrip('\n').split('\t')
	graderslist.append((cells[2], cells[1])) # change indices here
graders = dict(graderslist)
#print (graders)

# Read grading sheet and send emails
currcol = 472 #counting graded
for i in range(451, 472):
	currstu = ''
	currgrader = ''
	output = []
	f = open('CSE8A PSA Grading - PA1.tsv' , 'rU', encoding='utf-8') # grading sheet
	for line in f:
		cells = line.rstrip('\n').split('\t')
		output.append((cells[0], cells[i]))
	f.close()

	# build up email content
	content = ''
	for (x,y) in output:
		if x == 'Status':
			continue
		if x == 'Grader':
			#currgrader = 'cs30y' + y
			currgrader = y
			continue
		content += x
		content += ' '
		content += y
		content += '\n'
		if x == 'cs8af Student':
			currstu = y
			content += '\n'
		if x == 'Comments:':
			content += '\n'
	
	#print(graders[currgrader])
	content += '\n======================Please reply to ' + graders[currgrader] + ' for regrade request.========================\n\n'
		
	# get email addresses
	if currstu in roster:
		stuemail = roster[currstu]
		print(stuemail)
	else:
		continue;
	
	graderemail = graders[currgrader]
	print (currgrader)
	#print stuemail
	print (graderemail)
	
	# build up email message object
	msg = MIMEText(content)
	me = 'yezhao@ucsd.edu'
	###### IMPORTANT: Change the following lines if you want to test sending to your own email account #####
	you = stuemail
	cc = graderemail
	
	#you = 'jix073@ucsd.edu'
	#cc = 'yezhao@ucsd.edu'
	msg['Subject'] = 'PSA0 Grade Report'
	msg['From'] = me
	msg['To'] = you
	msg['CC'] = cc

	# send email
	try:
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.ehlo()
		s.starttls()
		s.login('yezhao@ucsd.edu','100308Zy')
		s.sendmail(me, [you] + [cc], msg.as_string())
		s.quit()
		print ("sent")
	except:
		print ("failed to send mail")
