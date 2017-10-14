from flask import Flask
from flask import jsonify
from flask import request
import translator

app = Flask(__name__)


@app.route('/ting/incoming', methods=['POST'])
def incoming():
    event_type = request.form['event_type']

    if event_type == 'ping':
        return jsonify({'content': 'pong'})
    else:
        content = request.form['content']
        command = request.form['command']
        command_argument = request.form['command_argument']

        language = command_argument.split()[0]


        num_letters = len(language)+1
        script = command_argument[num_letters:]
        
        content = u'🇪🇸%s' % translate_text("fr", script)

        return jsonify({
            'content': content,
        })



if __name__ == '__main__':
    app.run()