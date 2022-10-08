python = python3
fileid = 1tW7sinuEwo-Fij9j5fgDKdIblgVEcEBf

# ========== Default Rule ==========
all: setup collect process analyze


# ========== Setup ==========
setup: requirements.txt assets/

assets/:
	pip install -r requirements.txt
	mkdir -p assets/images


# ========== Collect ==========
collect: setup assets/company_reviews.csv

assets/company_reviews.csv: setup
	curl -L -o assets/company_reviews.csv "https://drive.google.com/uc?export=download&id=$(fileid)"


# ========== Process ==========
process: collect assets/cleaned_reviews.csv assets/processed_reviews.csv assets/processed_reviews.json

assets/cleaned_reviews.csv: assets/company_reviews.csv
	$(python) src/clean.py

assets/processed_reviews.csv: assets/cleaned_reviews.csv
	$(python) src/processing.py
assets/processed_reviews.json: assets/cleaned_reviews.csv
	$(python) src/processing.py


# ========== Analyze ==========
analyze: analyzeOriginal analyzeStatistics analyzeWords analyzeGraphs

analyzeOriginal: assets/company_reviews.csv
	$(python) src/analyzeOriginal.py

analyzeStatistics: assets/processed_reviews.csv
	$(python) src/analyzeStatistics.py

analyzeWords: assets/processed_reviews.csv
	$(python) src/analyzeWords.py

analyzeGraphs: assets/processed_reviews.csv
	$(python) src/analyzeGraphs.py


# ========== Clean ==========
clean:
	rm -rf assets
