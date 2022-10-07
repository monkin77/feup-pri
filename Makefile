python = python3

# The all target helps automate the whole process: by running `make` from the command line, you can do everything in one go
# You can define further targets that only execute smaller subsets of your data pipeline according to your needs
all: setup clean collect process analyze

# .PHONY: setup processed analysis adhoc


# ========== Setup ==========
setup: requirements.txt assets/

assets/:
	pip install -r requirements.txt
	mkdir -p assets/images

# ========== Collect ==========
collect: setup assets/company_reviews.csv

assets/company_reviews.csv:
	# TODO: Download the data from the server and place it in 'assets/company_reviews.csv'

# ========== Process ==========
process: collect assets/cleaned_reviews.csv assets/processed_reviews.csv assets/processed_reviews.json

assets/cleaned_reviews.csv:
	$(python) src/clean.py

assets/processed_reviews.csv:
	$(python) src/processing.py
assets/processed_reviews.json:
	$(python) src/processing.py

# ========== Analyze ==========
analyze: setup analyzeOriginal analyzeStatistics analyzeWords analyzeGraphs

# TODO: CHECK IF WE NEED THESE DEPENDENCIES
analyzeOriginal: assets/cleaned_reviews.csv setup
	$(python) src/analyzeOriginal.py

analyzeStatistics: assets/cleaned_reviews.csv setup
	$(python) src/analyzeStatistics.py

analyzeWords: assets/cleaned_reviews.csv setup
	$(python) src/analyzeWords.py

analyzeGraphs: assets/processed_reviews.csv setup
	# TODO: Change this name
	$(python) src/dataAnalysis.py	

adhoc:
	# This target is not part of the overall automation, but it can be useful to have something similar
	# to automate some less frequent operation that you might want to run only when strictly necessary
	# (e.g., organize all produced data/analysis and run a notebook for an easier visual verification of obtained results)
	Rscript code/some_adhoc_script.R

clean:
	rm -rf assets
