# AirBnB_clone Project
ALX Project on Creating an AirBnB clone 

## Description of the project
    This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.
   
## Description of the command interpreter:
   - how to start it 
   - how to use it 
   - how to store, update retrieve and destroy data
   - examples 
   
##First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

##Each task is linked and will help you to:
   -put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
   -create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
   -create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
   -create the first abstracted storage engine of the project: File storage.
   -create all unittests to validate all our classes and storage engine.


    classes are handled by the abstracted storage engine defined in the FileStorage class.

    Every time the backend is initialized, AirBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class     instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

##Console 💻
The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

##Using the Console
The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

##Example

guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests

...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------

Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$

