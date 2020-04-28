from flask import Flask, render_template, request, send_file, send_from_directory
app = Flask(__name__)


links = {
	"github": "https://github.com/sebbycat",
	"facebook": "https://www.facebook.com/yuming.long.9",
	"linkedin": "https://www.linkedin.com/in/yuming-long/"
}



@app.route('/', methods=["GET", "POST"])
def index():
     if request.method == "POST" :
     		return send_file("./pdf/resume.pdf", attachment_filename="resume.pdf", as_attachment=True)
     else:
     		return render_template("index.html", links=links)


@app.route('/<name>')
def index1(name):    
    return "hello, world " + name

if __name__ == '__main__' :
	app.run(debug = True ,host ='0.0.0.0')
