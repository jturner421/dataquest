#pg3
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])


#pg4
pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

#pg5
tip_amount = taxi[:,12]

#pg 6
# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
#pg 7
# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

#pg 8
# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

#pg 10
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

