
I did three takes on this challenge mainly because all of them look reasonable to me depending on the circumstances including time, scope, further maintainability and focus.


---
*sysadmin take*


Age Average:

```curl http://dummy.restapiexample.com/api/v1/employees --silent | jq -r '.data[].employee_age' | awk '{ total += $1; count++ } END { print total/count }'```

Salary Average:

```curl http://dummy.restapiexample.com/api/v1/employees --silent | jq -r '.data[].employee_salary' | awk '{ total += $1; count++ } END { print total/count }'```

---
*data science take*

View on [Google Colab](https://colab.research.google.com/drive/1hZUZMWFcegC30An-38opYdhtzKjaWWG4?usp=sharing)

---
*developer take*

The code resides in this repo. 
To run the code it's best to use [poetry](https://python-poetry.org/)

Install all dependencies:

    poetry install

Run it:

    poetry run python main.py
To view help use -h flag:

    poetry run python main.py -h

You can also build a docker image using the specified Dockerfile

    docker build -t employee_api:0.1.0 .
    docker run --rm -it employee_api:0.1.0

To run the tests, install dev dependencies and run tests like this:

    poetry install --dev
    poetry run python -m pytest

