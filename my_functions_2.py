def add(x, y,z):
    return x + y + z

res = add(7,8,9)
print(res)

def addition(*nums):
        # total =sum(nums)
        total = 0
        for num in nums:
            total = total + num
        return total
res = addition(1000, 3000,4000,50000,8000.9000)
# print(res)

def save(**data):

    with open('value.txt', 'w') as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")
# save(age=18, dob='2001/11/11', proffesional="Engineer")

save(dob='2025/12/12', name='Kennedy', age=23, proffesional= 'Doctor')

def some_functions(name, *scores, **details):
    pass

some_functions('Kennedy',  70, 99, 89, 90, subject = 'english', attain='A')

def cylinder(r,h):

    """
    calculate the volume and SA of the cylinder
    parameters include radius, height
    return volume and SA of the cylinder
    :param r:
    :param h:
    :return:
    """
    v = 22/7 * r * r * h
    sa = 22/7 * r **2 * 2 + 22/7 *r *2 * h
    return sa ,v
sa , v = cylinder(7, 15)

# print(sa, v)

# Lambda functions
divider = lambda x, y: x/y

area_circle = lambda r: 22/7 * r **2