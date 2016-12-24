import java.util.AbstractSequentialList;
import java.util.ListIterator;

/** A list of objects of type T with a fixed maximum list size.
 *  @author Gan Tu
 */
public class CompactLinkedList<T> extends AbstractSequentialList<T> {

    /* The class declaration above illustrates how to define a
     * polymorphic (paramterized) class, so that you can write, e.g.,
     * CompactLinkedList<String> or CompactLinkedList<Integer>.  For
     * technical reasons, one cannot write the obvious "new T[maxSize]"
     * in Java, but have to use 'new Object[]' and coerce the result to
     * T[].  This causes an annoying warning, which we suppress here. */

    /** A new, empty list whose maximum size is MAXSIZE. */
    @SuppressWarnings("unchecked")
    CompactLinkedList(int maxSize) {
        _data = (T[]) new Object[maxSize];
        _link = new int[maxSize];
        _size = 0;
        _first = _last = -1;
    }

    @Override
    public int size() {
        return _size;
    }

    @Override
    public ListIterator<T> listIterator(int k) {
        return new CompactIterator(k);
    }

    /** Iterator over my elements.  Does not support remove() or set(). */
    private class CompactIterator implements ListIterator<T> {
        /** A ListIterator that is initially positioned at item #K in
         *  my List, where 0 <= K < size(). */

        CompactIterator(int k) {
            /* After initializing instance variables of this iterator, we
             * find item #K by working from whichever end of the list is
             * closest.
             *
             * Since CompactIterator is an inner class, we can reference
             * instance variables of the containing CompactLinkedList
             * by their names (e.g., _first). */
            if (k < _size - k) {
                _prev = -1;
                _next = _nextIndex = _first;
                for (int i = 0; i < k; i += 1) {
                    next();
                }
            } else {
                _prev = _last;
                _next = _nextIndex = -1;
                for (int i = _size; i > k; i -= 1) {
                    previous();
                }
            }
        }

        @Override
        public boolean hasNext() {
            return _next != -1;
        }

        @Override
        public T next() {
            if (hasNext()) {
                _nextIndex += 1;
                T data = _data[_next];
                int temp = _prev;
                _prev = _next;
                _next = _link[_next] ^ temp;
                return data;
            } else {
                return null;
            }
        }

        @Override
        public int nextIndex() {
            return _nextIndex;
        }

        @Override
        public boolean hasPrevious() {
            return _prev != -1;
        }

        @Override
        public T previous() {
            if (hasPrevious()) {
                _nextIndex -= 1;
                T data = _data[_prev];
                int curr = _next;
                _next = _prev;
                _prev = _link[_next] ^ curr;
                return data;
            } else {
                return null;
            }
        }

        @Override
        public int previousIndex() {
            return _nextIndex - 1;
        }

        @Override
        /** Insert OBJ immediately before the element that would be
         *  returned by next() (if any) and after the element that would
         *  be returned by previous() (if any).  Throws an
         *  IllegalStateException if the list is currently full. */
        public void add(T obj) {
            /* Implementation note: because we don't allow removal from
             * this list, it's easy to find an unused element of _data
             * and _link to "allocate" to hold OBJ.  Just use the value
             * of _size. An implementation that allows removals would
             * require some other way of finding indices that are
             * no longer in use (for example, that were being used, but were
             * then removed).  For this exercise, you needn't bother. */
            if (_size >= _data.length) {
                throw new IllegalStateException();
            } else {
                _data[_size] = obj;
                if (_prev == -1) {
                    _first = _size;
                } else {
                    _link[_prev] = _link[_prev] ^ _next ^ _size;
                }
                if (_next == -1) {
                    _last = _size;
                } else {
                    _link[_next] = _link[_next] ^ _prev ^ _size;
                }
                _link[_size] = _prev ^ _next;
                _prev = _size;
                _size += 1;
            }
        }


        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        @Override
        public void set(T newVal) {
            throw new UnsupportedOperationException();
        }

        /** Sequence number of next item to be returned by next()
         *  (0 for the first item in the list, 1 for the second,
         *  etc. */
        private int _nextIndex;
        /** Index in the _data and _link arrays of the next item to be
         *  delivered by next(), or -1 if none. */
        private int _next;
        /** Index in the _data and _link arrays of the item before the
         *  the one a _next, or -1 if none. */
        private int _prev;

    }

    /** The items stored in this list. */
    private T[] _data;
    /** Current size of this list. */
    private int _size;
    /** Indices of the first and last element of this list in _DATA. */
    private int _first, _last;
    /** Exclusive ors of the next and previous elements for each item in
     *  this list.  Undefined for */
    private int[] _link;
}
