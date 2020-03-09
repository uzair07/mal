from flask import Flask, render_template,request
import malware_test
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename) 
        s = malware_test.try1(f.filename)
        return render_template("success.html",name='The file %s is %s' % (f.filename,['malicious', 'legitimate'][s]))
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0',port=80,debug = True)  
