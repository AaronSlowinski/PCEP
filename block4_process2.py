def process (data):
    data [1] = 2
    return data [-2]

measurements = [0 for i in range(3)]
process(measurements)
print(measurements [-2])

# prints to 2
