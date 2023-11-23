import os

# write a function to print all files full path that ends with .py
def find_files(path):
    lambdas = []
    if not os.path.exists(path):
        print("The path does not exist")
        return
    if os.path.isfile(path):
        return
    # check if directory name is not scripts
    if os.path.basename(path) == "scripts":
        return
    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and full_path.endswith(".py"):
            lambdas.append(full_path)
        elif os.path.isdir(full_path):
            if find_files(full_path): lambdas.extend(find_files(full_path)) 
    return lambdas
print(find_files("."))