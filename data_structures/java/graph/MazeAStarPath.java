import java.util.Observable;
import java.util.PriorityQueue;
import java.util.Comparator;
/**
 *  @author Josh Hug
 */

public class MazeAStarPath extends MazeExplorer {
    private int s;
    private int t;
    private boolean targetFound = false;
    private Maze maze;
    private PriorityQueue<Integer> fringe;

    public MazeAStarPath(Maze m, int sourceX, int sourceY, int targetX, int targetY) {
        super(m);
        maze = m;
        s = maze.xyTo1D(sourceX, sourceY);
        t = maze.xyTo1D(targetX, targetY);
        distTo[s] = 0;
        edgeTo[s] = s;
        fringe = new PriorityQueue<Integer>(new VertexComparator(t));
    }

    private class VertexComparator implements Comparator<Integer> {
        private int t;

        public VertexComparator(int t) {
            this.t = t;
        }

        @Override
        public int compare(Integer a, Integer k) {
            int a_value = h(a) + distTo[a], k_value = h(k) + distTo[k];
            if (a_value == k_value) {
                return 0;
            } else if (a_value > k_value) {
                return 1;
            } else {
                return -1;
            }
        }
    }

    /** Estimate of the distance from v to the target. */
    private int h(Integer v) {
        return Math.abs(maze.toX(v) - maze.toX(t)) + Math.abs(maze.toY(v) - maze.toY(t));
    }

    /** Performs an astar search from vertex s. */
    private void astar(int v) {
        marked[v] = true;
        announce();
        fringe.add(v);
        while (!fringe.isEmpty()) {
            v = fringe.remove();
            marked[v] = true;
            announce();
            for (int w : maze.adj(v)) {
                if (!marked[w]) {
                    distTo[w] = distTo[v] + 1;
                    edgeTo[w] = v;
                    fringe.add(w);
                    if (w == t) {
                        marked[w] = true;
                        announce();
                        return;
                    }   
                }
            }
        }
    }

    @Override
    public void solve() {
        astar(s);
    }

}

