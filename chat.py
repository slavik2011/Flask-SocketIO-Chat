#!/bin/env python
from app import create_app, socketio
import sys

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(sys.argv[1]), allow_unsafe_werkzeug=True)
