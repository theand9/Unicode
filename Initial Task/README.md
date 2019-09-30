# UNICODE BACKEND PYTHON-DJANGO ASSIGNMENT

**This Assignment has been completed in Django which is one of Python's Web Framework.**

The assignment had a total of four tasks out of which the first two were compulsory the next two were optional. Three of the four tasks have been completed by me.

### Task 1:
Create a function that will use ​SpaceX API​ to fetch all ​SpaceX​ Launches. If the Launch has non-empty mission ID array then fetch all the mission data as well. The ​response​ should consist of:
- The flight number
- The manufacturers of the mission
- The launch date in a pretty format. You will have to parse the string date to Date object.  <br />
***Dependencies:***
- *Libraries:*  <br /> a) DateTime  <br />
             b) Requests  <br />
             c) Json  <br />
- *Frameworks:* None  <br />
- *Files Created:* BasicAPIFetch.py  <br />

***Result:*** Displayed the required formatted data on the Command Prompt when the script was executed

### Task 2:
You should implement the above function using ​Django views​ and give the output using HTTPResponse​.  <br />
***Dependencies:***
- *Libraries:*  <br /> a) DateTime  <br />
             b) Requests  <br />
             c) Json  <br />
             d) HttpResponse  <br />
- *Frameworks:* Django  <br />
- *Files Created:* a) Basic Django Project  <br />
                 b) New Django Application  <br />
                 c) urls.py  <br />
                 d) apps.py  <br />

***Result:*** Retrieved the data from the SpaceX API formatted it as done in Task 1 and displayed it on a Django View with url /task2.

### (BONUS)Task 3:
Get the response from the above view function and display it on the webpage. You should use django template to do this.
***Dependencies:***
- *Libraries:*  <br /> a) DateTime  <br />
             b) Requests  <br />
             c) Json  <br />
             d) HttpResponse  <br />
             e) Render  <br />
- *Frameworks:* Django  <br />
- *Files Created:* task3.html(Template)  <br />

***Result:*** Organized and beautified the data by displaying it in a tablar format on a HTML template. URL /task3.

### (BONUS)Task 4:
Not Attempted.

-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
