 Αρχεία που χρειάζονται
meteo_larissa.py → το κύριο script (Python)

trexe_meteo.bat → για εύκολη εκτέλεση με διπλό κλικ

apoteleismata.txt → δημιουργείται αυτόματα κατά την εκτέλεση

🧱 1. Προαπαιτούμενα
✅ Εγκατεστημένη Python 3 (π.χ. 3.13.x)

✅ Εγκατεστημένος Google Chrome

✅ Κατάλληλο ChromeDriver για την έκδοση Chrome σου

🧰 2. Εγκατάσταση του Selenium
Ανοίγεις cmd και γράφεις:

nginx
Αντιγραφή
Επεξεργασία
pip install selenium
📦 3. Λήψη και ρύθμιση του ChromeDriver
Πήγαινε στο site: https://googlechromelabs.github.io/chrome-for-testing/

Κατέβασε την έκδοση του ChromeDriver που ταιριάζει με την έκδοση του Chrome σου

Κάνε extract το .zip αρχείο

Αντιγράψε το chromedriver.exe στο φάκελο:
C:\drivers\chromedriver.exe

💻 4. Τοποθέτηση αρχείων
Βάλε το meteo_larissa.py και το trexe_meteo.bat στην Επιφάνεια Εργασίας

▶️ 5. Εκτέλεση
Διπλό κλικ στο trexe_meteo.bat
➜ Αυτό θα ανοίξει το τερματικό και θα τρέξει το Python script.

📝 6. Έξοδος αποτελεσμάτων
Το script δημιουργεί αυτόματα αρχείο apoteleismata.txt
με τα δεδομένα που συλλέγει (π.χ. βροχόπτωση, θερμοκρασία κλπ).

🛡️ 7. Προβλήματα με antivirus;
Αν ο υπολογιστής σου διαγράφει το .bat αρχείο, κάνε τα εξής:

Άνοιξε Windows Defender > Ρυθμίσεις προστασίας από ιούς

Πρόσθεσε εξαίρεση στον φάκελο της Επιφάνειας Εργασίας