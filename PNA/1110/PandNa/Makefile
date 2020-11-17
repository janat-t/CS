CC = cc
CXX = cc
CFLAGS = -g

MAIN = polint
#OBJS = polint.o nrutil.o main.o
OBJS = polint.o nrutil.o polint_main.o
INC = nrutil.h nr.h
LIBS = 

all: $(MAIN)
$(OBJS): $(INC)

$(MAIN): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBS) -lm  -o $@

clean:
	rm $(OBJS)
#############
SUFFIXES: .cc .cpp .c .o

.c.o:
	$(CC) $(CFLAGS) -c $<

.cpp.o:
	$(CXX) $(CFLAGS) -c $<

.cc.o:
	$(CXX) $(CFLAGS) -c $<
