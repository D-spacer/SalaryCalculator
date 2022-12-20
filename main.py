import requests
import sys
import hh_jobs
import superjobs
import table_maker
from dotenv import load_dotenv

def main():
  languages = ['python', 'java', 'C++']
  superjob_result = {}
  headhunter_result = {}
  load_dotenv()
  sj_api_key = os.environ['SJ_API_KEY']
  for language in languages:
    try:
      count, salary = superjobs.predict_rub_salary_sj(language, sj_api_key)
      superjob_result[language] = {'Average salary': salary, 'Queries': count}
      count, salary = hh_jobs.predict_rub_salary_hh(language)
      headhunter_result[language] = {'Average salary': salary, 'Queries': count}
    except requests.exceptions.HTTPError:
      sys.exit('Неверная ссылка')
  print(table_maker.create_table(superjob_result))
  print(table_maker.create_table(headhunter_result))
    
  
if __name__ == "__main__":
    main()
