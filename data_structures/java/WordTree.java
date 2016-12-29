import java.util.HashMap;
import java.util.Stack;

/** A data structure for quick existence check for strings. 
 *  @author Gan Tu
 */
public class WordTree{

    /** The root node for this tree. */
    private Node root;

    public WordTree() {
        root = new Node();
    }

    /** Add the list of STRS to this tree. */
    public void add(String... strs) {
        for (String str : strs) {
            add(str);
        }
    }

    /** Add the word STR to this tree. */
    public void add(String str) {
        Node node = this.root;
        for (int i = 0; i < str.length(); i++) {
            node = node.getChild(str.charAt(i));
        }
        node.getChild('*'); // indicates the end of a string
    }

    /** Return the node at the end of STR, or null if STR is not in the tree. */
    private Node lastNode(String str) {
        Node node = this.root;
        for (int i = 0; i < str.length(); i++) {
            node = node.findChild(str.charAt(i));
            if (node == null) {
                return null;
            }
        }
        return node;
    }

    /** Return true iff the tree has prefix of STR. */
    public boolean hasPrefix(String prefix) {
        return lastNode(prefix) != null;
    }

    /** Return true iff the tree has exactly the word STR, not just the prefix. */
    public boolean hasWord(String str) {
        Node node = lastNode(str);
        return node != null && node.findChild('*') != null;
    }

    @FunctionalInterface
    interface Fill<T, F> {
        void fill(T s, F m);
    }

    /** Return the number of words that start with prefix STR. */
    public int countPrefix(String prefix) {
        Node node = lastNode(prefix);
        if (node == null) {
            return 0;
        }
        Stack<Node> nodes = new Stack<Node>();
        HashMap<Character, Node> map = node.children();
        for (Character c: map.keySet()) {
            nodes.add(map.get(c));
        }
        Node temp = null;
        int count = 0;
        while (!nodes.isEmpty()) {
            temp = nodes.pop();
            if (temp.isData('*')) {
                count += 1;
                continue;
            }
            map = temp.children();
            for (Character c: map.keySet()) {
                nodes.add(map.get(c));
            }
        }
        return count;
    }

    /** The class for Node. */
    private class Node {
        /** The value in this node. */
        private Character data;
        /** A mapping of character to corresponding child nodes. */
        private HashMap<Character, Node> child;

        /** A Node containing no data. */
        public Node() {
            this(null);
        }

        /** A Node containing data. */
        public Node(Character data) {
            this.data = data;
            this.child = new HashMap<Character, Node>();
        }

        /** Return the child containing C in this node. If no child has
         *  C as the value, return and add a new child to this node. */
        public Node getChild(Character c) {
            Node node = findChild(c);
            if (node == null) {
                child.put(c, new Node(c));
            }
            return findChild(c);
        }

        /** Return the child containing C in this node. If no child has
         *  C as the value, return null. */
        public Node findChild(Character c) {
            return child.get(c);
        }

        /** Return the number of child nodes I have, one level down. */
        public int childSize() {
            return child.size();
        }

        /** Return all child nodes. */
        public HashMap<Character, Node> children() {
            return child;
        }

        /** Return true iff my data is DATA. */
        public boolean isData(Character data) {
            return this.data.equals(data);
        }

    }
}