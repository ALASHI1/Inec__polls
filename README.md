# How to run the project
Install a virtual enviroment on your terminal if you dont have one already with

```
python3 -m pip install --user virtualenv
```
Then proceed to create a virtual environment and activate it with 

```
for mac 
    python3 -m venv env
    source env/bin/activate

for windows
    py -m venv env 
    .\env\Scripts\activate
```

To confirm if the above process has been completed you should see the 'env' like this '(env)' on your terminal/cmd

please note that you have to have python installed on your global computer to proceed 

Download the zip file or clone the repo to a folder on your system with
```
git clone https://github.com/ALASHI1/Inec__polls.git
```
After the above processes have been completed proceed to install the requirements necessary for the project
using the command 

```
pip install -r requirements.txt
```

this will take a few moments to install depending on your service provider

After installing confirm that you are in the root directory by pressing the command 'ls' and checking for the 'manage.py' file if you can see that file then you are in the right place 
finally start the server by migrating and then running the runserver command
```
python manage.py migrate
python manage.py runserver
```

IF YOU COME ABOUT A SECRET KEY ERROR RUN
```
for mac
export SECRET_KEY='django-insecure-s*_myt83*82&sy%rknaq#z3+$@0_5&wnh2ephp$_qv*qe4d^@$' MODE=dev DATABASE_URL=msql://ben_shi:bincom@localhost:3306/bincomphptest
for windows
set SECRET_KEY='django-insecure-s*_myt83*82&sy%rknaq#z3+$@0_5&wnh2ephp$_qv*qe4d^@$' MODE=dev DATABASE_URL=msql://ben_shi:bincom@localhost:3306/bincomphptest
```
IF NOT JUST PROCEED TO
```
http://127.0.0.1:8000/
```