#!/usr/bin/env bash
# shell script for emailTemplates.command on MacOS
echo '''KeyPhrases:
postInterviewEmail
interviewRequestResponse
sendingResumeEmail
'''
echo "Enter a KeyPhrase for emailTemplates:"
read ANYTHING 
python3 /Users/maximillianmata/Documents/Programming/Python/Automate-The-Boring-Stuff/Chapter-05/emailTemplates.py $ANYTHING
