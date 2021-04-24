PACK_DIR = "xlogin01_xlogin02_xlogin03_xlogin04"

# builds distributable package using pyinstaller
all:
	./build.sh

# makes the final package
pack:
	rm -rf ../../$(PACK_DIR)
	rm -rf ../../$(PACK_DIR).zip
	zip -cvf archive


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

# should compile profiling program
profile:

install:
	./install.sh

uninstall:
	./uninstall.sh
