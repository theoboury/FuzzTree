dependencies:
	conda install -y -c conda-forge -c bioconda 'infrared' viennarna jupyter matplotlib pip networkx graphviz pygraphviz
	pip install varnaapi
	pip install func_timeout
tests:
	python3 Launcher.py --task create_patterns_and_targets
	python Launcher.py --task launch_sanity_test

tests_no_varna:
	python3 Launcher.py --task create_patterns_and_targets
	python Launcher.py --task launch_sanity_test_novarna

clean:
	rm -f *.png
	rm -R -f __pycache__
	rm -f *.pdf
	rm -f carte1.csv
	rm -f eRMSD_distribution.csv
		
clean_all:
	rm -f *.png
	rm -R -f __pycache__
	rm -f *.pdf
	rm -f carte1.csv
	rm -f eRMSD_distribution.csv
	rm ALLkinkturnpattern 
	rm ALLkinkturntarget
	rm ALLkinkturnpatternwithgaps
	rm ALLkinkturntargetwithgaps
