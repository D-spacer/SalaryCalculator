import requests
import salary_calculator

def predict_rub_salary_hh(vacancy, pages=1):
  count = 0
  comulative = 0
  for page in range(pages):
    parameters = {
      'text': vacancy,
      'only_with_salary': 'true',
      'period': 30,
      'area': 1,
      "per_page": 100,
      "page": page,
    }
    response = requests.get('https://api.hh.ru/vacancies', params=parameters)
    response.raise_for_status()
    decoded_response = response.json()
    for job in decoded_response['items']:
      count += 1
      salary = salary_calculator.predict_salary(job['salary']['from'], job['salary']['to'])
      comulative += salary
  return count, int(comulative / count)