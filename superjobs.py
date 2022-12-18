import requests
import salary_calculator

def predict_rub_salary_sj(query, pages=1):
  comulative = 0
  count = 0
  key = 'v3.h.4419416.9944a64c342f275a7d558137f9aa0a817a3262dd.6775a860540a8b7b854f5fb005b38b467653988d'
  for page in range(pages):
    header = {
      'X-Api-App-Id': key
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