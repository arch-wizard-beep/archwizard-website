import os
from flask import Flask, request, make_response, render_template

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
    static_url_path='/static'
)

################## ALL THE ROUTES ##################
# the root directory
@app.route('/')
def index():
    
    myname = 'niroj'
    myage = '25'
    mytext = "jobless nerd"
    myarr = [12, 32, 44, 62, 68, 25, 754, 67]
    
    return render_template(
        'index.html',
        name=myname,
        age=myage,
        text=mytext,
        arr=myarr
        )


@app.route('/improvement')
def improvement():
    return render_template('improvement.html')


################## CUSTOM-FILTERS ################## 
@app.template_filter('reverse_string')
def reversing_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times = 2):
    return s * times
    
@app.template_filter('alternate')
def alternate(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])



################## _____ RUN _____ ##################
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)