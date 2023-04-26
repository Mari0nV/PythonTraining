## Exercise 1

Write a function that takes into parameters a dictionary and a string. The string will be under the form "key1.key2.key3...".
This function will return the value associated to the key passed in parameters if it exists, and raise an exception otherwise.

Example :
```
mydict = {
  "a": {
      "b": 33
    }
}
get_value(mydict, "a.b")  # will return 33
```

## Exercise 2

Write a function that receive a list of serial numbers.

A correct serial number is defined as below:
- There can only be letters and numbers (no special characters)
- Numbers must be strictly consecutive, either increasing or decreasing.
- Letters must be in the alphabetical order (but not necessarily consecutive).

For exemple, correct serial numbers are :
```
a2c3fgh4m56n, 123abd4, 8765, avz
```

Incorrect ones:
```
a2c3fgh5, 123azd4, zva
```

Your function must return a string containing all correct serial numbers separated by the symbol "_".
Example:
```
a2c3fgh4m56n_123abd4_8765_avz
```
Incorrect serial numbers will be ignored.

## Exercise 3

You receive a string encoded in base64. You know that once decoded, this string has the following format :

```
machine<id>?:<name>@<vendor>?:<password>@<year>
```

where *id* and *year* are integers, *name* and *vendor* are alphanumerical strings, and *password* is a string that can contain alphanumerical values, integers or the following special characters: ```.?@!:```.

Write a function that can decode the encoded string and return the password.

You can test your function with the following inputs :

```
bWFjaGluZTE/OmJvYkBtYW1hem9uPzpzaW1wbGVwYXNzd29yZDFAMjAzMg==    # should output simplepassword1
bWFjaGluZTI/OmFsaWNlQGFsaWJvdWJvdT86cFJmP2dsMTJATUAyMDMy    # should output pRf?gl12@M
bWFjaGluZTM/Om1hcnRpbkBzbmFjPzptZHA/OmJiOEAyMDMz    # should output mdp?:bb8
bWFjaGluZTQ/OmVsb0BkYXJweT86QGM/NEBAZ3JyPzpAMjAzMw==    # should output @c?4@@grr?:
```

## Exercise 4

You work for a company that sells products in multiple cities around the world. You have a CSV file containing sales data for these products in each city over the past few months. Your task is to analyze this data and produce a report on the company's performance in each city.

The CSV file contains the following columns:

- City: the name of the city where the products were sold.
- Month: the month in which the products were sold (in YYYY-MM format).
- Product: the name of the product sold.
- Quantity: the quantity of the product sold.
- Unit Price: the unit price of the product.

You need to write a function ```analyze_sales(csv_file: str) -> dict``` that takes the path to the CSV file as input and returns a dictionary containing the following statistics for each city:

- The total number of products sold.
- The total revenue (sum of the unit prices multiplied by the quantity sold).
- The month with the highest sales (by revenue).

The dictionary should have the city as the key and the statistics as the value, in the form of a dictionary with the keys "total_quantity", "total_revenue", and "month_max".

Example : 
```py 
{
    "Paris": {
        "total_quantity": 250,
        "total_revenue": 5000.0,
        "month_max": "2022-02"
    },
    "New York": {
        "total_quantity": 350,
        "total_revenue": 8750.0,
        "month_max": "2022-03"
    }
}
```

You can create a CSV containing these lines to test your function:
```
City,Month,Product,Quantity,Unit Price
Paris,2022-01,Widget A,100,20.00
Paris,2022-02,Widget A,50,20.00
Paris,2022-02,Widget B,50,25.00
New York,2022-02,Widget A,150,25.00
New York,2022-03,Widget A,100,25.00
New York,2022-03,Widget B,50,30.00
```
