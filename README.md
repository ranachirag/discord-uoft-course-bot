# Discord UofT Bot

A Discord bot that gives information about courses at the University of Toronto.

## Description

Using data scraped off the University of Toronto's course finder website, the following Discord bot gives a detailed overview of the courses availabe during the 2020-2021 year using simple Discord commands. 

## Getting Started

### Dependencies

* discord.py
* python-dotenv
* requests
* beautifulsoup4

### Installing

* Clone the repository into a local directory.
* [Create a Discord Server.](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)
* [Create a Discord bot and add it to the Discord server.](https://discordpy.readthedocs.io/en/latest/discord.html)
* Take the Token generated by the bot and copy it.
* Create an ```.env``` file in the local directory.
* Add the following to ```.env```:
```
DISCORD_TOKEN={token_key_you_copied}
DISCORD_GUILD={name_of_your_server}
```

### Executing program

* Run ```bot.py``` to get the connection to Discord running.

## Help

Use the ```!help``` command to see the list of available commands and their uses.

## Authors

* Chirag Rana  
* Gabriel Chow

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

* [Tutorial followed to setup the bot](https://realpython.com/how-to-make-a-discord-bot-python/)