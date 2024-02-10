# Airbnb Command Line Interface (CLI)

## Description
    This project is a Command Line Interface (CLI) for managing Airbnb listings.
    It provides functionalities to interact with Airbnb listings through the command line,
    enabling users to search for properties, book accommodations,
    manage reservations, and more

## Command Interpreter
    The Airbnb Command Interpreter is a Python-based tool
    that allows users to interact with Airbnb listings using a command-line
    interface. It is designed to provide a seamless experience for searching,
    booking, and managing Airbnb properties directly from the terminal
## How to Start
    To start the Airbnb Command Interpreter, follow these steps:

    1. Clone this repository to your local machine.
    2. Navigate to the project directory.
    3. Run the command `python airbnb_cli.py` to start the command interpreter.
## How to Use
    Once the command interpreter is running,
    you can use various commands to interact with Airbnb listings.
    Here are some of the basic commands:

- `search <location>`: Search for Airbnb listings in the specified location.
- `book <listing_id> <check-in_date> <check-out_date>`: Book a listing with 
the specified ID for the given check-in and check-out dates.
- `cancel <reservation_id>`: Cancel a reservation with the specified ID.
- `list_reservations`:  List all reservations associated with your account.
- `help`: Display a list of available commands and their usage instructions.
- `exit` or `quit`: Exit the command interpreter.
## examples 
    
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```    
```
(hbnb) create BaseModel
7fa29982-fe32-4dcc-aca5-35a4a249a517
```
```
(hbnb) all
["[BaseModel] (7fa29982-fe32-4dcc-aca5-35a4a249a517) {'id': '7fa29982-fe32-4dcc-aca5-35a4a249a517',
 'created_at': datetime.datetime(2024, 2, 11, 0, 37, 56, 34761),
 'updated_at': datetime.datetime(2024, 2, 11, 0, 37, 56, 35762)}"]
```
```
(hbnb) show BaseModel 7fa29982-fe32-4dcc-aca5-35a4a249a517
[BaseModel] (7fa29982-fe32-4dcc-aca5-35a4a249a517) {
'id': '7fa29982-fe32-4dcc-aca5-35a4a249a517', 
'created_at': datetime.datetime(2024, 2, 11, 0, 37, 56, 34761), 
'updated_at': datetime.datetime(2024, 2, 11, 0, 37, 56, 35762)}
```
```
(hbnb) update BaseModel 7fa29982-fe32-4dcc-aca5-35a4a249a517 first_name "jhin"
(hbnb) show BaseModel 7fa29982-fe32-4dcc-aca5-35a4a249a517
[BaseModel] (7fa29982-fe32-4dcc-aca5-35a4a249a517) {
 'id': '7fa29982-fe32-4dcc-aca5-35a4a249a517',
 'created_at': datetime.datetime(2024, 2, 11, 0, 37, 56, 34761),
 'updated_at': datetime.datetime(2024, 2, 11, 0, 42, 9, 309604), 
 'first_name': 'jhin'}
```
```
(hbnb) destroy BaseModel 7fa29982-fe32-4dcc-aca5-35a4a249a517
(hbnb) show BaseModel 7fa29982-fe32-4dcc-aca5-35a4a249a517
** no instance found **
```
```
(hbnb) quit {you closed the project}
(hbnh) EOF {you closed the project}
```