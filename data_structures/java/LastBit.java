/** Bit-twiddling class.
 *  @author Gan Tu
 */
public class LastBit {

    /** Returns the number N!=0 with all but its last (least significant)
     *  1-bit set to 0.
     *
     *  For example
     *      lastBit(3) == lastBit(7) == lastBit(1145) == 1,
     *      Note that bin(3): '11', bin(7) = '111', so lastBit(3): 1
     *  and
     *      lastBit(4) == lastBit(12) == lastBit(2052) == 4.
     *      Note that bin(12) = '1100', lastBit(12) = '100' = 4
     */
    public static int lastBit(int n) {
        return (n & 1) != 0 ? 1 : lastBit(n >>> 1) << 1;
    }

}
