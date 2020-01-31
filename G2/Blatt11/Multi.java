public class Multi {
    public static void main(String[] args) {
        String wort = args[0];
        int anzahl = Integer.parseInt(args[1]);
        
        String ausgabe = "";

        for (int i = 0; i < anzahl; i++) {
            ausgabe += wort;
        }

        System.out.println(ausgabe);
    }
}
