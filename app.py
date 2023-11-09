from flask import Flask, jsonify, request

server = Flask(__name__)

@server.route('/')
def le_truc():

    return jsonify(
        {
            "res":"welccome to my tmy book API !!!"
        }
    )
books_list=[
    {
        "id":1,
        "title":"tittle 01"
    },
    {
        "id":2,
        "title":"tittle 02"
    }
]

@server.route('/api/books/', methods=['GET', 'POST'])
def all_books():
    limit = 2
    if request.method == 'GET':
        return jsonify(books_list)
    else :
        req = request.json
        new_id = len(books_list)
        for index in range(limit):
            new_id = new_id +1
            new_books = [{
                
            "id": new_id,
            "title": request.json[index]
            }]
        
            books_list.append(new_books)
            print (new_books) 
        
        return 'post request'
@server.route('/api/books/<int:id>', methods=['GET', 'POST','DELETE','PUT'])
def book_one(id):
    if request.method == 'GET':
        try :
            return jsonify({"msg":books_list[id-1]})
        except :
            return jsonify({"msg":"Livre non trouvé"}),404
    elif request.method == 'DELETE':
        try:
            books_list.remove(books_list[id-1])
            return jsonify({"msg":"Livre {id} supprimé"}),200
        except :
            return jsonify({"msg":"Livre non trouvé"}),404
    elif request.method == 'PUT':
        try:
            books_list[id-1]['title'] = request.json['title']
            return jsonify({"msg":"Book updated"}),200
        except :
            return jsonify({"msg":"Livre non trouvé"}),404
    
server.debug = True
server.run()