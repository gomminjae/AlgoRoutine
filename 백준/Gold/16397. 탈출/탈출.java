import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node1 {
    int n, time;

    Node1(int n, int time) {
        this.n = n;
        this.time = time;
    }
}

public class Main {

    static int n, t, g;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        n = Integer.parseInt(s.split(" ")[0]);
        t = Integer.parseInt(s.split(" ")[1]);
        g = Integer.parseInt(s.split(" ")[2]);

        if (g > 99999) {
            System.out.println("ANG");
            return;
        }

        int ans = bfs();
        if (ans == -1 || ans == Integer.MAX_VALUE) {
            System.out.println("ANG");
        } else {
            System.out.println(ans);
        }
    }

    public static int bfs() {
        Queue<Node1> q = new LinkedList<>();
        boolean[] visited = new boolean[100000]; // 방문 여부 확인을 위한 배열 추가
        q.add(new Node1(n, 0));
        visited[n] = true; // 시작 노드 방문 표시
        int ans = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            Node1 node = q.poll();
            int num = node.n;
            int time = node.time;
            if (num == g) {
                return time; // 목적지 도착 시 즉시 반환
            }
            if (time >= t) {
                continue;
            }

            // +1 연산
            int nn = num + 1;
            if (nn <= 99999 && !visited[nn]) {
                visited[nn] = true;
                q.add(new Node1(nn, time + 1));
            }

            // *2 후 1 빼기 연산
            if (num > 0) {
                nn = num * 2;
                if (nn <= 99999) {
                    // 1 빼기 연산
                    nn = nn - (int)Math.pow(10, (int)Math.log10(nn));
                    if (nn >= 0 && nn <= 99999 && !visited[nn]) {
                        visited[nn] = true;
                        q.add(new Node1(nn, time + 1));
                    }
                }
            }
        }
        return -1; // 도달 불가 시 -1 반환
    }
}
