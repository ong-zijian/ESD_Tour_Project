# ESD Merlion Tour Project

Merlion Tours is a web platform that operates on a Microservice-oriented architecture. This enterprise solution aims to connect prospective tourists with tour guides. 

The project uses a local MySQL database with the source file attached to the `SQL_Scripts` folder. The file is called `tourDBdata.sql`. 

## To import the file:
    1. Start up wamp server
    2. Go to localhost 
    3. Select phpmyadmin
    4. On the tabs above, select import
    5. Select the add button and attach the <folder> and click go
    6. Check that the import is done properly by finding the database on the left side menu.
    7. You should see "tourdb" imported with 4 number of tables

### Troubleshoot:

### Before starting the service:
- Mac users should check their root account if a password is required. If password is required, use `root:<your Wamp password` in the urls for `.env` and `docker-compose.yml`
- If any of the files give you any issues like npm modules not installed, run `npm install` to install all the dependencies. 

## Running the microservices:
- The microservices are running on docker-compose containerised. 
- To start, make the changes to the `docker-compose.yml` file:
    1. change all the image from <our docker id>/ESDtour... to <your docker id>/ESDtour....
    2. check the MySQL port to be your port
    3. check your WAMP root access or user `is213` access. If the access is not set, use <insert lab instruction on setting is213 user>



## Frontend:
The frontend is a simple Vue.js cli frontend. To start the frontend, it is as simple as starting up the Vue local server. 

1. Run `npm run serve` to start up the Vue.js frontend.
2. If it doesn't work, you can follow the Vue troubleshoot:
    - Ctrl + c to stop vue services
    - Run `npm run build` to build the local Web application 
    - Start up Vue again using `npm run serve`
    


## Packages
The projects uses some packages and libraries to make it work. In the event that `npm install` and the `requirements.txt` failed to install everything, here is a list of commands to install the other packages beyond the lab.

pip install python-dotenv
python -m pip install requests
python -m pip install request
python -m pip install pyTelegramBotAPI
python -m pip install -U Werkzeug

### esd_project_template

### First, run the following statements in your
### terminal to install the following python packages

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Encodes DateTimes into a numeric format
```
npm install moment from 'moment'
```

### Stripe API support
npm install stripe

### Kong API Gateway and Konga setup

### Konga

1. Access http://localhost:1337 in a browser to create an admin user for Konga
Username: 	admin
Email: 	    <your email address>
Password: 	adminadmin

2. Sign in

3. Connect Konga to Kong by creating a new connection
Name: default
Kong Admin URL: http://kong:8001

### Kong

4. Add a new service
Name: 	tourapi
Url: 	http://tour.v1.service:5002
Leave the defaults for the rest
Then, click “SUBMIT SERVICE” button at the end of the page.

5. Click on the “bookapi” service, then the Routes tab.

6. Add a new route.
Paths: 	/api/v1/tour
(ensure no space before or after; MUST press “Enter”) 
Methods: 	GET (MUST press “Enter”)
Then, click “SUBMIT ROUTE” button at the end of the page.	

7.	Open the UPSTREAMS page

8. Create an upstream (a virtual hostname)
Name: tour.v1.service
Then, click “SUBMIT UPSTREAM” button at the end of the page.

9. Click DETAILS, then the Targets tab

10. Add a target
Target: tour-service-1:5002
Then, click “SUBMIT TARGET”  button.

11. Add another target 
Target: tour-service-1:5003
Then, click “SUBMIT TARGET” button.
