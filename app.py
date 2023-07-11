from flask import Flask, jsonify, request

books = [
    {"isbn": "9789020537963",
    "title": "de kleur van colorado",
    "writer": "Rebecca Yarros"
    },
    {"isbn":"9789024592470",
    "title": "Onverbeterlijk",
    "writer":"Lisette Jonkman"
    },
    {"isbn:":" 9789026158254",
    "title": "Het veilige huis",
    "writer": "Anna Downes"
    },
    {"isbn:":"9783499272134",
    "title": "Dochters van een nieuwe tijd",
    "writer": "Carmen Korn"
    },
    {"isbn:":"9789025454647",
    "title": "Het echte leven",
    "writer": "Adeline Dieudonné"
    }
]

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World! This is my first API-call."
    
