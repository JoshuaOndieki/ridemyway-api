"""
    Manage.py | Handles all database migrations
    Usage:
        manage.py
        manage.py migrate <db> <host> <username> <password> [-d | --detached]
        manage.py (-h | --help | --version)
        quit
    Options:
        -d, --detached  Detached Mode
        -h, --help  Show this screen and exit.
"""

import cmd
import os

from psycopg2 import connect
from docopt import docopt, DocoptExit
from termcolor import colored
from prettytable import PrettyTable


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    print(__doc__)


def tables():
    """ Prints tables migrated!
    """
    print()
    print('These tables were migrated')
    print()
    users = PrettyTable()
    username = colored("username", 'blue')
    name = colored("name", 'blue')
    gender = colored("gender", 'blue')
    usertype = colored("usertype", 'blue')
    date_joined = colored("date_joined", 'blue')
    contacts = colored("contacts", 'blue')
    email = colored("email", 'blue')
    password = colored("password", 'blue')
    users.field_names = [username, name, gender, usertype, date_joined,
                         contacts, email, password]
    print(colored('\t\t\t\tUSER TABLE', 'green', attrs=['bold']))
    print(users)
    print()

    rides = PrettyTable()
    ride_id = colored("ride_id", 'blue')
    date_offered = colored("date_offered", 'blue')
    departure = colored("departure", 'blue')
    driver = colored("driver", 'blue')
    cost = colored("cost", 'blue')
    vehicle = colored("vehicle", 'blue')
    status = colored("status", 'blue')
    origin = colored("origin", 'blue')
    destination = colored("destination", 'blue')
    available_capacity = colored("available_capacity", 'blue')
    notes = colored("notes", 'blue')
    rides.field_names = [ride_id, date_offered, driver, departure,
                         cost, vehicle, status, origin, destination,
                         available_capacity, notes]
    print(colored('\t\t\t\tRIDE TABLE', 'green', attrs=['bold']))
    print(rides)
    print()

    requests = PrettyTable()
    request_id = colored('request_id', 'blue')
    ride_id = colored('ride_id', 'blue')
    date_requested = colored("date_requested", 'blue')
    rider = colored("rider", 'blue')
    status = colored("status", 'blue')
    seats = colored("seats", 'blue')
    luggage = colored("luggage", 'blue')
    notes = colored("notes", 'blue')
    requests.field_names = [request_id, ride_id, date_requested, rider, status,
                            seats, luggage, notes]
    print(colored('\t\t\t\tREQUEST TABLE', 'green', attrs=['bold']))
    print(requests)
    print()

    vehicles = PrettyTable()
    number_plate = colored('number_plate', 'blue')
    driver = colored('driver', 'blue')
    model = colored("model", 'blue')
    vehicle_type = colored("vehicle_type", 'blue')
    color = colored("color", 'blue')
    capacity = colored("capacity", 'blue')
    vehicles.field_names = [number_plate, driver, model,
                            vehicle_type, color, capacity]
    print(colored('\t\t\t\tVEHICLE TABLE', 'green', attrs=['bold']))
    print(vehicles)


def migrate(conn):

    """ Migrations are made here!
    """
    cur = conn.cursor()
    with open('schema.sql') as f:
        cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()
    tables()


class Manager(cmd.Cmd):
    """ Migrations Manager
    """
    prompt = 'RIDEMYWAY' + colored('# ', 'magenta', attrs=['blink', 'bold'])

    @docopt_cmd
    def do_migrate(self, arg):
        """ Usage: migrate <db> <host> <username> <password>"""
        print('Migrating..')
        conn = connect('dbname=' + arg['<db>'] +
                       ' host=' + arg['<host>'] +
                       ' user=' + arg['<username>'] +
                       ' password=' + arg['<password>'])
        migrate(conn)

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit """
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Ciao Ciao!')
        exit()


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if not arguments['--detached']:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            intro()
            Manager().cmdloop()
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Ciao Ciao!')
    else:
        conn = connect('dbname=' + arguments['<db>'] +
                       ' host=' + arguments['<host>'] +
                       ' user=' + arguments['<username>'] +
                       ' password=' + arguments['<password>'])
        migrate(conn)
