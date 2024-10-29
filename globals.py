global global_var
global_var = "I am Global!"
def print_variables():
    global global_var
    local_var = "I am Local!"
    
print_variables()
print(global_var)
print(local_var)