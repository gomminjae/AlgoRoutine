import java.util.Scanner;

class Coordinator {
    int x;
    int y;

    Coordinator(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {

    static int n, m, l, k;
    static Coordinator[] stars;

    public static int countStarsInTrampoline(int left, int bottom) {
        int count = 0;

        for (Coordinator star : stars) {
            if (star.x >= left && star.x <= left + l && star.y >= bottom && star.y <= bottom + l) {
                count++;
            }
        }

        return count;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        l = sc.nextInt();
        k = sc.nextInt();

        stars = new Coordinator[k];

        for (int i = 0; i < k; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            stars[i] = new Coordinator(x, y);
        }

        int maxStars = 0;

        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                Coordinator star1 = stars[i];
                Coordinator star2 = stars[j];

                // 트램펄린의 왼쪽 아래 모서리를 별똥별 위치에 맞추는 경우
                maxStars = Math.max(maxStars, countStarsInTrampoline(star1.x, star2.y));
                // 트램펄린의 오른쪽 위 모서리를 별똥별 위치에 맞추는 경우
                maxStars = Math.max(maxStars, countStarsInTrampoline(star1.x - l, star2.y - l));
                // 트램펄린의 오른쪽 아래 모서리를 별똥별 위치에 맞추는 경우
                maxStars = Math.max(maxStars, countStarsInTrampoline(star1.x - l, star2.y));
                // 트램펄린의 왼쪽 위 모서리를 별똥별 위치에 맞추는 경우
                maxStars = Math.max(maxStars, countStarsInTrampoline(star1.x, star2.y - l));
            }
        }

        System.out.println(k - maxStars);
    }
}