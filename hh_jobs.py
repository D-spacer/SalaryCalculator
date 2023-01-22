import requests
import salary_calculator

def predict_rub_salary_hh(vacancy, pages=1, period=30, region=1, results_per_page=100):
    count = 0
    with_salary = 0
    comulative = 0
    for page in range(pages):
      parameters = {
        'text': vacancy,
        'only_with_salary': 'true',
        'period': period,
        'area': region,
        "per_page": results_per_page,
        "page": page,
      }
      response = requests.get('https://api.hh.ru/vacancies', params=parameters)
      response.raise_for_status()
      decoded_response = response.json()
      for job in decoded_response['items']:
        count += 1
        if job['salary']['from'] or job['salary']['to:']:
      	    salary = salary_calculator.predict_salary(job['salary']['from'], job['salary']['to'])
		    with_salary += 1
      	    comulative += salary
    if count != 0:
        return count, with_salary, int(comulative / count)
