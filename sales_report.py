"""Generate sales report showing total melons each salesperson sold."""


def get_melons_sold_by_salesperson(file_path):
    sales_data = {}

    with open(file_path, 'r') as f:
        for line in f:
            sales_person, amount, sold_melons = line.split('|')
            sold_melons = int(sold_melons)

            if sales_person in sales_data:
                sales_data[sales_person] += sold_melons
            else:
                sales_data[sales_person] = sold_melons

    return sales_data


def print_sales_report(datas):
    for name, sold_melons in datas.items():
        print(f'{name} sold {sold_melons} melons.')


print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))
