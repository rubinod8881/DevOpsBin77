with open("C:/Users/VINOD/Documents/Binod/Devops/python/grade.py","r") as file:
    content=file.read(100)
    print(content)

with open("C:/Users/VINOD/Documents/Binod/Devops/python/sql_ops.txt","r") as file:
    for line in file:
        print(line.strip())  

with open("C:/Users/VINOD/Documents/Binod/Devops/python/sql_ops.txt","r") as file:
    lines=file.readlines(6)
    print(lines)

SELECT emp_name, emp_salary
FROM employee
WHERE emp_salary IN (
    SELECT * FROM (
        SELECT DISTINCT emp_salary 
        FROM employee 
        ORDER BY emp_salary DESC 
        LIMIT 5
    ) AS top_salaries
)
ORDER BY emp_salary DESC;

SELECT * FROM SELECT DISTINCT emp_salary 
 FROM employee 
ORDER BY emp_salary DESC 
    LIMIT 5;