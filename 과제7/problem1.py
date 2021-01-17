import matplotlib.pyplot as plt
import xlrd
 
while True:
    wb = xlrd.open_workbook(filename = 'elec.xlsx')
    ws = wb.sheet_by_name('Sheet1')
    data = []
    for r in range(ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        data.append(col)
    labels = 'No.1 '+data[0][0], 'No.2 '+data[0][1], 'No.3 '+data[0][2], 'No.4 '+data[0][3], 'No.5 '+data[0][4]
    explode = (0.05, 0.05, 0.05, 0.05, 0.05)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("20th election")
    plt.pie(data[1], explode = explode, labels = labels, autopct = '%1.1f%%', startangle=70)
    plt.draw()
    plt.pause(10)    #10초마다 다시 그리기
    plt.clf()
