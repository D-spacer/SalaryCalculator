import requests
import sys
import hh_jobs
import superjobs
import table_maker

def main():
  try:
    queries = ['python', 'java', 'C++']
    superjob = {}
    headhunter = {}
    for query in queries:
      count, salary = superjobs.predict_rub_salary_sj(query)
      superjob[query] = {'Average salary': salary, 'Queries': count}
      count, salary = hh_jobs.predict_rub_salary_hh(query)
      headhunter[query] = {'Average salary': salary, 'Queries': count}
    table_maker.create_table(superjob)
    table_maker.create_table(headhunter)
  except requests.exceptions.HTTPError:
    sys.exit('Неверная ссылка')
  
  
if __name__ == "__main__":
    main()