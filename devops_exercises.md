# DevOps exercise

### Create a Python API

Create a Python API using FastAPI (or another framework of your choice).

This API will contain a single route GET */time*, which takes two parameters: 
- *country* (a string corresponding to an existing country). Ex: France, Germany...
- *format* (a string corresponding to a time format). Ex: HH:mm:ss, hh:mm...
The response will contain the current time corresponding to the specified country and under the specified format. 
Response example :
```
{
   "time": "13:37"
}
```

If the country does not exist, an exception should be raised.

Create unit tests to test the API using Pytest. Use ```pytest-cov```to check the test coverage.

### Dockerize your server

Install docker on your machine if you don't already have it.
Create a Dockerfile that will install your Python dependencies and launch your server.
Then run it in a container (using ```docker run```).


### Create an simple interface

Create a very simple interface using the language of your choice.
It will contain a form containing two dropdown menu: one for choosing a country, one for choosing a time format. Upon submitting the form, the current time of the specified country should be displayed with the specified format. This current time will be retrieved from the API you built previously.


### Create a CI on github actions

Create a github repository and push your application code on it.
Create a workflow on Github Actions that will be executed each time some code is pushed on the main branch.
This workflow will:
- Check the code format with linters such as pylint and mypy.
- Launch unit tests.











