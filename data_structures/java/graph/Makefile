wSHELL = bash

JFLAGS = -g -Xlint:unchecked -encoding utf8

SRCS = $(wildcard *.java)

CLASSES = $(SRCS:.java=.class)

# Tell make that these are not really files.
.PHONY: clean default style check 

default: compile

compile: $(CLASSES)

$(CLASSES): sentinel

sentinel: $(SRCS)
	javac $(JFLAGS) $(SRCS)
	touch $@

# Find and remove all *~ and *.class files.
clean:
	$(RM) sentinel *.class *~ 

astar: compile
	java AStarDemo

bfs: compile
	java BreadthFirstDemo

dfs: compile
	java DepthFirstDemo

trivial: compile
	java TrivialMazeExplorerDemo

cycle: compile
	java CyclesDemo