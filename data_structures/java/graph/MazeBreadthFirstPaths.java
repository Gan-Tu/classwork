import java.util.Observable;
import java.util.LinkedList;
/**
 *  @author Josh Hug
 */

public class MazeBreadthFirstPaths extends MazeExplorer {
    /* Inherits public fields:
    public int[] distTo;
    public int[] edgeTo;
    public boolean[] marked;
    */
    private int s;
    private int t;
    private Maze maze; 
    private LinkedList<Integer> fringe;


    public MazeBreadthFirstPaths(Maze m, int sourceX, int sourceY, int targetX, int targetY) {
        super(m);
        fringe = new LinkedList<Integer>();
        maze = m;
        s = maze.xyTo1D(sourceX, sourceY);
        t = maze.xyTo1D(targetX, targetY);
        distTo[s] = 0;
        edgeTo[s] = s;
    }

    /** Conducts a breadth first search of the maze starting at vertex V. */
    private void bfs(int v) {
        marked[v] = true;
        announce();
        fringe.add(v);
        while (!fringe.isEmpty()) {
            v = fringe.remove();
            for (int w : maze.adj(v)) {
                if (!marked[w]) {
                    edgeTo[w] = v;
                    marked[w] = true;
                    distTo[w] = distTo[v] + 1;
                    announce();
                    fringe.add(w);
                    if (w == t) {
                        return;
                    }   
                }
            }
        }
    }


    @Override
    public void solve() {
        bfs(s);
    }
}

