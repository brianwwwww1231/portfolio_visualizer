# down below are the code wrote by our instructor
import pandas as pd

def read_csv(file):
# converters 那邊是告訴它Adj Close那欄 我要讀取成float，否則他預設會是字串。
    df = pd.read_csv(file, converters={'Adj Close': float}) 
    df = df['Adj Close'] # 我只要Adj Close那欄的資料
    return df.tolist() # 轉換回python內建的list物件


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


def calc_profit(data, signal):
    pos = 0 # 持有方向
    entry = 0 # 進場價
    total = 0 # 總共賺的錢
    for i in range(len(data)):
        if signal[i] == 1:
            if pos == 0: # 表示目前沒有持股
                entry = data[i] # 那就只是單純進場，紀錄成本價就好
            elif pos == -1: # 原本持有空單，現在遇到買進訊號
                            # 因為要把空單出場，換成多單
                            # 要先計算 此筆單出場的獲利
                profit = entry - data[i] # 空單的獲利是 成本價 - 現在價格
                total += profit
                entry = data[i]
            pos = 1 # 把持有方向 設為 1
        elif signal[i] == -1:
            if pos == 0: # 表示目前沒有持股
                entry = data[i] # 那就只是單純進場，紀錄成本價就好
            elif pos == 1: # 原本持有多單，現在遇到賣出訊號
                        # 因為要把多單出場，換成空單
                        # 要先計算 此筆單出場的獲利
                profit = data[i] - entry # 空單的獲利是 成本價 - 現在價格
                total += profit
                entry = data[i]
            pos = -1 # 把持有方向 設為 1

    return total * 1000 # 放大一千倍因為每次交易都是一張(1000股)


def main():
    data = read_csv('2330.csv')
    signal = three_days(data)
    total = calc_profit(data, signal)
    print(total)

main()

### down below are the answer wrote by myself 

# # read existed data
# tsmc = []
# with open('2330.csv', 'r') as f:
#     for line in f:
#         if 'Date' in line or 'Open' in line or 'High' in line or 'Low' in line or 'Close' in line or 'Adj Close' in line or 'Volume' in line:
#             continue
#         tsmc.append(line.strip().split(','))

# # revised data -> creat a list of str
# tsmc_revised = []
# num = -1
# for data in tsmc:
#     num += 1
#     if num != None:
#         tsmc_revised.append(tsmc[num][5])
# # print(tsmc_revised)

# # creat a list of list of int
# tsmc_revised_new = []
# for data in tsmc_revised:
#     tsmc_revised_new.append([float(data)])
# # print(tsmc_revised_new)


# # check for buy(1), sell(-1) or hold(0)
# def three_days(data):
#     output = []
#     for i in range(len(data)):
#         print(i)
#         if i < 3:
#             output.append(0)
#         elif data[i] > data[i-1] > data[i-2] > data[i-3]:
#             output.append(1)
#         elif data[i] < data[i-1] < data[i-2] < data[i-3]:
#             output.append(-1)
#         else:
#             output.append(0)
#     return output

# # print(three_days(tsmc_revised))

# # creat a list of a list of tsmc_reviesd_new and output
# num_1 = -1
# for d in three_days(tsmc_revised):
#     num_1 += 1
#     tsmc_revised_new[num_1].append(d)
# # print(tsmc_revised_new)

# quatity = 0
# buy_price = 0
# sell_price = 0
# profit = 0
# for d in tsmc_revised_new:
#     if quatity == 1:
#         if d[1] == 0 or d[1] == 1:
#             continue
#         elif d[1] == -1: # i think there's some problem in line 57
#             quatity = -1
#             sell_price = d[0]
#             profit_cal = sell_price - buy_price
#             profit += profit_cal
#     elif quatity == -1:
#         if d[1] == 0 or d[1] == -1:
#             continue
#         elif d[1] == 1:
#             quatity = 1
#             buy_price = d[0]
#             profit_cal = sell_price - buy_price
#             profit += profit_cal        
#     elif quatity == 0:
#         if d[1] == 0:
#             continue
#         elif d[1] == 1:
#             quatity = 1
#             buy_price = d[0]
#         elif d[1] == -1:
#             quatity = -1
#             sell_price = d[0]
# print(profit)


