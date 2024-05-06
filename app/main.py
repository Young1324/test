import os

from flask import Flask

app = Flask(__name__)

@app.route('/get-image', methods=['GET'])
def get_image():
    image_url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.KX_05K6jrKo-yU66jG3mNwHaFo?w=260&h=198&c=7&r=0&o=5&dpr=1.3&pid=1.7'
    return image_url

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))


