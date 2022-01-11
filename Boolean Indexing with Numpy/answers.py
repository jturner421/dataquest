#pg5


tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]

#pg 6
# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

taxi_modified[1066,5] = 1
taxi_modified[:,0] = 16
taxi_modified[550:552,7] = taxi_modified[:,7].mean()

#pg 7
# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

total_amount = taxi_copy[:,13]
total_amount[total_amount < 0] = 0

#pg 8
# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1

#pg9
jfk = taxi[taxi[:,6] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:,6] == 3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]

#pg 10
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

cleaned_taxi = taxi[trip_mph < 100]

mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()