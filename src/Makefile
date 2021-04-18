# should copile everything including profiling program, but python is interpreted
all:
	
# makes the final package
pack:
	./build.sh

# removes all files, that should not be submitted
clean: 
	
# runs the test for math library
test:
	. venv/bin/activate
	python3 -m unittest -v tests_math_library.py

# generates the documentation
doc:
	doxygen Doxyfile
	
# runs the program
run:
	. venv/bin/activate
	python3 calculator.py

# compiles the program for profiling
profile:

install:
	cp -f ../dist/calculator /usr/bin/ivscalculator
	cp -f icon.png /usr/share/pixmaps/ivscalculator.png
	cp -f calculator.desktop /usr/share/applications/
