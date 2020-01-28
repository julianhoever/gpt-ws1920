/*
import sys

n = int(sys.argv[1])
summe = "1"
ergebnis = 1

for i in range(2, n+1):
    summe += " + " + str(i)
    ergebnis += i

print(summe, "=", ergebnis)
*/

public class NatSum {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        String summe = "1";
        int ergebnis = 1;

        for (int i = 2; i < n+1; i++) {
            summe += " + " + i;
            ergebnis += i;
        }

        System.out.println(summe + " = " + ergebnis);
    }
}
