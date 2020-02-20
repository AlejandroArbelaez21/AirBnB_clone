# AirBnB clone - The console
### Medellin 2019

## What is "AirBnB clone"
our version of the AirBnB web page, where the guest can reserve different rooms offered. This first part of the project consist on making a console
capable of creating new objects with its attributes.

### Console

/** *AirBnB console- our version of console command interpreter* */

To initialize the console just run ./console.py

There type an executable command and press enter, the console should execute the command successfully.

### Description

This Console was created by Alejando Arbelaez and Tomas Mejia, students at Holberton school. the console is a command processor that runs in a text window, allowing the user to type commands. The idea is to let the user replicate some of the same functions the airbnb web page has. This project was completed as a part of the curriculum for Holberton School.

### Requirements

This was made it for running in a ```Ubuntu 14.04 LTS``` Linux enviroment.

### Installation

 - Clone the repository
 - Change directories into the repository
 - Run the shell in interactive mode with ```./console.py```

### Usage
After excecuting the console a prompt will apear, there you can procede to write the different features mentioned below. The way to write a command goes like this:
```bash
(hbnb) [WRITE COMMANDS]
```
Press enter

### Special Features to execute
 -Create a new object (ex: a new User or a new Place
 - Retrieve an object from a file, a database etc
 - Do operations on objects (count, compute stats, etc)
 - Update attributes of an object
 - Destroy an object
 - quit: Use this to exit properly from the console

### Example

This happens when you run the command ```all``` after running this in the console:

The console retrieve and prints all objects previously created and stored in a json file.

```bash
(hbnb) all
["[BaseModel] (6570024a-9ad3-447f-89e0-5e163fa5085c) {'id': '6570024a-9ad3-447f-89e0-5e163fa5085c', 'name': 'Holberton', 'updated_at': datetime.datetime(2020, 2, 19, 19, 26, 45, 205348), 'my_number': 89, 'created_at': datetime.datetime(2020, 2, 19, 19, 26, 45, 205216)}", "[Amenity] (b435c30a-fdef-4fba-8df6-dbd0b240cc97) {'created_at': datetime.datetime(2020, 2, 19, 10, 20, 54, 12753), 'updated_at': datetime.datetime(2020, 2, 19, 10, 20, 54, 12669), 'id': 'b435c30a-fdef-4fba-8df6-dbd0b240cc97'}", "[City] (a04dbd88-179b-4be4-8125-df08242c91f4) {'created_at': datetime.datetime(2020, 2, 19, 10, 47, 4, 535639), 'updated_at': datetime.datetime(2020, 2, 19, 10, 47, 4, 535558), 'id': 'a04dbd88-179b-4be4-8125-df08242c91f4'}"]
(hbnb)
```

### Bugs

Bugs are unknown for this shell.

### Authors

Tomás Mejía | [Github](https://github.com/towasme/) | [Twitter](https://twitter.com/towasme)

Alejandro Arbelaez | [Github](https://github.com/AlejandroArbelaez21) 

### License

This project has no license. Just copy and enjoy.
