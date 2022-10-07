# The all target helps automate the whole process: by running `make` from the command line, you can do everything in one go
# You can define further targets that only execute smaller subsets of your data pipeline according to your needs
all: setup clean collect process analyze

.PHONY: setup processed analysis adhoc

# Step to download dependencies (python packages)
setup: requirements.txt assets/

assets/:
	pip install -r requirements.txt
	mkdir -p assets

# TODO: Check what the collect depends on
collect: setup assets/company_reviews.csv

assets/company_reviews.csv:
	# TODO: Download the data from the server and place it in 'assets/company_reviews.csv'


process: collect 
	python3 src/clean.py

analyze: setup analyzeOriginal analyzeProcessed
	# This target is recommended to isolate all data analysis scripts.
	# Once again, it is recommended to separate different types of analysis between scripts,
	# which may span several languages. Diversity is key here so data can be better understood.
	# TODO: Mkdirs and save stuff inside the folders
	# mkdir -p analysis/...

analyzeOriginal: setup
	python3 src/analyzeOriginal.py

analyzeProcessed: process
	python3 src/analyzeWords.py
	python3 src/analyzeStatistics.py
	python3 src/dataAnalysis.py

adhoc:
	# This target is not part of the overall automation, but it can be useful to have something similar
	# to automate some less frequent operation that you might want to run only when strictly necessary
	# (e.g., organize all produced data/analysis and run a notebook for an easier visual verification of obtained results)
	Rscript code/some_adhoc_script.R

clean:
	rm -rf assets data processed analysis
