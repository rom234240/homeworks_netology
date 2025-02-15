from pprint import pprint

cook_book = {
'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
 ],
 'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
 ],
 'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
 ],
 'Фахитос': [
    {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
    {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
 ]
}

def get_shop_list_by_dishes(dish_list, person_count):
   
   shop_list = {}
    
   for dish in dish_list:
      if dish not in cook_book:
         print(f'Блюда нет в кулинарной книге')
            
      for ingredient in cook_book[dish]:
         name = ingredient['ingredient_name']
         quantity = ingredient['quantity'] * person_count
         measure = ingredient['measure']

         if name in shop_list:
            if shop_list[name]['measure'] == measure:
               shop_list[name]['quantity'] += quantity
         else:
            shop_list[name] = {'quantity': quantity, 'measure': measure}
   return shop_list

dishes = ['Омлет', 'Фахитос', 'Запеченный картофель', 'Утка по-пекински']
persons = 10
shopping_list = get_shop_list_by_dishes(dishes, persons)

pprint(shopping_list)