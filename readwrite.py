#reads name.txt into a variable my_name and then
with open('name.txt') as f:
    my_name = f.read()

print(my_name)

#writes a new file named output/hello.txt with the contents Hello, my name is <my_name>.

with open('output/hello.txt', 'w') as f:
    f.write('hello, my name is '+ my_name)
    f.write('\n')