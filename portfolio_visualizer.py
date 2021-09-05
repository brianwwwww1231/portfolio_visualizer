# read existed data
tsmc = []
with open('2330.csv', 'r') as f:
    for line in f:
        if 'Date' in line or 'Open' in line or 'High' in line or 'Low' in line or 'Close' in line or 'Adj Close' in line or 'Volume' in line:
            continue
        tsmc.append(line.strip().split(','))

# revised data -> creat a list of str
tsmc_revised = []
num = -1
for data in tsmc:
    num += 1
    if num != None:
        tsmc_revised.append(tsmc[num][5])
# print(tsmc_revised)

# creat a list of list of int
tsmc_revised_new = []
for data in tsmc_revised:
    tsmc_revised_new.append([float(data)])
# print(tsmc_revised_new)


# check for buy(1), sell(-1) or hold(0)
def three_days(data):
    output = []
    for i in range(len(data)):
        if i < 3:
            output.append(0)
        elif data[i] > data[i-1] > data[i-2] > data[i-3]:
            output.append(1)
        elif data[i] < data[i-1] < data[i-2] < data[i-3]:
            output.append(-1)
        else:
            output.append(0)
    return output

# print(three_days(tsmc_revised))

# creat a list of a list of tsmc_reviesd_new and output
num_1 = -1
for d in three_days(tsmc_revised):
    num_1 += 1
    tsmc_revised_new[num_1].append(d)
# print(tsmc_revised_new)

quatity = 0
buy_price = 0
sell_price = 0
profit_cal = sell_price - buy_price
profit_stat = []

num_2 = -1
for d in tsmc_revised_new:
    num_2 += 1
    if portfolio != 0 and portfolio == 1:
        if d[num_2][1] == 0 or d[num_2][1] == 1:
            continue
        elif d[num_2][1] == -1:
            quatity = -1
            sell_price = d[num_2][0]
            profit
            if 
    elif portfolio != 0 and portfolio == -1:
        continue
        
    else:
        if d[num_2][1] == 0:
            continue
        elif d[num_2][1] == 1:
            quatity += 1
            buy_price = d[num_2][0]
        elif d[num_2][1] == -1:
            quatity -= 1
            sell_price = d[num_2][0]



