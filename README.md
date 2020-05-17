# Sales_Stats

![](/Sales_ERD.jpg)

Features:
  - I used django models to create and setup the database
  - To create the forms:
      * I created the order page using a raw HTML form (url: '/sales/form')
      * I created the report page using django model forms (url: '/sales/report')
  - I have also added the models to the admin system
      * To use this application, clone it, install required dependencies and here are the credentials for the admin system:
          username: aggrimarora
          password: hello@123

Sales Entry Form(Raw HTML)

![](/Sales_Entry.png)

Sales Report Form(Django Model Form)

![](/Sales_Report.png)

Aesthetics

* For any form fields that fail validation, have them change color to a light red to clearly indicate which fields contain invalid values.
![](/Invalid_Red_gif.gif)

* Once the form has been successfully submitted and the data saved, please add a clear message on top of the now empty form that the data has been saved. This message should disappear after 5 seconds.
![](/Success_Message_gif.gif)

*Please add a read-only text field at the bottom of the form labeled "Total Price”. This field should dynamically update with the total price of the sale as the cashier chooses the items that make up the sale.
![](/Order_Total_gif.gif)

