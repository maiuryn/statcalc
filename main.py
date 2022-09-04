
def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Sum: " + str(sum(a)))
    print("Mean: " + str(mean(a)))
    print("Variance: " + str(variance(a)))
    print("Standard Deviation: " + str(stdDev(a)))
    print("Median: " + str(median(a)))

    a.sort()
    print(a)

#Sum of the array arr
def sum(arr):
    result = 0
    for x in arr:
        result += x
    return result

#Mean of the array arr
def mean(arr):
    return sum(arr) / len(arr)

#Variance of the array arr
def variance(arr):
    result = 0
    m = mean(arr)
    for x in arr:
        result += (x - m) ** 2
    return (result / len(arr))

#Standard deviation of the array arr
def stdDev(arr):
    return variance(arr) ** 0.5

#Median of the array arr
def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        return arr[len(arr) / 2]

#Organize data into 2D array histogram
#def histogram(arr, step):  
#    arr.sort()
#    result = []
#   for i in range(max(arr) // step + 1):
#        current = []
#        for x in range(len(arr)):
#           current.append(arr[x])
#    return result

main()