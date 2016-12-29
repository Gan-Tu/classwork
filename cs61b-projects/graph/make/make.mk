run: class sentinel
	running java files as desired

class: cleanup sentinel
	compiling class files for java

sentinel: cleanup
	creating sentinel file

cleanup: oldfiles
	cleaning up old class files