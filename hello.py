import flask as F
app = F.Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    pp = 5
    content = {
        'a' : 5,
        'b' : {
            'c' : 5
        }
    }
    return F.render_template('index.html', **content, dd = pp)

@app.route('/guest', methods=['GET'])
def quest_get():
    pp = 5
    content = {
        'a' : 5,
        'b' : {
            'c' : 5
        }
    }
    return F.render_template('guest.html', **content, dd = pp)

@app.route('/h', methods=['GET'])
def gg():   
    id = F.request.args.get("id")
    return "id is %s " % id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7032, debug=True)