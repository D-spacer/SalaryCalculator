import requests
import salary_calculator

def predict_rub_salary_sj(language, sj_api_key, pages=1, city=4, results_per_page=100, category=48, allow_without_salary=1):
    comulative = 0
    count = 0
    for page in range(pages):
      header = {
        'X-Api-App-Id': sj_api_key
      }
      parameters = {
        "page": page,
        "count": results_per_page,
        'town': city,
        'catalogues': category,
        'keyword': language,
        'currency': 'rub'
      }
      response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=header, params=parameters)
      response.raise_for_status()
      decoded_response = response.json()
      for job in decoded_response['objects']:
        count += 1
        with_salary = 0
        if job["payment_from"] or job["payment_to"]:
            salary = salary_calculator.predict_salary(job["payment_from"], job["payment_to"])
            with_salary += 1
            comulative += salary
    if count != 0:
        return count, with_salary, int(comulative / count)
