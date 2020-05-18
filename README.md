# Sales_Stats

Running the project locally:

  1) clone the git repository
  2) open the project folder in terminal
  3) I have added a requirements.txt file to the root directory
  4) to install the packages and dependencies, run "pip3 install -r requirements.txt" in terminal
      or you might have to run "sudo pip3 install -r requirements.txt"
  5) run "python3 manage.py runserver"
  6) open the defined paths:
        - 'localhost:8000/sales/form'
        - 'localhost:8000/sales/report'
  7) Either create a new superuser to access 'localhost:8000/admin' or use these credentials:
        - username: aggrimarora
        - password: hello@123

Entity-Relationship Diagram

![](/Sales_ERD.jpg)

Features:
  - I used django models to create and setup the database
  - To create the forms:
      * I created the order page using a raw HTML form (url: '/sales/form')
      * I created the report page using django model forms (url: '/sales/report')

Sales Entry Form(Raw HTML)

  - This form has been created by using dynamic templating so any changes in the database will be  reflected in the form   automatically.
  ![](/Sales_Entry.png)

Sales Report Form(Django Model Form)

  ![](/Sales_Report.png)




Aesthetics

* For any form fields that fail validation, have them change color to a light red to clearly indicate which fields contain invalid values.
![](/Invalid_Red_gif.gif)

* Once the form has been successfully submitted and the data saved, please add a clear message on top of the now empty form that the data has been saved. This message should disappear after 5 seconds.
![](/Success_Message_gif.gif)

* Please add a read-only text field at the bottom of the form labeled "Total Price”. This field should dynamically update with the total price of the sale as the cashier chooses the items that make up the sale.
![](/Order_Total_gif.gif)
