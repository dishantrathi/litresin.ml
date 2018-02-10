# Litresin.ml ⚡️ URL Shortening Django Powered 💡 Web Application

[Dishant Rathi](https://www.dishantrathi.tk)  [@techiedishant](https://www.twitter.com/techiedishant)

A python-django powered web application whch can shorten long url's in seconds, designed on Bootstrap 4.


## Getting Started 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

    ```
    git clone https://github.com/dishantrathi/litresin.ml.git
    ```


### Prerequisites

* [Python v3.6](https://www.python.org/) - As Base


### Setting up the machine (Windows Machine)

1. Creating Virtual Environment
    ```
    cd litresin.ml
    virtualenv .
    ```

2. Activating Virtual Environment
    ```
    .\Scripts\activate
    ```

3. [Requirements.txt](Requirements.txt) : installing requirements.txt using pip command.
    ```
    pip install -r requirements.txt
    ```

4. Editing the Host File [Linux - Mac - Windows](https://support.rackspace.com/how-to/modify-your-hosts-file/)

    ```
    sudo nano /etc/hosts/

    # insert 
    127.0.0.1     litresin.ml
    127.0.0.1     www.litresin.ml
    ```


## Running

To run the program, simply execute

* For Windows
    ```
    cd src
    py manage.py runserver
    ```
* For Linux
    ```
    cd src
    python3 manage.py runserver
    ```

### URL : 
    ```
    http://www.litresin.ml:8000/
    ```


## Help Section

* Admin Login Url
    ```
    http://litresin.ml:8000/admin
    ```
* Admin Login
    -   Username : localhost
    -   Password : localhost


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.