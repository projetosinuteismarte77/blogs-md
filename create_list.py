import os
file_list_name = 'list.md'
blog_folder = 'blog-md'
os.chdir(blog_folder)
try:
    os.remove(file_list_name)
    print('removed file')
except FileNotFoundError: 
    pass
file_list = open(file_list_name, "w")
print('created file')
files = os.listdir('list')
for index, f in enumerate(files):
    file_list.write(f)
    if index +1 != len(files):
        file_list.write('\n')
print('wrote everything to file' + file_list.read())
file_list.close()

