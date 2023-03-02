## Project: Music Culture Project

This project is a test project. It is mainly used to learn the flask framework and some front-end knowledge.

It is not suitable for production environments because it lacks some security guarantees, such as csrf, xss, and so on.

Another reason for developing it is to explore the relationship between the data and deeply understand the relationship between the musician and his song style in the social background at that time.

## How to start it
+ First of all, you need to create a virtual environment venv. Here I use virtualenv, which is executed from the command line
  
    ```shell
    virtualenv venv
    source venv/bin/activate  # Activate virtual environment,windows: venv\Scripts\activate
    ```

+ then install the dependent package
      
     ```shell
     pip install -r requirements.txt
     ```
+ Initialize database data
    ```shell
    python setup_db.py
    ```
+ Run Project
    ```shell
    flask run
    ```
+ Browser access http://127.0.0.1:5000


## How to test it
First of all, you need to determine your browser and version. I'm using Chrome 109. If your version is different, there may be some problems.
Here is the download connection，http://chromedriver.storage.googleapis.com/index.html
+ Download the corresponding version of chromedriver，Then put it in the project directory `features/driver/`
+ Then execute
    ```shell
    behave
    ```
+ If you see the following output, congratulations, you have successfully tested this project
    ```shell
    ----------------------------------------
    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    3 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.281s
    ```

## Installation
Clone or download the project code:

```shell
git clone https://github.com/your_username/app.git
```

Enter the project directory:

```shell
cd app
```

To create and activate a Python virtual environment:

```shell
python3 -m venv .venv
source .venv/bin/activate

```
Python dependencies required to install the project:

```shell
pip install -r requirements.txt
Initialize and import data
python3 arse_csv.py
```

Run the application (take the codio run as an example)

```shell
export FLASK_APP=app.py
python3 -m flask run -h 0.0.0.0
```



Visit the following URL in your Web browser to view the application:

```shell
http://localhost:5000/
```



## USE
1. The page displays a list of applications. You can click the Details button to see the details of your application.
2. On the application list page, you can use the paging control to browse applications on different pages.


## Which libraries and plug-ins are used
```text
1. flask: python website application framework
2. jinjia2: template engine
3. sqlite3: connect and query the database
4. selenium: automated test tools
5. behave: BDD test framework
6. flask g: manage global variables

```
