# def outer_color_func():
#     color = "blue"

#     def inner_color_func():
#         # declare a new 'color' local variable
#         color = "red"
#         print(color)  # This will print "red"

#     inner_color_func()
#     # This will print "blue" because 'color' in inner_color_func is local to that function
#     print(color)


# outer_color_func()

def outer_color_func():
    color = "blue"

    def inner_color_func():
        nonlocal color
        # This will modify the 'color' variable in the outer function's scope
        color = "red"
        print(color)  # This will print "red"

    inner_color_func()
    print(color)  # This will print "red"


outer_color_func()
