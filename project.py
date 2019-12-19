import csv
import matplotlib.pyplot as plt
import pandas as pd


def read_file():
    with open('Copy of Sales.csv', 'r') as csv_file:
        data = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


def calc_total_sales():
    data = read_file()
    monthly_sales = []
    total_sales = 0
    for row in data:
        monthly_sales.append(int(row["sales"]))
    for sales in monthly_sales:
        total_sales = total_sales + sales
    print('List of sales from each month: {}'.format(monthly_sales))
    print('Total Sales = £{}'.format(round(total_sales, 2)))


def monthly_changes():
    data = read_file()
    monthly_sales = []
    change_percentages = [0]
    count = 0
    for row in data:
        monthly_sales.append(int(row["sales"]))
    for a, b in zip(monthly_sales[::1], monthly_sales[1::1]):
        percentage = round(100 * (b - a) / a, 1)
        change_percentages.append(percentage)
    for elem in change_percentages:
        count = count + 1
        print('Percentage change in month {}: {}%'.format(count, elem))
    return change_percentages


def average():
    data = read_file()
    monthly_sales = []
    total_sales = 0
    for row in data:
        monthly_sales.append(int(row["sales"]))
    for sales in monthly_sales:
        total_sales = total_sales + sales
        avg = total_sales / len(monthly_sales)
    print('Average Sales: £{}'.format(round(avg, 2)))


def highest_month():
    data = read_file()
    monthly_sales = []
    months = []
    for row in data:
        monthly_sales.append(int(row["sales"]))
        months.append(row["month"])
    max_index = monthly_sales.index(max(monthly_sales))
    max_month = months[max_index]
    print('Month With Highest Sales: {}'.format(max_month))
    return max_month


def lowest_month():
    data = read_file()
    monthly_sales = []
    months = []
    for row in data:
        monthly_sales.append(int(row["sales"]))
        months.append(row["month"])
    min_index = monthly_sales.index(min(monthly_sales))
    min_month = months[min_index]
    print('Month With Lowest Sales: {}'.format(min_month))
    return min_month


def plot_data():
    data = read_file()
    x = []
    y = []
    height = monthly_changes()
    for row in data:
        y.append(int(row["sales"]))
        x.append(row["month"])

    plt.figure(1)
    plt.plot(x, y, label='Monthly Sales', color='black', linewidth=1)
    plt.plot(highest_month(), max(y), 'ro', label='Maximum')
    plt.plot(lowest_month(), min(y), 'b*', label='Minimum')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales')
    plt.legend()

    plt.figure(2)
    df = pd.DataFrame({'x': x, 'y': height})
    print(df.head())
    ax = df['y'].plot(kind='bar', color=(df['y'] > 0).map({True: 'g', False: 'r'}))
    ax.set_xticklabels(x, rotation=0)
    plt.xlabel('Month')
    plt.ylabel('Percentage change(%)')
    plt.title('Monthly Changes')
    plt.show()

#
# def save_summary():
#     with open('summary.csv', 'w') as file:
#         # writer = csv.writer(file)
#         # total = calc_total_sales()
#         # file.write()
#         print('Filename', filename, file=file)


calc_total_sales()
# monthly_changes()
average()
# highest_month()
# lowest_month()
plot_data()
# save_summary()
