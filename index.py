from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/test/incoming', methods=['POST'])
def incoming():
    event_type = request.form['event_type']

    if event_type == 'ping':
        return jsonify({'content': 'pong'})
    else:
        content = request.form['content']
        command = request.form['command']
        command_argument = request.form['command_argument']

        appear_url =  'https://appear.in/%s' % command_argument

        content = content.replace(u'%s %s' % (command, command_argument),
                                  u'📹 [%s](%s)' % (command_argument, appear_url))

        return jsonify({
            'content': content,
        })

@app.route('/incoming1', methods=['GET'])
def incoming1():
    return jsonify({
            'Foo': "Bar",
        })


if __name__ == '__main__':
    app.run()