from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  data = {
    'title':'Flask Jinja Template',
    'user': '웅비',
    'is_admin': True,
    'item_list': ["스시", "치킨", "소고기"]
  }

  users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

  # (1) rendering 할 html 파일명 입력
  # (2) html로 넘겨줄 데이터 입력
  return render_template('index.html', data=data, users=users)

if __name__ == "__main__":
  app.run(debug=True)