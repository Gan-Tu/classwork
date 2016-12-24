import java.util.LinkedList;
import java.util.List;
import java.util.TreeSet;
import java.util.ArrayList;

class ECHashStringSet extends BSTStringSet {
    
    public ECHashStringSet() {
        _table = null;
        _load = 0;
        _count = 0;
    }

    /** Adds the string S to the string set. If it is already present in the
      * set, do nothing. */
    public void put(String s) {
        if (_count == 0) {
            resize();
        }
        int hash = s.hashCode();
        int index = hash % _table.length;
        if (index < 0) {
            index = hash & 0x7fffffff % _table.length;
        }
        LinkedString list = _table[index];
        if (list != null) {
            list.add(s);
        } else {
            _table[index] = new LinkedString();
            _table[index].add(s);
        }
        _count++;
        _load = _count / _table.length;
        if (_load >= 5) {
            resize();
            _load = _count / _table.length;
        }
    }

    /** Returns true iff S is in the string set. */
    public boolean contains(String s) {
        if (_load <= 0) {
            return false;
        }
        int hash = s.hashCode();
        int index = hash % _table.length;
        if (index < 0) {
            index = hash & 0x7fffffff % _table.length;
        }
        LinkedString list = _table[index];
        for (int i = 0; i < list.size(); i++) {
            if (list != null && list.get(i).equals(s)) {
                return true;
            }
        }
        return false;
    }

    /** Return a list of all members of this set in ascending order. */
    public List<String> asList() {
        TreeSet<String> set = new TreeSet<String>();
        List<String>  members = this.asListRandom();
        for (String str: members) {
            set.add(str);
        }
        members = new ArrayList<String>();
        for (String str: set) {
            members.add(str);
        }
        return members;
    }

    /** Return a list of all members of this set in random order. */
    public List<String> asListRandom() {
        ArrayList<String>  members = new ArrayList<String> ();
        if (_table == null) {
            return members;
        }
        for (int i = 0; i < _table.length; i++) {
            LinkedString list = _table[i];
            if (list == null) {
                continue;
            }
            for (int j = 0; j < list.size(); j++) {
                members.add(list.get(j));
            }
        }
        return members;
    }

    /** Resize the table. */
    private void resize() {
        if (_table == null) {
            _table = new LinkedString[1];
            _table[0] = new LinkedString();
        } else {
            int size = _count * 5;
            List<String> items = this.asListRandom();
            _table = new LinkedString[size];
            for (String str : items) {
                put(str);
            }
        }
    }

    private class LinkedString extends LinkedList<String> {}

    /** Load Factor. */
    private double _load;
    /** Item Count. */
    private int _count;
    /** Hash Table. */
    private LinkedString[] _table;

}
