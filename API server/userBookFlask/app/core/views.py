from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify, make_response
from werkzeug.utils import secure_filename                  
from app.core.repository import *
from app import mysql
from app import app
import os, sys

mod = Blueprint('core', __name__)

# Fake Json datas
users = [
  {
      'id': 1,
      'name': 'Luke',
      'major': 'cs',
      'school': 'university of arkansas', 
      'year': 'senior'
  },
  {
      'id': 2,
      'name': 'Yueun',
      'major': 'cs',
      'school': 'university of arkansas', 
      'year': 'senior'
  },
  {
      'id': 3,
      'name': 'Ryan',
      'major': 'cs',
      'school': 'university of arkansas', 
      'year': 'senior'
  },
  {
      'id': 4,
      'name': 'Michael',
      'major': 'cs',
      'school': 'university of arkansas', 
      'year': 'senior'
  }
]

@mod.route('/')
def index():
  return "Index userBook Api"

@mod.route('/help')
def help():
  repository = Repository()
  return render_template('core/index.html', resources=repository.getResources())

@mod.route('/users')
def get_all_users():
  return jsonify({'users': users})


@mod.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})




# @mod.route('/tasks')
# def get_tasks():
#   return jsonify({'tasks': tasks})

# @mod.route('/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})
  

# @mod.route('/db')
# def loco():
#   cur = mysql.get_db().cursor()
#   cur.execute("SELECT * FROM `AUTHORS`")
#   rows = cur.fetchall()

#   payload = []
#   content = {}
#   for row in rows:
#       content = {'id': row[0], 'firstName': row[1], 'lastName': row[2]}
#       payload.append(content)
#       content = {}
#   cur.close()
#   return jsonify(payload)



# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# def allowed_file(filename):
#   return '.' in filename and \
#     filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @mod.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'image' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['image']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join('app/userFiles/', filename))
#             filePath = "{{ url_for('static', filename='userFiles/" + filename + "' ) }}"
#             print (filePath)
#             return jsonify(
#               {'url': filePath}
#             )


# def listdir_nohidden(path):
#     for f in os.listdir(path):
#         if not f.startswith('.'):
#             yield f