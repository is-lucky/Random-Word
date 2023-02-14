Run the program directly in your browser (open folder location in terminal and type "python [ProgramName].py")
In the terminal a link will be provided to the the location on the browser where the program is now running

To request a random word simply add "get word" to the web address (i.e., http://127.0.0.1:5000/get word) and a random word will be printed to the browser window
To request within another program send GET requests to the same address and the program will receive a random word in string form.
In the example program (sendRecieve.py) this was done by importing the requests library and printing the response as a json object.
![image](https://user-images.githubusercontent.com/91282083/218641581-99ceda97-7501-4e48-ac9b-ea3ed0a301ff.png)
