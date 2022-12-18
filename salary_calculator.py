def predict_salary(salary_from, salary_to):
  salary = 0
  if salary_from is not None and salary_to is not None:
    salary = (salary_from + salary_to) / 2
  elif salary_from is not None and salary_to is None:
    salary = salary_from * 1.2
  else:
    salary = salary_to * 0.8
  return salary