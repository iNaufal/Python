import yaml #pip install pyyaml

def extract_yaml(file_path, keyword=None):
  with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
  
  if keyword:
    results = [employee.get(keyword) for employee in data.get('employees', []) if keyword in employee]
  else:
    results = data.get('employees', [])
  
  return results

#validasi maintain code
if __name__ == '__main__':
  while True:
    ymlFile = 'config.yaml'
    search_key = input("Enter 'all' to retrieve all data or enter a keyword to search for: ")

    #Validation search result data
    if search_key.lower() == 'all':
        search_results = extract_yaml(ymlFile)
    else:
        search_results = extract_yaml(ymlFile, search_key)
        
    if search_results:
      print(f"Search results for '{search_key}': ")
      for result in search_results:
        print(result)
        #manipulation result data
        # print("".join(f"{key}: {value}, " for key, value in result.items()))
    else:
      print(f"No results found for '{search_key}'")
      
    search_again = input("\nDo you want to search again? [y/n]")
    if search_again == "n":
      break