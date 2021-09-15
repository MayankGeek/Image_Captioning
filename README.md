# Image_Captioning
# Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/MayankGeek/Image_Captioning.git
$ cd Image_Captioning
$ cd Caption_Project

```

Activate virtual environment to install dependencies in and activate it:

```sh
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip3 install -r requirements.txt
```

Once `pip3` has finished downloading the dependencies:
```sh


(venv)$ python3 manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

# Configuration for forgot password feature(To send email to users )
Go to settings.py file under Img_Upload folder:

1. Go to line number 152 & 154 replace 'enter email address' with your gmail address. 
2. Go to line number 153 and replace 'enter your google app password' with your google app password. 

# Steps to generate google app passwords 

1. Go to your google account.

2. Under settings tab click on App passwords under Signing in to Google. (you need to enable 2-step verification in order to make it working)

3. Click the select app drop down and select other(Custom name) and then type Image_Captioning.

4. Click on generate 

5. You will get a 16 digit code in a yellow box copy that code and replace 'enter your google app password' on line 153 with it.

# Project sample images

