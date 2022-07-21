train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


f_temp = float(input("Please enter the temp in F:"))
c_temp = (f_temp - 32) * 5/9
print(c_temp)

def f_temp(f_temp):
    c_temp = (f_temp - 32) * 5/9
    print(c_temp)


f100_in_celsius = f_temp(int(100))
print (f100_in_celsius)


def c_to_f(c_temp):
    f_temp = int(c_temp) * (9/5) + 32
    print(f_temp)

c0_in_f = c_to_f(int(0))







def get_force(load, distance):
    return load * distance

