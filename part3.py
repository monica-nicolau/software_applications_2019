from flask import Flask, render_template, request, session, redirect
import os.path
import pandas as pd
import part1 as p

app = Flask(__name__)

class_dict = p.class_dictionary
template_directory = os.path.join(app.root_path, 'templates')

def read(html_file, table):
	with open(template_directory +'/'+ html_file, "r") as text_file:
		text_file = text_file.read()
		if table not in text_file: 
			return None
			text_file.close()
		else: 
			return True
			text_file.close()

def replace(html_file, table):
	with open(template_directory +'/'+ html_file, "r") as text_file:
		content = text_file.read()
		old_tab = content[content.find("<table"):]
		content = content.replace(old_tab, table)
		text_file.close()
	with open(template_directory +'/'+ html_file, "w") as text_file:
		text_file.write(content)

def formatter(html_file, table):
	check = read(html_file, table)
	if check is None:
		replace(html_file, table)
	return render_template (html_file, table =[table])

@app.route('/')
def index():
	return render_template('homepage.html')
	
@app.route('/help')
def helping():
	return render_template('help.html')
	
@app.route('/dfinfo')
def geninfo():
	return render_template('dfinfo.html')

@app.route('/dataframe')
def dataframe():
	return render_template('dataframe.html')

@app.route('/dimensions')
def dimensions():
	html = class_dict['Number'].to_html(index=False, justify="justify-all")
	return formatter('dimensions.html', html)

@app.route('/semantics')
def labelling():
	html = class_dict['Semantics'].to_html(index=False, justify="justify-all")
	return formatter('semantics.html', html)

@app.route('/biotype')
def type():
	html = class_dict['Biotype'].to_html(index=False, justify="justify-all")
	return formatter('biotype.html', html)

@app.route('/associate')
def associations():
	return render_template("associate.html")
	
@app.route('/login', methods=["GET", "POST"])
def login():
	d = class_dict['Associate']
	l = list(d.index.values)
	if request.method == "POST":
		global choice
		choice = request.form.get("biotype", None)
		if choice != "Select biotype":
			choice_res = d.loc[str(choice), :]
			choice_frame = choice_res.to_frame()
			global choice_html
			choice_html = choice_frame.to_html()
		if choice != None:
			return render_template("associate.html", l=l, choice=choice)
	return render_template("associate.html")

@app.route('/results')
def show_results():
	try:
		if choice != "Select biotype":
			replace("results.html", choice_html)
			return render_template("results.html", table=[choice_html])
		else: return render_template("error.html")
	except NameError:
		return render_template("error.html")	
		
@app.route('/chromosome')
def chrom():
	html = class_dict['Chromosome']
	return formatter('chromosome.html', html)

@app.route('/genechr')
def gchromosome():
	html = class_dict['Genes_Chromosome'].to_html(index=False, justify="justify-all")
	return formatter('genechr.html', html)

@app.route('/strandperc')
def perc():
	return render_template('strandperc.html')

@app.route('/plus')
def plus_strand():
	html = class_dict['Plus'].to_html(index=False, justify='justify-all')
	return formatter('plus.html', html)

@app.route('/minus')
def minus_strand():
	html = class_dict['Minus'].to_html(index=False, justify='justify-all')
	return formatter('minus.html', html)

@app.route('/credits')
def cred():
	return render_template('credits.html')

if __name__ == '__main__':
	app.run(debug=True)