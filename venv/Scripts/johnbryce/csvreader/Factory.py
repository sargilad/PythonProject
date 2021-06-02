import csv

ORDERS_CSV = 'orders.csv'
CUST_CSV = 'cust.csv'


class Factory:
    name = ""
    filtered_orders = []

    def __init__(self, name):
        self.name = name

    def get_id_by_name(self):
        with open(CUST_CSV) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if row[1] == self.name:
                    return row[0]
        return None

    def get_orders_by_id(self, id):
        with open(ORDERS_CSV) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if row[1] == id:
                    self.filtered_orders.append(row)

    def calc_sum_of_orders(self):
        sum=0
        for order in self.filtered_orders:
            sum += int(order[3])

        return sum
