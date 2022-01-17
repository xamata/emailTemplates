#!/usr/bin/env bash
# shell script for emailTemplates.command on MacOS
echo '''KeyPhrases:
postInterviewEmail
interviewRequestResponse
sendingResumeEmail
'''
echo "Enter an argument for mclip:"
read ANYTHING 
python3 /Users/maximillianmata/Documents/Programming/Python/Automate-The-Boring-Stuff/Chapter-05/emailTemplates.py $ANYTHING
