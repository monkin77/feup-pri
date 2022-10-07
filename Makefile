# The all target helps automate the whole process: by running `make` from the command line, you can do everything in one go
# You can define further targets that only execute smaller subsets of your data pipeline according to your needs
all: clean collect process analyze

.PHONY: collect processed analysis adhoc

# Step to download dependencies (python)
setup: requirements.txt
	pip install -r requirements.txt

# TODO: Check what the collect depends on
collect:
	# This target is usually associated with data collection
	# This can involved scraping websites, downloading files from servers,
	# or other similar operations.
	# As best practice, ensure that all output data goes to a known location (e.g., here, data/)
	# mkdir -p data/...
	# In our case, the data is already in the desired path

process: collect setup
	# This target is reserved for data processing, which typically includes
	# cleaning and refinement.
	# As best practice, have multiple scripts to perform different (sub)steps
	# You may even opt for several targets for bigger granularity
	# (e.g., a process_cleaning and a process_refinement target)
	# Moreover, ensure that data also goes to a known location for easier analysis
	python src/clean.py

analyze: setup analyzeOriginal analyzeProcessed
	# This target is recommended to isolate all data analysis scripts.
	# Once again, it is recommended to separate different types of analysis between scripts,
	# which may span several languages. Diversity is key here so data can be better understood.
	# TODO: Mkdirs and save stuff inside the folders
	# mkdir -p analysis/...

analyzeOriginal: setup
	python src/analyzeOriginal.py

analyzeProcessed: process
	python src/analyzeWords.py
	python src/analyzeStatistics.py
	python src/dataAnalysis.py

adhoc:
	# This target is not part of the overall automation, but it can be useful to have something similar
	# to automate some less frequent operation that you might want to run only when strictly necessary
	# (e.g., organize all produced data/analysis and run a notebook for an easier visual verification of obtained results)
	Rscript code/some_adhoc_script.R

clean:
	rm -rf data processed analysis
