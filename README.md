You need an api key from the website https://console.groq.com/login they are free
THE API KEYS ONLY SHOW ONCE SO SAVE IT SOMEWHERE!
repalce the text on line 6 of the 
run -> pip install groq (in your terminal)
once you have the file get the directory path with the command pwd save the full path including the file name
run this command in your terminal "nano ~/.bashrc" (w/o "s)
choose a variable_name for your file ie AI
add this line to the bashrc file at the bottom export vairable_name="full path to the pyhton file"
then call $variable_name from anywhere in your terminal (note this should work in your terminal in VS code as well)
