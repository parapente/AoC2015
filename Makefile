CXX=c++
LIBCXX=-lstdc++
OPT=-O3 -pedantic -Wall -Wfatal-errors
STD=-std=c++14
PROGS=1a.c++ 1b.c++ 2a.c++ 2b.c++ 3a.c++ 3b.c++ 4a.c++ 4b.c++

all: $(PROGS)

1a.c++: 1a.cc
	$(CXX) 1a.cc $(LIBCXX) $(OPT) $(STD) -o 1a.c++

1b.c++: 1b.cc
	$(CXX) 1b.cc $(LIBCXX) $(OPT) $(STD) -o 1b.c++

2a.c++: 2a.cc
	$(CXX) 2a.cc $(LIBCXX) $(OPT) $(STD) -o 2a.c++

2b.c++: 2b.cc
	$(CXX) 2b.cc $(LIBCXX) $(OPT) $(STD) -o 2b.c++

3a.c++: 3a.cc
	$(CXX) 3a.cc $(LIBCXX) $(OPT) $(STD) -o 3a.c++

3b.c++: 3b.cc
	$(CXX) 3b.cc $(LIBCXX) $(OPT) $(STD) -o 3b.c++

4a.c++: 4a.cc
	$(CXX) 4a.cc $(LIBCXX) $(OPT) $(STD) -lcrypto -o 4a.c++

4b.c++: 4b.cc
	$(CXX) 4b.cc $(LIBCXX) $(OPT) $(STD) -lcrypto -o 4b.c++

clean:
	rm -f *.c++

