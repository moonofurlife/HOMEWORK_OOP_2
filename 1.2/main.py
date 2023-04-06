import pprint
cook_book = {}
d = []

with open('recipes.txt', 'rt') as file:
	for l in file:
		name = l.strip()
		ingredient_list = []
		dishes = {"name": name, "ingredient_name": []}
		person_count = file.readline()
		for i in range(int(person_count)):
			emp = file.readline()
			ingredient_name, quantity, measure  = emp.strip().split(' | ')
			ingredient_list.append({'ingredient_name': ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure})
			dep = {name: ingredient_list}
		blank_line = file.readline()
		cook_book.update(dep)
		d.append(name)
print('Задание №1\n\ncook_book:\n')
pp = pprint.PrettyPrinter(indent=5)
pp.pprint(cook_book)
# pprint(f'cook_book = \n{cook_book}\n')

def get_shop_list_by_dishes(dishes, person_count):
	list_of_required_products = {}
	for dish in dishes:	
		if dish in cook_book:
			dish_list = {}
			for ingredient in cook_book[dish]:
				if ingredient['ingredient_name'] in dish_list:
					dish_list = {ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}}
				else:
					person = int(ingredient['quantity']) * person_count
					dish_list = {ingredient['ingredient_name']:{'measure':ingredient['measure'], 'quantity': person}}
					list_of_required_products.update(dish_list)
	return list_of_required_products
print('\nЗадание №2\n')
pp = pprint.PrettyPrinter(indent=10)
pp.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))