python = python3
fileid = 1tW7sinuEwo-Fij9j5fgDKdIblgVEcEBf

# The all target helps automate the whole process: by running `make` from the command line, you can do everything in one go
# You can define further targets that only execute smaller subsets of your data pipeline according to your needs
all: setup collect process analyze

# .PHONY: setup processed analysis adhoc


# ========== Setup ==========
setup: requirements.txt assets/

assets/:
	pip install -r requirements.txt
	mkdir -p assets/images

# ========== Collect ==========
collect: setup assets/company_reviews.csv

assets/company_reviews.csv:
	curl -L -o assets/company_reviews.csv "https://drive.google.com/uc?export=download&id=$(fileid)"

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

analyzeStatistics: assets/processed_reviews.csv setup
	$(python) src/analyzeStatistics.py

analyzeWords: assets/processed_reviews.csv setup
	$(python) src/analyzeWords.py

analyzeGraphs: assets/processed_reviews.csv setup
	$(python) src/analyzeGraphs.py

clean:
	rm -rf assets
