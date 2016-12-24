import java.util.Iterator;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Stack;

/**
 * Implementation of a BST based String Set.
 * @author Gan Tu
 */
public class BSTStringSet implements Iterable<String> {

    /** Creates a new empty set. */
    public BSTStringSet() {
        root = null;
    }

    /** Returns true iff S is in the string set. */
    public boolean contains(String s) {
        Node last = find(s);
        return last != null && s.equals(last.s);
    }

    /** Adds the string S to the string set. If it is already present in the
      * set, do nothing. */
    public void put(String s) {
        Node last = find(s);
        if (last == null) {
            root = new Node(s);
        } else {
            int c = s.compareTo(last.s);
            if (c < 0) {
                last.left = new Node(s);
            } else if (c > 0) {
                last.right = new Node(s);
            }
        }
    }

    /** Return a list of all members of this set in ascending order. */
    public List<String> asList() {
        ArrayList<String> result = new ArrayList<>();
        for (String label : this) {
            result.add(label);
        }
        return result;
    }

    @Override
    public Iterator<String> iterator() {
        return new BSTIterator(root);
    }

   /** Return an Iterator yielding all my strings that are between L
     *  (inclusive) and U (exclusive) in ascending order. */
    public Iterator<String> iterator(String l, String u) {
        return new BSTRangeIterator(root, l, u);
    }

    /** Return either the node in this BST that contains S, or, if
     *  there is no such node, the node that should be the parent
     *  of that node, or null if neither exists. */
    private Node find(String s) {
        if (root == null) {
            return null;
        }
        Node p;
        p = root;
        while (true) {
            int c = s.compareTo(p.s);
            Node next;
            if (c < 0) {
                next = p.left;
            } else if (c > 0) {
                next = p.right;
            } else {
                return p;
            }
            if (next == null) {
                return p;
            } else {
                p = next;
            }
        }
    }

    /** Represents a single Node of the tree. */
    private static class Node {
        /** String stored in this Node. */
        private String s;
        /** Left child of this Node. */
        private Node left;
        /** Right child of this Node. */
        private Node right;

        /** Creates a Node containing SP. */
        public Node(String sp) {
            s = sp;
        }
    }

    /** An iterator over BSTs. */
    private static class BSTIterator implements Iterator<String> {
        /** Stack of nodes to be delivered.  The values to be delivered
         *  are (a) the label of the top of the stack, then (b)
         *  the labels of the right child of the top of the stack inorder,
         *  then (c) the nodes in the rest of the stack (i.e., the result
         *  of recursively applying this rule to the result of popping
         *  the stack. */
        private Stack<Node> _toDo = new Stack<>();

        /** A new iterator over the labels in NODE. */
        BSTIterator(Node node) {
            addTree(node);
        }

        @Override
        public boolean hasNext() {
            return !_toDo.empty();
        }

        @Override
        public String next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }

            Node node = _toDo.pop();
            addTree(node.right);
            return node.s;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        /** Add the relevant subtrees of the tree rooted at NODE. */
        private void addTree(Node node) {
            while (node != null) {
                _toDo.push(node);
                node = node.left;
            }
        }
    }

     /** An iterator over BSTs from range low to high. */
    private static class BSTRangeIterator implements Iterator<String> {
        /** Stack of nodes to be delivered.  The values to be delivered
         *  in inorder sequence. */
        private Stack<Node> _toDo = new Stack<>();
        /** The lower bound for the strings to deliver. */
        private String _low;
        /** The upper bound for the strings to deliver. */
        private String _high;

        /** A new iterator over the labels in NODE. */
        BSTRangeIterator(Node node, String low, String high) {
            _low = low;
            _high = high; 
        }

        @Override
        public boolean hasNext() {
            return !_toDo.empty();
        }

        @Override
        public String next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            Node node = _toDo.pop();
            addTree(node.right);
            return node.s;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        private void addTree(Node node) {
            while (node != null) {
                if (_low != null && node.s.compareTo(_low) < 0) {
                    node = node.right;
                } else if (_high != null && node.s.compareTo(_high) > 0) {
                    node = node.left;
                } else {
                    _toDo.push(node);
                    node = node.left;
                }
            }
        }
    }

    /** Root node of the tree. */
    private Node root;
}
