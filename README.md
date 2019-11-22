# dollar_auction
Simple server hosting dollar auction in local network

## Instalation
1. Download repository code
2. Run `python dollar_auction` in **folder containing repository folder**
3. Visit 127.0.0.1:8008 in your web browser. First user to join the website becomes the admin.
4. Set up game options
5. Check host address in local network (Win: `ipconfig`, Linux: `ifconfig -a`). 
Other players have to join it.
6. Start the game once everybody is in!

## Technology stack

dollar_auction utilises:
- *Python 3* as language, 
- *Flask* as server engine 
- *Jinja 2* as User Interface html generator. 
([documentation here](https://buildmedia.readthedocs.org/media/pdf/jinja2/stable/jinja2.pdf))

## Known issues

- Flask server does not understand HTTPS connections 
and raises ValueError when machine tries to connect via https://domain.example address. 
Please remember to change the address to http.

[issue update]: added false certificate to sign 
during https connections. Web browser will raise 
a warning that shall be ignored.
