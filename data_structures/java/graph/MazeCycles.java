import java.util.Observable;
/** 
 *  @author Josh Hug
 */

public class MazeCycles extends MazeExplorer {
    /* Inherits public fields: 
    public int[] distTo;
    public int[] edgeTo;
    public boolean[] marked;
    */
    private boolean cycleFound;
    private Maze maze;
    private int cycleNode;
    private boolean cycleDraw;

    public MazeCycles(Maze m) {
        super(m);
        maze = m;
        cycleFound = false;
        cycleDraw = false;
    }

    private void findCycle(int v, int parent) {
        marked[v] = true;
        announce();

        if (cycleFound) {
            return;
        }

        for (int w : maze.adj(v)) {
            if (!marked[w] && !cycleFound) {
                marked[w] = true;
                findCycle(w, v);
                if (cycleFound && cycleDraw) {
                    if (cycleNode == w) {
                        cycleDraw = false;
                        return;
                    }
                    edgeTo[w] = v;
                    announce();
                    return;
                }                
            } else if (marked[w] && w != parent && !cycleFound) {
                cycleFound = true;
                edgeTo[w] = v;
                cycleNode = w;
                cycleDraw = true;
                announce();
                return;
            }
        }
    }

    @Override
    public void solve() {
        for (int i = 0; i < marked.length && !cycleFound; i++) {
            if (!marked[i]) {
                cycleNode = -1;
                findCycle(i, i);   
            }
        }
    }
} 

