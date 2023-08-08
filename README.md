# ML experiment system

 Construct and reuse machine learning models

![](https://img.shields.io/badge/dependencies-Python_3.8-blue)
![](https://img.shields.io/badge/dependencies-Django_3.2-green)

## Acknowledgement

Pandas profiling: https://github.com/pandas-profiling/pandas-profiling

## Deployment

The current folder of command line is the software's project root.

**Build token files.**

1. Create `token` folder at project root.

2. Create `token/django_secret_key` and input 52 random characters.

3. Create `token/smtp.json` and configure the web maintainer's email sender as the following format.

    ```json
    {
    "host": "example.com",
    "port": 465,
    "username": "registration@example.com",
    "password": "anypassword"
    }
    ```

**Payment with PayPal.**

*Applicable only when the module `paypal`, `paypalhttp`, and `paypalcheckoutsdk` exist.*

1. Create `token/paypal.json` and configure the password as the following format.

    ```json
    {
    "client_id": "anypassword",
    "secret": "anypassword"
    }
    ```

2. If used in real business, replace `paypal/models.py -> PaypalClient class -> SandboxEnvironment` with `LiveEnvironment`. Also, use live environment's client ID and secret in `token/paypal.json`.

**Build the environment.**

*It is a complete environment. With the environment, all functions can be used, but not all functions are necessary.*

1. Run the following command.

    ```
    pip install -r requirements.txt
    ```

**Create the database.**

1. Navigate to the project folder.
2. Create the database and super user.

    ```
    python manage.py migrate
    python manage.py createsuperuser
    ```

3. Follow the instructions in the command line. This user has the highest permission in this software.

## Administration

**Start running the website.**

1. Run the following command.

    ```
    python manage.py 0.0.0.0:$port --insecure
    ```

    The IP address can only be 127.0.0.1 (for local use only) or 0.0.0.0 (for web server), and `port` can be customized.

2. Visit `https://example.com:$port/admin`. Create at least one group. Add the groups, which users can freely add into, to "Register groups" table. These groups each must include the following permissions:

   - Library: add, delete, change, view papers

   - My login: add, change, view register

   - Paypal: view plans; add, delete, change, view subscription; add, change, view transaction

   - Task manager: add, delete, change, view openedtask; add, delete, change, view step; add, delete, change, view task


3. Add charged functions to some new groups, and bound them to plans. Add all groups that contains charged functions to "Locked groups" table. Every time when users login, the software will remove them from all locked groups, and then add them back according to effective subscriptions.

**Limit storage space.**

1. Set group storages for each group, which represents the storage each user in this group can use. 
