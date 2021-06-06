from factory import Factory

factory = Factory(input("name?\n"))
orders_by_id = factory.get_orders_by_id(factory.get_id_by_name())
sum = factory.calc_sum_of_orders()
print(f'Total orders {sum}$')
