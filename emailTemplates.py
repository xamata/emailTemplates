#! python3 
# emailTemplates.py - A multi-clipboard program that copies templates to your clipboard for pasting

emailTemplates = {'postInterviewEmail': """Hi [Interviewer Name],

Thank you so much for meeting with me today. It was such a pleasure to learn more about the team and position, and I’m very excited about the opportunity to join [Company Name] and help [bring in new clients/develop world-class content/anything else awesome you would be doing] with your team.

I look forward to hearing from you about the next steps in the hiring process, and please do not hesitate to contact me if I can provide additional information.

Best regards,
[Your Name]""", \

'interviewRequestResponse': """Dear Ms. Wade,

Thank you for your consideration and the invitation to interview for the Social Media Manager role at XYZ Company. I am available this Wednesday at 1:30 pm, and I look forward to meeting with you to discuss this position in more detail.

Please let me know if I can provide any additional information prior to our meeting on Wednesday afternoon at your offices.

Sincerely,
Jaime Jones""", \

'sendingResumeEmail': """
Subject: ‘Job application’ – Job title, Job ID (if applicable) — Your Name

Dear [Hiring Manager’s Name]

I am very interested in applying for the [position] opportunity at [name of the company]. Please find attached my resume and cover letter for your consideration.

With [x] years of experience in [qualification] I have a verifiable history of [relevant achievements, major success, relevant work experiences]. I believe I would be a strong fit for this position.

Thank you very much for reviewing my application. I look forward to hearing from you regarding next steps.

Yours sincerely, 

[Your name]
[Your job title]
[Email address]
[Phone number]
"""}

import sys, pyperclip
if len(sys.argv) < 2: # there are 2 items in sys.argv: title and arg line
	print('Usage: python3 mclip.py [keyphrase] - copy phrase text\n')
	print('You have these templates to choose from: ')
	for i in emailTemplates:
		print(f'{i}')
	sys.exit()

keyphrase = sys.argv[1] # keyphrase is equal to 1st cmnd line arg

if keyphrase in emailTemplates: 
	pyperclip.copy(emailTemplates[keyphrase])
	print('Text for ' + keyphrase + ' copied to clipboard.')
else:
	print('There is no text for ' + keyphrase)
	