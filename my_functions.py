# function

def greet():
    print("Hello, welcome to python")

# greet()
# greet()
# greet()

def greeting(user):
    print(f"Hello {user}, welcome to python")


# par/arg
# greeting('ken')
# greeting('Kennedy')

def area_circle(radius, precision):
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)

def volume_cylinder(r,h):
    v= 22/7 * r * r * h
    return v

v1 = volume_cylinder(8.2, 12.8)

print(round(v1))


# area_circle(2.9, 2)
# area_circle(3.2, 0)