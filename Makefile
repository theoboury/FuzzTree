dependencies:
	conda install -y -c conda-forge -c bioconda 'infrared' viennarna jupyter matplotlib pip networkx graphviz pygraphviz
	pip install varnaapi
	pip install func_timeout
tests:
	python3 Launcher.py --pattern 53kink_turninto3NVI.pickle --target 3NVI.nxpickle --usevarna True

tests_no_varna:
	python3 Launcher.py --pattern 53kink_turninto3NVI.pickle --target 3NVI.nxpickle
	
clean:
	rm -f *.png
	rm -R -f __pycache__
	rm -f *.pdf

