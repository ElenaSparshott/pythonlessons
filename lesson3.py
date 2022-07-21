train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


f_temp = float(input("Please enter the temp in F:"))
c_temp = (f_temp - 32) * 5/9
print(c_temp)


def get_force(load, distance):
    return load * distance

