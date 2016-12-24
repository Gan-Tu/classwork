/** Scheme-like pairs that can be used to form a list of
 *  integers.
 *  @author Gan Tu
 */
public class IntList {
    /** First element of list. */
    public int head;
    /** Remaining elements of list. */
    public IntList tail;

    /** A List with head HEAD0 and tail TAIL0. */
    public IntList(int head0, IntList tail0) {
        head = head0;
        tail = tail0;
    }

    /** A List with null tail, and head = 0. */
    public IntList() {
        this (0, null);
    }

    /** Returns a new IntList containing the ints in ARGS. */
    public static IntList list(Integer ... args) {
        IntList sentinel = new IntList(0, null);

        IntList p;
        p = sentinel;
        for (Integer x : args) {
            p.tail = new IntList(x, null);
            p = p.tail;
        }
        return sentinel.tail;
    }

    /** Returns a new IntList containing the ints A. */
    public static IntList list(int[] A) {
        IntList sentinel = new IntList(0, null);

        IntList p;
        p = sentinel;
        for (int x : A) {
            p.tail = new IntList(x, null);
            p = p.tail;
        }
        return sentinel.tail;
    }


    /** Returns true iff X is an IntList or int[] containing the same
     *  sequence of ints as THIS. */
    public boolean equals(Object x) {
        if (x instanceof IntList) {
            IntList L = (IntList) x;
            IntList p;
            for (p = this; p != null && L != null; p = p.tail, L = L.tail) {
                if (p.head != L.head) {
                    return false;
                }
            }
            if (p == null && L == null) {
                return true;
            }
        } else if (x instanceof int[]) {
            int[] A = (int[]) x;
            IntList p;
            int i;
            for (i = 0, p = this; i < A.length && p != null;
                 i += 1, p = p.tail) {
                if (A[i] != p.head) {
                    return false;
                }
            }
            if (i == A.length && p == null) {
                return true;
            }
        }
        return false;
    }

    /** Return an integer value such that if x1 and x2 represent two
     *  IntLists that represent identical sequences of ints, then
     *  x1.hashCode() == x2.hashCode().  (Any class that overrides
     *  equals should override this method,) */
    @Override
    public int hashCode() {
        return head;
    }

    /** Returns a new IntList containing the ints in ARGS. You are not
     * expected to read or understand this method. */
    public static IntList list(Integer ... args) {
        IntList result, p;

        if (args.length > 0) {
            result = new IntList(args[0], null);
        } else {
            return null;
        }

        int k;
        for (k = 1, p = result; k < args.length; k += 1, p = p.tail) {
            p.tail = new IntList(args[k], null);
        }
        return result;
    }

    /** If a cycle exists in A, return an integer equal to
     *  the item number of the location where the cycle is detected.
     *  If there is no cycle, returns 0. */
    private int detectCycles(IntList A) {
        IntList tortoise;
        IntList hare;

        if (A == null) {
            return 0;
        }

        tortoise = hare = A;

        for (int cnt = 0;; cnt += 1) {
            cnt += 1;
            if (hare.tail != null) {
                hare = hare.tail.tail;
            } else {
                return 0;
            }

            tortoise = tortoise.tail;

            if (tortoise == null || hare == null) {
                return 0;
            }

            if (hare == tortoise) {
                return cnt;
            }
        }
    }

    /** Return a printable representation of an IntList. */
    @Override
    public String toString() {
        Formatter out = new Formatter();
        String sep;
        sep = "[";
        int cycleLocation = detectCycles(this);
        int cnt;

        cnt = 0;
        for (IntList p = this; p != null; p = p.tail) {
            out.format("%s%d", sep, p.head);
            sep = ", ";

            cnt += 1;
            if (cnt > cycleLocation && cycleLocation > 0) {
                out.format("... (cycle)");
                break;
            }
        }
        out.format("]");
        return out.toString();
    }
}
