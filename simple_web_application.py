from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route('/json', methods=['GET','POST'])
def json():

    if request.method == 'GET':

        print(request.host)
        return jsonify({
                    'Accept': request.accept_mimetypes,
                    'User-Agent': request.headers.get('User-Agent'),
                    'Host': request.host,
                    'Client IP': request.remote_addr
                    }), 200
    elif request.method == 'POST':

        data = request.get_json()
        client_ip = data['client_ip']
        host = data['host']
        user_agent = data['user_agent']
        accept = data['accept']

        return '''
                   Value client ip: {}
                   Value host: {}
                   Valuse user agent: {}
                   Valuse accept: {}'''.format(client_ip, host, user_agent, accept)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)
