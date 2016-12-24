import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

/** Interval.
 *  @author Gan Tu
  */
public class Intervals {
    /** Assuming that INTERVALS contains two-element arrays of integers,
     *  <x,y> with x <= y, representing intervals of ints, this returns the
     *  total length covered by the union of the intervals. */
    public static int coveredLength(List<int[]> intervals) {
        ArrayList<int[]> sorted = sortIntervals(intervals);
        ArrayList<int[]> filtered = new ArrayList<int[]>();
        for (int[] interval : sorted) {
            if (filtered.size() <= 0) {
                filtered.add(interval);
                continue;
            }
            int[] last = filtered.get(filtered.size() - 1);
            if (last[0] > interval[1] || last[1] < interval[0]) {
                filtered.add(interval);
            } else {
                last[0] = Math.min(last[0], interval[0]);
                last[1] = Math.max(last[1], interval[1]);
            }
        }
        int count = 0;
        for (int[] interval : filtered) {
            count += interval[1] - interval[0];
        }
        return count;
    }

    /** Return a sorted list of INTERVALS based on its starting value. */
    private static ArrayList<int[]> sortIntervals(List<int[]> intervals) {
        ArrayList<int[]> sorted = new ArrayList<int[]>(intervals);
        mergesort(sorted, 0, sorted.size() - 1);
        return sorted;
    }

    /** Merge sort an ARRAY from I to K. */
    private static void mergesort(ArrayList<int[]> array, int i, int k) {
        int lower = i, upper = k;
        int middle = (lower + upper) / 2;
        if (lower < upper) {
            mergesort(array, lower, middle);
            mergesort(array, middle + 1, upper);
            mergeParts(array, lower, middle, upper);
        }
    }

    /** Merge sorted parts from LOWER to MIDDLE and
     *  from MIDDLE to UPPER of ARRAY. */
    private static void mergeParts(ArrayList<int[]> array, int lower,
                                int middle, int upper) {

        ArrayList<int[]> temp = new ArrayList<int[]>();
        int i = lower, j = middle + 1;
        while (i <= middle && j <= upper) {
            if (array.get(i)[0] <= array.get(j)[0]) {
                temp.add(array.get(i));
                i++;
            } else {
                temp.add(array.get(j));
                j++;
            }
        }
        int remainder = i;
        if (i > middle) {
            remainder = j;
        }
        while (temp.size() < upper - lower + 1) {
            temp.add(array.get(remainder));
            remainder++;
        }
        for (i = 0; i < temp.size(); i++, lower++) {
            array.set(lower, temp.get(i));
        }
    }

}
