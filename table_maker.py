from terminaltables import AsciiTable

def create_table(initial_data):
  summ = 0
  table_layout = [['Язык', 'Ср. зарплата', 'Число записей']]
  for index, language in enumerate(initial_data, start=1):
    table_layout.append([])
    table_layout[index].append(language)
    table_layout[index].append(initial_data[language]['Average salary'])
    table_layout[index].append(initial_data[language]['Queries'])
    summ += initial_data[language]['Queries']
  table_layout.append([f'Всего найдено вакансий: {summ}'])
  table = AsciiTable(table_layout)
  return table.table
