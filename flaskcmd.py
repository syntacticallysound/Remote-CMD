from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///custom_commands.db'
db = SQLAlchemy(app)

# Define the CustomCommand model
class CustomCommand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), unique=True, nullable=False)
    command = db.Column(db.String(255), nullable=False)

# Create the database table
with app.app_context():
    db.create_all()

@app.route('/admin', methods=['GET', 'POST'])
def admin():

    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'add':
            # Add a new custom command to the database
            url = request.form['url']
            command = request.form['command']
            new_command = CustomCommand(url=url, command=command)
            db.session.add(new_command)
            db.session.commit()

        elif action == 'edit':
            # Edit an existing custom command in the database
            command_id = request.form['command_id']
            command = CustomCommand.query.get(command_id)
            
            if command:
                command.url = request.form['url']
                command.command = request.form['command']
                db.session.commit()
        
        elif action == 'delete':
            # Delete an existing custom command from the database
            command_id = request.form['command_id']
            command = CustomCommand.query.get(command_id)
            if command:
                db.session.delete(command)
                db.session.commit()
        return redirect(url_for('admin'))
    
    # Fetch all custom commands from the database and convert to dictionary
    custom_commands = {command.id: {'url': command.url, 'command': command.command} for command in CustomCommand.query.all()}
    return render_template('admin.html', custom_commands=custom_commands)

@app.route('/<path:url>')
def trigger_custom_cmd(url):

    command = CustomCommand.query.filter_by(url=url).first()
    
    if command:
        cmd = command.command

        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output_lines = result.stdout.splitlines()
            return jsonify({'output': output_lines})
        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        return jsonify({'error': 'Custom command not found.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
