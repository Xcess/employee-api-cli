There are multiple takes on this challenge.

*Bash one-liner*

Age Avg:

```curl http://dummy.restapiexample.com/api/v1/employees --silent | jq -r '.data[].employee_age' | awk '{ total += $1; count++ } END { print total/count }'```


Salary Avg:

```curl http://dummy.restapiexample.com/api/v1/employees --silent | jq -r '.data[].employee_salary' | awk '{ total += $1; count++ } END { print total/count }'```
