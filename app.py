from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')



@app.route('/kvadrat', methods=['GET','POST'])
def kvadrat():   
    if request.method == 'POST':        
            son=int(request.form.get('son'))
            kvadrat=son**2        
            return render_template('kvadrat.html', kvadrat=kvadrat)
    return render_template('kvadrat.html')



@app.route('/dam', methods=['GET','POST'])
def dam():   
    if request.method == 'POST':    
            kun=request.form.get('kun')    
            harorat=int(request.form.get('harorat'))
            if kun in ["shanba" , "yakshanba"] and harorat>30: 
                return render_template('dam.html', dam="boramiz") 
            else: 
                return render_template('dam.html', error="Boshqa kun boramiz")        
            
    return render_template('dam.html')



@app.route('/x2', methods=['GET','POST'])
def x2():
    sonlar=[]   
    if request.method == 'POST':        
        son = int(request.form.get('son'))
        sonlar = [x for x in range(1, son + 1)]                
    return render_template('x2.html',  sonlar=sonlar) 


@app.route('/oshxona', methods=['GET', 'POST'])
def oshxona():
    mavjud = ["osh", "somsa", "manti", "shashlik"]
    error = None
    taom = None

    if request.method == 'POST':
        selected_taom = request.form.get('taom')  # Get the selected dish from the form
        
        if selected_taom in mavjud:
            taom = selected_taom
        else:
            error = "Ushbu taom bugun yo'q" 
        
    return render_template('oshxona.html', taom=taom, error=error)




if __name__ == '__main__':
    app.run(debug=True)

