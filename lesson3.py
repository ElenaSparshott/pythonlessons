train_mass = 22680
train_acceleration = 2
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

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies", train_force, "Newtons of force.")


c = 3*10**8
def get_energy(mass, c):
    return mass * (c**2)

bomb_energy = get_energy(bomb_mass, c)
print(bomb_energy)

print("A 1KG bomb supplies", bomb_energy, "joules")

def get_work(mass, acceralation, distance):
    return get_force(mass, acceralation) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)  

print("The GE train does", train_work, "joules of work over", train_distance, "meters")
