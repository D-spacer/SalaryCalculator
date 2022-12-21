from terminaltables import AsciiTable

def create_table(dictionary):
  summ = 0
  table_layout = [['Язык', 'Ср. зарплата', 'Число записей']]
  for index, language in enumerate(dictionary, start=1):
    table_layout.append([])
    table_layout[index].append(language)
    table_layout[index].append(dictionary[language]['Average salary'])
    table_layout[index].append(dictionary[language]['Queries'])
    summ += dictionary[language]['Queries']
  table_layout.append([f'Всего найдено вакансий: {summ}'])
  table = AsciiTable(table_layout)
  return table.table
