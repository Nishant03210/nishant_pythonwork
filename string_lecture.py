string_var_1 = 12
string_var_2 = "Hello World"
string_var_3 = """Hello World"""
string_var = '''Hello World'''

# print(string_var_1)
# print(type(string_var_1))
# print(isinstance(string_var_1, str))

print(string_var_2.count("l"))
print(string_var_3.center(40,"$"))

# print(dir(string_var_3))



import datetime


## here we are fetching current time which is a instance of datetime object and converted it into string
## using explicit conversion
time = str(datetime.datetime.now())

## we are sp
## we are splitting that timestring using string split method and splitting strings at a whitespace
new_time = time.split(" ")
print(new_time)

print(new_time[1])

#here we are checking if string value is greater than 12 it is afternoon and equal to 24 it is morning
if new_time[1] > "12:00:00":
    print("Good Afternoon")
if new_time[1] == "24:00:00":
    print("Good Morning")