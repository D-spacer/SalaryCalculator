import requests
import sys
import os
import hh_jobs
import superjobs
import table_maker
from dotenv import load_dotenv

def main():
  languages = ['python', 'java', 'C++']
  superjob_stats = {}
  headhunter_stats = {}
  load_dotenv()
  sj_api_key = os.environ['SJ_API_KEY']
  for language in languages:
    try:
      count, salary = superjobs.predict_rub_salary_sj(language, sj_api_key)
      superjob_stats[language] = {'Average salary': salary, 'Queries': count}
      count, salary = hh_jobs.predict_rub_salary_hh(language)
      headhunter_stats[language] = {'Average salary': salary, 'Queries': count}
    except requests.exceptions.HTTPError:
      sys.exit('Неверная ссылка')
    except ZeroDivisionError:
      print('По данному запросу не найдено вакансий, измените запрос')
  print(table_maker.create_table(superjob_stats))
  print(table_maker.create_table(headhunter_stats))
    
  
if __name__ == "__main__":
    main()
