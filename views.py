from flask import render_template, request
from app import app
from schedule_api import *


@app.route('/')
def index():
    options = {}

    options['terms'] = get_terms()
   

    return render_template('index.html', **options)

@app.route('/term/<id>/')
def schoolIndex(id):
    options = {}
    
    options['termid'] = id
    options['schools'] = get_schools(id)

    return render_template('schoolIndex.html', **options)

@app.route('/term/<id>/school/<id2>/')
def subjectIndex(id,id2):
	options = {}

	options['termid'] = id
	options['schoolid'] = id2

	options['subjects'] = get_subjects(id,id2)

	return render_template('subjectIndex.html', **options)

@app.route('/term/<id>/school/<id2>/subject/<id3>/')
def catalognumbersIndex(id,id2,id3):
	options = {}

	options['termid'] = id
	options['schoolid'] = id2
	options['subject'] = id3

	options['catalognumbers'] = get_catalog_numbers(id,id2,id3)

	return  render_template('catalognumbersIndex.html', **options)

@app.route('/term/<id>/school/<id2>/subject/<id3>/catalognum/<id4>/') 
def courseInfo(id,id2,id3,id4):
	options = {}

	options['termid'] = id
	options['schoolid'] = id2
	options['subject'] = id3
	options['course'] = id4	


	options['courseDescription'] = get_course_description(id,id2,id3,id4)
	options['sections'] = get_section_details(id,id2,id3,id4)

	return render_template('courseInfo.html', **options)

@app.route('/term/<id>/school/<id2>/subject/<id3>/catalognum/<id4>/section/<id5>/')
def sectionDetails(id,id2,id3,id4,id5):
	try:
		options = {}
		locations = {}
		room = {}
		locations['CHEM'] = "Chemistry+Building"
		locations['CCL'] = 'Clarence+Cook+Little+Building'
		locations['DENN'] = "Dennison+Building"
		locations['AH'] = "Angell+Hall"
		locations['ARR'] = "University+of+Michigan"
		locations['ALH'] = "Alice+Lloyd+Hall"
		locations['W-BUS'] = "Wyly Hall"
		locations['WH'] = "West+Hall"
		locations['WEIS'] = "Joan+and+Sanford+Weill+Hall"
		locations['WDC'] = "Charles+Walgreen+Drama+Center"
		locations['USB'] = "Undergraduate+Science+Building"
		locations['UNION'] = "Michigan+Union"
		locations['UMMA'] = "UMMA+Auditorium"
		locations['TISCH'] = "Tisch+Hall"
		locations['TAUBL'] = "Taubman+Medical+Library"
		locations['TAP'] = "Tappan+Hall"
		locations['STRNS'] = "Sterns+Building"
		locations['STOCKWELL'] = "Stockwell+Hall"
		locations['STAMPS'] = "Stamps+Auditorium"
		locations['SSWB'] = "School+of+Social+Work+Building"
		locations['SRB'] = "Space+Research+Building"
		locations['SPH2'] = "Thomas+Francis+Jr+Building+School+of+Public+Health+II"
		locations['SPH1'] = "Henry+Vaughan+Building+School+of+Public+Health+I"
		locations['SNB'] = "School+of+Nursing+Building"
		locations['SM'] = "Earl+Moore+School+of+Music"
		locations['SHAPIRO'] = "Shapiro+Undergraduate+Library"
		locations['SEB'] = "School+of+Education+Building"
		locations['SCHEM'] = "Glen+Schembechler+Hall"
		locations['RUTHVEN'] = "Natural+History+Museum"
		locations['REVELLI'] = "Reveilli+Hall"
		locations['R-BUS'] = "Ross+School+of+Business"
		locations['RAND'] = "Randall+Laboratory"
		locations['PIER'] = "Pierpont+Commons"
		locations['PALM'] = "Palmer+Commons"
		locations['NS'] = "Natural+Science+Building"
		locations['NQ'] = "North+Quad"
		locations['400NI'] = "400+North+Ingalls+Building"
		locations['NIB'] = "300+North+Ingalls+Building"
		locations['NH'] = "North+Hall"
		locations['NAME'] = "Naval+Architecture+and+Marine+Engineering+Building"
		locations['MSRB3'] = "Medical+Science+Building+III"
		locations['MSC2'] = "Medical+Science+Building+II"
		locations['MSC1'] = "Medical+Science+Building+I"
		locations['MOSHER'] = "Mosher+Jordan+Hall"
		locations['MLB'] = "Modern+Languages+Building"
		locations['MHRI'] = "Mental+Health+Research+Institute"
		locations['MH'] = "Mason+Hall"
		locations['MARKLEY'] = "Mary+Markley+Hall"
		locations['LSSH'] = "Law+School+South+Hall"
		locations['LSI'] = "Life+Sciences+Institute"
		locations['LSA'] = "Literature+Science+and+the+Arts+Building"
		locations['LORCH'] = 'Lorch+Hall'
		locations['LLIB'] = "Law+Library"
		locations['LEC'] = "Lurie+Engineering+Center"
		locations['LEAG'] = "Michigan+League"
		locations['LBME'] = "Lurie+Biomedical+Engineering+Building"
		locations['LANE'] = "Lane+Hall"
		locations['KELSEY'] = "Kelsey+Museum+of+Archaeology"
		locations['KHRI'] = "Kresge+Hearing+Research+Institute"
		locations['KEC'] = "Kelogg+Eye+Center"
		locations['K-BUS'] = "Kresge+Library"
		locations['ISR'] = "Institute+for+Social+Research"
		locations['IOE'] = "Industrial+Operations+Engineering+Building"
		locations['IM POOL'] = "Intramural+Building"
		locations['HUTCH'] = "Hutchins+Hall"
		locations['HH'] = "Haven+Hall"
		locations['GLIBN'] = "Harlan+Hatcher+Graduate+Library"
		locations['GGBL'] = "G+G+Brown+Library"
		locations['GFL'] = "Gorguze+Family+Laboratory"
		locations['FXB'] = "Francois+Xavier+Bagnoud+Building"
		locations['FORD LIB'] = "Ford+Library"
		locations['EWRE'] = "Environmental+and+Water+Resources+Engineering+Building"
		locations['ERB1'] = "Engineering+Research+Building+1"
		locations['ERB2'] = "Engineering+Research+Building+2"
		locations['EQ'] = "East+Quadrangle"
		locations['EH'] = "East+Hall"
		locations['EECS'] = "Electrical+Engineering+and+Computer+Science+Building"
		locations['E-BUS'] = "Executive+Education"
		locations['DOW'] = "Macromolecular+Science+and+Engineering"
		locations['DENT'] = "Dental+Building"
		locations['DC'] = "Duderstadt+Center"
		locations['DANCE'] = "Dance+Building"
		locations['DANA'] = "Dana+Building"
		locations['CRISLER'] = "Crisler+Arena"
		locations['COUZENS'] = "Couzens+Hall"
		locations['COOL'] = "2355+Bonisteel+Blvd"
		locations['COMM PARK'] = "Commerce+Park"
		locations['CHRYS'] = "Chrysler+Center+Bonisteel"
		locations['CCRB'] = "Central+Campus+Recreation+Building"
		locations['CAMP DAVIS'] = "Camp+Davis"
		locations['BUS'] = "Ross+School+of+Business"
		locations['BURS'] = "Bursley+Hall"
		locations['BSRB'] = "Biomedical+Science+Research+Building"
		locations['BOT GARD'] = "Matthaei+Botanical+Gardens"
		locations['BMT'] = "Burton+Memorial+Tower"
		locations['BIOL STAT'] = "Biological+Station"
		locations['BEYSTER'] = "Bob+and+Betty+Beyster+Building"
		locations['BELL POOL'] = "Margaret+Bell+Pool+CCRB"
		locations['BAM HALL'] = "Blanch+Anderson+Moore+Hall"
		locations['ARGUS3'] = "Argus+Building+III"
		locations['ARGUS2'] = "Argus+Building+II+Television+Center"
		locations['ANNEX'] = "Public+Policy+Annex"
		locations['AL'] = "Walter+Lay+Automotive+Lab"
		locations['A&AB'] = "Art+and+Architecture+Building"
		locations['TBA'] = "University+of+Michigan"
		locations[' '] = "Kelsey+Museum+of+Archaeology"
		locations['AUD'] = "UMMA+Auditorium"
		locations['WEILL'] = "Joan+and+Sanford+Weill+Hall"
		locations['HOSP'] = "University+of+Michigan+Hospital"
		locations['HALL'] = "Couzens+Hall"
		locations['STB'] = "South+Thayer+Building"

		options['meeting'] = get_meetings(id,id2,id3,id4,id5)
		options['instructor'] = get_instructors(id,id2,id3,id4,id5)
		options['section'] = get_section_add_details(id,id2,id3,id4,id5)
		options['locations'] = locations
		options['course'] = options['meeting'][0]['Location'].split(' ')

			
				
		if (id2 == 'LSA' or id2 == 'RC'):
			if options['meeting'][0]['Location'] == 'AUD 3 MLB':
					options['room'] = [u'1200', u'MLB']
			elif options['meeting'][0]['Location'] == 'AUD 4 MLB':
					options['room'] = [u'1400', u'MLB']
			elif options['meeting'][0]['Location'] == '2009 RUTHVEN':
					options['room'] = [u'2009', u'AGRMU']
			elif options['meeting'][0]['Location'] == 'TBA':
					options['room'] = room
			else:
				options['room'] = options['meeting'][0]['Location'].split(' ')
		else:
			options['room'] = room


		return render_template('sectionDetails.html', **options)

	except:

		return render_template('errorMessage.html',**options)
	
	
