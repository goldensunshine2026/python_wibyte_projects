import random

laptop = {'brand':'Dell', 'Model': 'ABC111', 'Processor': 'Intel Core i5'}



print('Welcome to WiByte Laptop store.')
print('We have a huge inventory of laptops.')
print('Please indicate your preference of specs.')
print()


def append_s(name):
  return name + 's'



print()



# Create a list of laptops
laptops_list      = []

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']

specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)

master_dict['Brands'] =  ['WDell', 'WAsus', 'WAcer', 'WLenovo', 'WHP']
master_dict['Models'] = ['AAA', 'BBB', 'CCC']
master_dict['CPUs'] = ['WIntel i5', 'WIntel i7', 'WAMD Ryzen']
master_dict['Speeds'] = ['2 GHz', '3 GHz', '3.15 GHz', '3.8 GHz']
master_dict['RAMs'] = [ '2 GB', '4 GB', '8 GB', '16 GB']
master_dict['Storages'] = [ '128 GB', '256 GB', '512 GB', '1024 GB']
master_dict['Screensizes'] = [ '9 in', '12 in', '14.9 in', '17 in']
master_dict['Prices'] = ['INR 20000', 'INR 30000', 'INR 40000']


for n_laptops in range(60):
  new_laptop = dict.fromkeys(specs)
  for kk in new_laptop:
    new_laptop[kk] = random.choice(master_dict[kk+'s'])
  laptops_list.append(new_laptop)  
  
# Seek user preference

# Display laptops that meet the criterion

#print(kk)
user_choice = dict.fromkeys(specs)
for kk in specs:
  user_choice[kk] = input('Any preference for ' + kk + ' (Enter none for no preference)'+'\n')

query = ''

for kk in user_choice:
  if user_choice[kk].lower() == 'none':
    pass
  else:
    query = query + 'laptop[' + '\'' + kk + '\'] == ' + '\'' + user_choice[kk] + '\' and '

print(query)


input()

query = query[0:-4:1]

# Print top row

if query != '':
  selected = [laptop for laptop in laptops_list if eval(query)]
else:
  selected = [laptop for laptop in laptops_list]
  
# Print top row (all the keys of specs)

print(len(selected), 'laptops met your preference.')

characters = 0
for kk in specs:
  print(kk, end = '')
  characters = len(kk)
  print((12 - characters)*' ', end = '')
print()

selected.sort(key=lambda laptop: int(laptop['Price'].replace('INR ', '')), reverse=True)

characters = 0

for laptop in selected:
  for kk in laptop:
    print(laptop[kk],  end = '')
    characters = len(laptop[kk])
    print((12 - characters)*' ', end = '')
  print()


  
