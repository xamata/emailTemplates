# emailTemplates
There are two files included on this repo, the python file and the bat file. 
You may edit the emailTemplates.bat file to link to your emailTemplates.py file so that you can use windows Run feature to copy the templates more efficiently.

How to use emailTemplates.bat file to streamline the multi-lipboard program:
1. Download both the emailTemplates.bat and emailTemplates.py files.
2. Open the emailTemplates.bat file using a python text editor (I use Sublime Text)
3. Edit the emailTemplates.bat file's directory to link to your emailTemplates.py file. The directory is located on line 1 of the .bat file.
4. Create a PATH to your emailTemplates.bat file by going to Window's Settings and searching 'Edit Enviornment variables for your account'
5. Under 'User variables for [USERNAME]', click on Path->Edit 
6. Create a New Path to your directory where your emailTemplates.bat file is located(it is suggested to keep all of your .bat files in one folder)
7. Click OK and now you have created a path directly to your .bat file 
8. Open 'Run' app and type 'emailTemplates [KEYPHRASE]', if you want to see the list of keyphrases, simply type 'emailTemplates' into the 'Run' app
9. The template has now been copied to your clipboard, you may now paste it anywhere you want
