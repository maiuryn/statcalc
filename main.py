
def main():
    a = [1, 2, 3, 4]
    print("Sum: " + sum(a))
    print("Mean: " + mean(a))
    print("Variance: " + variance(a))
    print("Standard Deviation: " + stdDev(a))
    print("Median: " + median(a))

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

main()