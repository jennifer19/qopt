#!/bin/bash

function check() {
	if [ "$?" -eq 0 ]; then
		echo OK
	else
		echo Compilation FAILED
		exit 1
	fi
}

# algorithms
cd algorithms
cython --cplus _algorithms.pyx
check
g++ -shared -o _algorithms.so _algorithms.cpp C/qiga.cpp `python-config --cflags`
check
cd ..

# problems
cd problems

cython --cplus _knapsack.pyx
check
g++ -shared -o _knapsack.so C/knapsack.cpp _knapsack.cpp `python-config --cflags`
check
cd CEC2005
#bash genlibs.sh
check
cd ..

cython --cplus _cec2005.pyx
check
g++ -shared -o _cec2005.so _cec2005.cpp `python-config --cflags`
check
cython --cplus _cec2011.pyx
check
g++ -I CEC2011 -shared -o _cec2011.so _cec2011.cpp  CEC2011/mCEC_Function.o  `python-config --cflags` -lCEC2011 -L./CEC2011
check
cython --cplus _func1d.pyx
check
g++ -shared -o _func1d.so _func1d.cpp C/functions1d.cpp -I../contrib/alglib/src  `python-config --cflags` ../contrib/alglib/src/*.o
check

cd ..


echo All well done!
