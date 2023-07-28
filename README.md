# AI Solutions

### Description

This project contains functionality for interacting with AI models.

##### Models Include
- gpt-3.5-turbo
- blip-2

### usage

To run the app you need to ru the server and the front end.

##### front end setup

1. Open the 'vue' directory in a terminal
```bash
$ cd vue
```
2. install dependencies 
```bash
$ npm install
```
3. Start the development server
```bash
$ quasar dev
```
##### server setup
1. Create a virtual environment
```bash
$ python3 -m venv venv
```
2. Start the virtual environment
- Windows
```
$ venv\Scripts\activate
```
- mac os and linux
```bash
$ source venv/bin/activate
```
3. Install all dependencies
```bash
$ pip3 install -r requirements.txt
```
4. Start the server
```bash
$ python3 main.py
```
note: this step can take up to several minutes on the first time.

That sould be it. Once the server is up and running, the web app sould work great!

If you ever need to update the list of dependencies you can use this command
```bash
$ pip3 freeze > requirements.txt 
```
To exit the virtual environment use this command
```bash
$ deactivate
```