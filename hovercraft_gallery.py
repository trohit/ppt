#!/usr/bin/python3
################################################
# Can be used to create a HTML5 galery of photos
# Step 1 : 
#   ./hovercraft_gallery.py > gallery.rst
# Step 2 : 
#   hovercraft gallery.rst gallery
################################################


import jinja2
import os
import glob

def get_list_of_interesting_images(filt="./images/*.jpg"):
    ll = glob.glob("./images/*.jpg")
    return ll

def make_list(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def render_output(template_name, pic_list):
    heredoc="""
:title: HoverCraft Gallery 

generated from https://github.com/trohit/ppts/hovercraft_gallery.py

"""
    #loader = jinja2.FileSystemLoader(os.getcwd())
    loader = jinja2.FileSystemLoader("templates")
    jenv = jinja2.Environment(loader = loader, trim_blocks= True, lstrip_blocks = True)
    template = jenv.get_template(template_name)
    print(heredoc)
    for i in (range(len(pic_list))):
        #print(pic_list[i])
        print(template.render(index=i, pic=pic_list[i]))
    

if __name__ == "__main__":
    # ls -1 images > ls.txt
    # ll = make_list("ls.txt")
    ll = get_list_of_interesting_images()
    #print(ll)
    #output = template.render()
    render_output('hovercraft_gallery.tmpl', ll)



