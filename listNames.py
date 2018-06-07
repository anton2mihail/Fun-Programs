def main():
    prices = [[ 1.0, 3.50, 7.50 ],
            [ 10.0, 30.50, 70.50 ],
            [ 100.0, 300.50, 700.50 ],
            [ 1000.0, 3000.50, 7000.50 ]]
    print(rowavg(prices))
    print(colavg(prices))
    printTable(prices)


def listavg(lst):
    xavg = 0
    for i in lst:
        xavg += i
    return xavg/len(lst)


def rowavg(t):
    avg = []
    count = 0
    while count <= 3:
        temp_row = [int(i) for i in t[count]]
        avgRow = sum(temp_row)/len(temp_row)
        avg.append(avgRow)
        count += 1
    return avg


def colavg(tList):
    avg = []
    ncols = len(tList[0])
    colCount = 0
    for i in range(ncols):
        rowCount = 0
        while colCount <= 2 and rowCount <= 3:
            tempCol = []
            tempCol.append(tList[rowCount][colCount])
            avgCol = 0
            for z in tempCol:
                avgCol += z
            rowCount += 1
        avg.append(avgCol/len(tList))
        colCount += 1
    return avg


def printTable(t):
    ravg = rowavg(t)
    cavg = colavg(t)
    for i in range(0,len(t)):
        for j in range(0,len(t[i])):
            print("%8.2f" % t[i][j],end="")
        print("%8.2f" % ravg[i])
    for i in range(0,len(cavg)):
        print("%8.2f" % cavg[i],end="")
    print()
main()
