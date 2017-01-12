import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.Collections;
import java.util.Comparator;

/** Interval.
 *  @author Gan Tu
  */
public class Intervals {
    /** Assuming that INTERVALS contains two-element arrays of integers,
     *  <x,y> with x <= y, representing intervals of ints, this returns the
     *  total length covered by the union of the intervals. */
    public static int coveredLength(List<int[]> intervals) {
        ArrayList<int[]> sorted = new ArrayList<int[]>(intervals);
        Collections.sort(sorted, new Comparator<int[]>() {
            public int compare(int[] a1, int[] a2) {
                if (a1.length == 0 && a2.length == 0) {
                    return 0;
                } else if (a1.length == 0 ){
                    return -1;
                } else if (a2.length == 0 ){
                    return 1;
                }
                return a1[0] -  a2[0];
            }
        });
        Stack<int[]> combined = new Stack<int[]>();
        for (int[] arr: intervals) {
            if (combined.isEmpty()) {
                combined.add(arr);
                continue;
            }
            int[] last = combined.peek();
            if (last[0] > arr[1] || last[1] < arr[0]) {
                combined.add(arr);
            } else {
                last[0] = Math.min(last[0], arr[0]);
                last[1] = Math.max(last[1], arr[1]);
            }
        }
        int count = 0;
        while (!combined.isEmpty()) {
            int[] last = combined.pop();
            count += last[1] - last[0];
        } 
        return count;
    }

}
