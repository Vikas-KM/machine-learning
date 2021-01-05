from flask import Flask, render_template, request
import movie_recommend_system as mrs
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        user_input = request.form.get('search')
        print(user_input)
        movies_list  = mrs.recommend(user_input)
        # print(movies_list)
    return render_template('index.html', movies_list=movies_list)

if __name__ == '__main__':
    app.run(debug=True)