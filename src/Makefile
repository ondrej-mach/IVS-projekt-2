PACK_NAME=xlogin01_xlogin02_xlogin03_xlogin04
PACK_DIR=../../$(PACK_NAME)

# builds package using pyinstaller
# python does not compile, so at least it does something
all: ../dist/calculator

../dist/calculator:
	./build.sh

# makes the final package
pack: clean
	# delete previous temporary files - if there are any
	rm -rf $(PACK_DIR)
	rm -rf $(PACK_DIR).zip

	mkdir $(PACK_DIR)
	mkdir $(PACK_DIR)/doc


	mkdir $(PACK_DIR)/install

	mkdir $(PACK_DIR)/repo
	cp -r .. $(PACK_DIR)/repo

	cd ../../ && zip -r $(PACK_NAME).zip $(PACK_NAME)

	rm -rf $(PACK_DIR) # remove the temporary directory

# removes all files, that should not be submitted
clean:
	rm -rf venv/
	rm -rf html/
	rm -rf latex/

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
