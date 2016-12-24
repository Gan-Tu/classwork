import java.util.Iterator;
import java.util.LinkedList;

public class BST {
    BSTNode root;

    public BST(LinkedList list) {
        root = linkedListToTree(list.iterator(), list.size());
    }

    /** Return a BSTNode with N items recursively from items
     *  supplied by ITER. */
    private BSTNode linkedListToTree (Iterator iter, int n) {
        if (n <= 0) {
            return null;
        }
        BSTNode left = linkedListToTree(iter, n / 2);
        Object root = iter.next();
        BSTNode right = linkedListToTree(iter, n - n / 2 - 1);
        return new BSTNode(root, left, right);
    }

    /** Prints the tree to the console. */
    private void print() {
        print(root, 0);
    }

    private void print(BSTNode node, int d) {
        if (node == null) {
            return;
        }
        for (int i = 0; i < d; i++) {
            System.out.print("  ");
        }
        System.out.println(node.item);
        print(node.left, d + 1);
        print(node.right, d + 1);
    }

    /** Node for BST. */
    static class BSTNode {

        /** Item. */
        Object item;

        /** Left child. */
        BSTNode left;

        /** Right child. */
        BSTNode right;

        /** Constructor. */
        BSTNode(Object i, BSTNode l, BSTNode r) {
            item = i;
            left = l;
            right = r;
        }
    }
}
