# Telegram Base Bot
This repo containts code for building a base telegram bot. Furthermore, on top of the base bot, you can add your own customization accordingly.

> **Detailed blog for the base bot and steps for hosting the same on Heroku can be found [HERE](https://bijawesanket.medium.com/building-your-first-telegram-bot-cca7490ef60e).**

## Installation Details
All the required modules are listed under requirements.txt. Run the following command to install the same:
```
C:\> pip install -r requirements.txt
```

## Essential Requirements
Create a new telegram chatbot using [BotFather](https://core.telegram.org/bots#6-botfather).

Then, create a ```.env``` file and add following variables
```
API_KEY = "here goes your access token from BotFather"
BOT_USER_NAME = "the username you entered"
URL = "the hosting link that we will create later"
```

## Base Bot Details
```app.py``` contains the complete code for base bot built using ```Flask```. Additionally, we've used **webhook** which provides us a way of letting the bot call our server whenever a message is called, so that we don’t need to make our server suffer in a while loop waiting for a message to come.

## LocalHost Deployment Details
Telegram can’t communicate with the localhost directly and hence we’ll need a public URL to communicate with the bot. Here, we’ll be using ngrok tunneling. ngrok is a free tool that allows us to tunnel from a public URL to our application running locally. You can download ngrok from [here](https://ngrok.com/download).
Activate the ngrok tunnel using following command:
```
C:\> ngrok http 5000
```
Copy the https URL tunneled to localhost to the URL variable of ```.env``` file and Make sure you append ```/``` at the end of URL.

Now run the ```app.py``` file. Then copy the ngrok URL and add to the end of the link ```/setwebhook``` so that the address will be something like ```https://<ngrok code>.ngrok.io/setwebhook```. If you see ```GET /set_webhook 200 OK``` on ngrok’s terminal, that means you are ready to go!

## Go talk to your BOT!
![Sample Chat](https://github.com/San-B-09/Telegram-Bot-Base/blob/6f25db6308fbfbfa5a2524bae8249f02302f2426/README%20Images/Sample%20Chat.gif)
