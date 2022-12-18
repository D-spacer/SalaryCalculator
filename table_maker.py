from terminaltables import AsciiTable

def create_table(dictionary):
  table_data = [['Язык', 'Ср. зарплата', 'Число записей']]
  for i in range(len(dictionary)):
    table_data.append([])
  for index, language in enumerate(dictionary, start=1):
    table_data[index].append(language)
    table_data[index].append(dictionary[language]['Average salary'])
    table_data[index].append(dictionary[language]['Queries'])
  table = AsciiTable(table_data)
  print(table.table)