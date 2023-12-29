# 0x04. AirBnB clone - Web framework


Web framework is a software that is designed to streamline the development process of web applications. It provides a structured way to build and organize code for building web-based software.One such framework covered in this folder is flask. Python flask is a lightweight and flexible web framework with the right tools to build web applications quickly and efficiently.
The tasks below orchestrates the process of building a web app using python flask framework.


## Task 0: Hello Flask!

Files:
	- 0-hello_route.py, __init__.py

Script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
	-  /: display “Hello HBNB!”
* You must use the option strict_slashes=False in your route definition



## Task 1: HBNB

File:
	- 1-hbnb_route.py

Script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
* You must use the option strict_slashes=False in your route definition



## Task 2: C is fun!

File:
	- 2-c_route.py

Script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
* You must use the option strict_slashes=False in your route definition



## Task 3: Python is cool!

File:
	- 3-python_route.py

A script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	* The default value of text is “is cool”
* You must use the option strict_slashes=False in your route definition



## Task 4: Is it a number?

File:
	- 4-number_route.py

A script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
* You must use the option strict_slashes=False in your route definition



## Task 5:Number template

File:
	- 5-number_template.py, templates/5-number.html

A script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	* The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
	- /number_template/<n>: display a HTML page only if n is an integer:
	* H1 tag: “Number: n” inside the tag BODY
* You must use the option strict_slashes=False in your route definition
