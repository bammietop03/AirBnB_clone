# AirBnB_clone
Welcome to the AirBnB clone project

<img src="https://miro.medium.com/v2/resize:fit:1358/0*NChTo-XqLOxLabIW" width="1500" height="200">

## Welcome to the AirBnB clone project!

# First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

**Each task is linked and will help you to:**

1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4. create the first abstracted storage engine of the project: File storage.
5. create all unittests to validate all our classes and storage engine

## What’s a command interpreter?

### Processing Commands
The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command
to an appropriate command handler. The command, and any other text on the line. If the user enters a
command ``` all User ```, and your class includes a method named do_all(), it is called with "User" as the only argument.

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

## How to start
1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

## How to use
**In interactive mode:**

	$ ./console.py
	(hbnb) help
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	
	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

**In non-interactive mode: (like the Shell project in C)**

	$ echo "help" | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

**All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash**

## Examples 1
	guilaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) create BaseModel
	49faff9a-6318-451f-87b6-910505c55907
	(hbnb) all BaseModel
	["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
	(hbnb) destroy
	** class name missing **
	(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	(hbnb) create BaseModel
	2dd6ef5c-467c-4f82-9521-a772ea7d84e9
	(hbnb) all BaseModel
	["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
	(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	** no instance found **
	(hbnb)

## Example 2
	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.count()
	2
	(hbnb)

## Example 3
	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
	[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
	(hbnb) User.show("Bar")
	** no instance found **
	(hbnb)

## Example 4
	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) User.count()
	2
	(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
	(hbnb) User.count()
	1
	(hbnb) User.destroy("Bar")
	** no instance found **
	(hbnb)

## Unittests Example
	guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
	...................................................................................
	...................................................................................
	.......................
	----------------------------------------------------------------------
	Ran 189 tests in 13.135s
	
	OK
	guillaume@ubuntu:~/AirBnB$  
or

	guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
	...................................................................................
	...................................................................................
	.......................
	----------------------------------------------------------------------
	Ran 189 tests in 13.135s
	
	OK
	guillaume@ubuntu:~/AirBnB$
