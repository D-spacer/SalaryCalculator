import requests
import salary_calculator

def predict_rub_salary_sj(query, sj_api_key, pages=1):
  comulative = 0
  count = 0
  for page in range(pages):
    header = {
      'X-Api-App-Id': sj_api_key
    }
    parameters = {
      "page": page,
      "count": 100,
      'town': 4,
      'catalogues': 48,
      'keyword': query,
      'no_agreement': 1,
      'currency': 'rub'
    }
    response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=header, params=parameters)
    response.raise_for_status()
    decoded_response = response.json()
    for job in decoded_response['objects']:
      count += 1
      salary = salary_calculator.predict_salary(job["payment_from"], job["payment_to"])
      # print(job["payment_from"], job["payment_to"])
      # print(job['profession'], job['town']['title'], salary)
      comulative += salary
      
  return count, int(comulative / count)
