import javafx.scene.chart.BubbleChart;
import java.util.ArrayList;

/** A Generic heap class. Unlike Java's priority queue, this heap doesn't just
  * store Comparable objects. Instead, it can store any type of object
  * (represented by type T) and an associated priority value.
  * @author CS61B Staff & Gan Tu */
public class ArrayHeap<T> {

	/* An ArrayList that stores the nodes in this binary heap. */
	private ArrayList<Node> contents;

	/* A constructor that initializes an empty ArrayHeap. */
	public ArrayHeap() {
		contents = new ArrayList<>();
		contents.add(null);
	}

	/* Returns the node at index INDEX. */
	private Node getNode(int index) {
		if (index >= contents.size()) {
			return null;
		} else {
			return contents.get(index);
		}
	}

	private void setNode(int index, Node n) {
		// In the case that the ArrayList is not big enough
		// add null elements until it is the right size
		while (index >= contents.size()) {
			contents.add(null);
		}
		contents.set(index, n);
	}

	/* Swap the nodes at the two indices. */
	private void swap(int index1, int index2) {
		Node node1 = getNode(index1);
		Node node2 = getNode(index2);
		this.contents.set(index1, node2);
		this.contents.set(index2, node1);
	}

	/* Prints out the heap sideways. Use for debugging. */
	@Override
	public String toString() {
		return toStringHelper(1, "");
	}

	/* Recursive helper method for toString. */
	private String toStringHelper(int index, String soFar) {
		if (getNode(index) == null) {
			return "";
		} else {
			String toReturn = "";
			int rightChild = getRightOf(index);
			toReturn += toStringHelper(rightChild, "        " + soFar);
			if (getNode(rightChild) != null) {
				toReturn += soFar + "    /";
			}
			toReturn += "\n" + soFar + getNode(index) + "\n";
			int leftChild = getLeftOf(index);
			if (getNode(leftChild) != null) {
				toReturn += soFar + "    \\";
			}
			toReturn += toStringHelper(leftChild, "        " + soFar);
			return toReturn;
		}
	}

	/* A Node class that stores items and their associated priorities. */
	public class Node {
		private T item;
		private double priority;

		private Node(T item, double priority) {
			this.item = item;
			this.priority = priority;
		}

		public T item(){
			return this.item;
		}

		public double priority() {
			return this.priority;
		}

		@Override
		public String toString() {
			return this.item.toString() + ", " + this.priority;
		}
	}

	/* Returns the index of the node to the left of the node at i. */
	private int getLeftOf(int i) {
		return 2 * i;
	}

	/* Returns the index of the node to the right of the node at i. */
	private int getRightOf(int i) {
		return getLeftOf(i) + 1;
	}

	/* Returns the index of the node that is the parent of the node at i. */
	private int getParentOf(int i) {
		return i / 2;
	}

	/* Adds the given node as a left child of the node at the given index. */
	private void setLeft(int index, Node n) {
		setNode(getLeftOf(index), n);
	}

	/* Adds the given node as the right child of the node at the given index. */
	private void setRight(int index, Node n) {
		setNode(getRightOf(index), n);
	}

	/** Returns the index of the node with smaller priority. Precondition
	 * not both nodes are null. */
	private int min(int index1, int index2) {
		Node n1 = getNode(index1);
		Node n2 = getNode(index2);
        if (n1 == null){
            return index2;
        } else if (n2 == null) {
            return index1;
        } else if (n1.priority() < n2.priority()) {
            return index1;
        } else {
            return index2;
        }
	}

	/* Returns the Node with the smallest priority value, but does not remove it
	 * from the heap. */
	public Node peek() {
		return getNode(1);
	}

	/* Bubbles up the node currently at the given index. */
	private void bubbleUp(int index) {
		if (getNode(index) != null && index > 1) {
			int parentIndex = getParentOf(index);
			double parent = getNode(parentIndex).priority();
			double curr = getNode(index).priority();
			if (parent > curr) {
				swap(index, parentIndex);
				bubbleUp(parentIndex);
			}
		}
	}

	/* Bubbles down the node currently at the given index. */
	private void bubbleDown(int index) {
		if (index >= 1 && getNode(index) != null) {
			int left = getLeftOf(index);
			int right = getRightOf(index);
			double curr = getNode(index).priority();
			if (!(getNode(left) == null && getNode(right) == null)) {
				int childIndex = min(left, right);
				double child = getNode(childIndex).priority();
				if (child < curr) {
					swap(index, childIndex);
					bubbleDown(childIndex);
				}
			}
		}
	}

	/* Inserts an item with the given priority value. Same as enqueue, or offer. */
	public void insert(T item, double priority) {
		Node node = new Node(item, priority);
       setNode(contents.size(), node);
       bubbleUp(contents.size());
	}

	/* Returns the Node with the smallest priority value, and removes it from
	 * the heap. Same as dequeue, or poll. */
	public Node removeMin() {
		Node smallest = peek();
		setNode(1, null);
		int last = contents.size() - 1;
		swap(1, last);
		bubbleDown(1);
		contents.remove(contents.size() - 1);
		return smallest;
	}

	/* Changes the node in this heap with the given item to have the given
	 * priority. You can assume the heap will not have two nodes with the same
	 * item. Check for item equality with .equals(), not == */
	public void changePriority(T item, double priority) {
		Node node = new Node(item, priority);
		for (int i = 1; i < contents.size(); i += 1) {
			if (getNode(i).item().equals(item)) {
				setNode(i, node);
				bubbleUp(i);
				bubbleDown(i);
				break;
			}
		}
	}

}
