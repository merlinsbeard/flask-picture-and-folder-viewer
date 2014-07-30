from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, request, flash

import os
from slugify import slugify

DATABASE = False

app= Flask(__name__)
app.config.from_object(__name__)

def get_root_dirs_files():
    """
        Returns a dict containing the paths of Pictures and Pictures Folder,
        Inside the static/uploads/Pictures Folder.

    """
    main_path = os.path.dirname(os.path.abspath('__file__'))
    new_path= main_path + '/static/uploads/Pictures'
    path_subtract = main_path + '/static/'
    root_dirs_files = {}
    samp={}
    for root, dirs, files in os.walk(new_path):
        relative_path = root.replace(path_subtract,"")
        new_key = slugify(relative_path)
        folder_name = relative_path.replace("uploads/Pictures/","")
        samp[new_key] = {
                'relative_path': relative_path,
                'dirs': dirs,
                'files': files,
                'folder_name': folder_name,
                }


    #return root_dirs_files
    return samp


@app.route('/')
def index():
    #return render_template('index.html')
    r= get_root_dirs_files()
    dicts = 'hello'
    dicts =r
    return render_template('index.html', dicts=dicts)


@app.route('/album/<slug>')
def show_album(slug):
    r= get_root_dirs_files()
    try:
        r = r[slug]
    except:
        return 'Album Not Existing'
    return render_template('albums.html', dicts=r)

if __name__ == '__main__':
    app.debug == True
    app.run(host='0.0.0.0',port=5001)
