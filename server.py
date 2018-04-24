
from flask import Flask, render_template, request
import json


w = json.load(open("worldl.json"))
lota=sorted(list(set([c['name'][0]for c in w])))

print(lota)
for c in w:
	c['tld'] = c['tld'][1:]
page_size = 20
app = Flask(__name__)

@app.route('/')
def mainPage():
	return render_template('index.html', #pass all to index.html page
		page_number=0,
		page_size=page_size,
		w = w[0:page_size],
                lota=lota)

@app.route('/begin/<b>')
def beginPage(b,):
	bn = int(b)

	return render_template('index.html', #pass all to index.html page
		w = w[bn:bn+page_size],
              
		page_number = bn,
		page_size = page_size
		)

@app.route('/continent/<a>')
def continentPage(a):
	cl = [c for c in w if c['continent']==a] 
	return render_template( #pass all to continent.html page
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a
		)


@app.route('/startwith/<a>')
def firstalphabetpage(a):
	cl = [c for c in w if c['name'][0]==a] 
	return render_template( #pass all to continent.html page
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a,
		lota=lota)


@app.route('/country/<i>')
def countryPage(i):
	return render_template( #pass all to country.html page
		'country.html',
		c = w[int(i)])


@app.route('/countryByName/<n>')
def countryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country.html', #pass all to country.html page

		c = c)

@app.route('/delete/<n>')

def deleteCountryPage(n):
	i=0
	for c in w:
		if c['name'] == n:
			break

		i+=1

	del w[i]
	return render_template('index.html', #pass all to index.html page

		page_number=0,
		page_size=page_size,
		w = w[0:page_size])


@app.route('/editcountryByName/<n>')
def editcountryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country-edit.html', #pass all to country-edit.html page

		c = c)


@app.route('/updatecountrybyname')
def updatecountryByNamePage():
	n=request.args.get('name')
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	c['capital']=request.args.get('capital')
	c['continent']=request.args.get('continent')
	c['population']=request.args.get('population')
	c['gdp']=request.args.get('gdp')
	c['area']=request.args.get('area')
	return render_template(
		'country.html',
		c = c)



@app.route('/createcountry')
def createcountry():
        c['name']=request.args.get('name')
        c['capital']=request.args.get('capital')
        c['continent']=request.args.get('continent')
        c['population']=request.args.get('population')
        c['area']=request.args.get('area')
        c['gdp']=request.args.get('gdp')
        c['tld']=request.args.get('tld')
        return render_template(
		'create.html',
		c = c)

app.run(host='0.0.0.0', port=5618, debug=True)



