/*
import sys

n = int(sys.argv[1])
rechnung = "1"
ergebnis = 1

for i in range(2, n+1):
    rechnung += " + " + str(i)
    ergebnis += i
    
print(rechnung, "=", ergebnis)
*/

public class NatSum {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        String rechnung = "1";
        int ergebnis = 1;

        for (int i = 2; i < n+1; i++) {
            rechnung += " + " + i;
            ergebnis += i;
        }
        
        System.out.println(rechnung + " = " + ergebnis);
    }
}
