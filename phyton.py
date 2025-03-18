import streamlit as st
import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, comment, recipient_email, smtp_user, smtp_pass):
    """
    Verschickt eine E-Mail mit den uebergebenen Informationen.
    :param sender_email: Absender-E-Mail (wird im Formular eingegeben)
    :param comment: Kommentartext (wird im Formular eingegeben)
    :param recipient_email: Empfaenger-E-Mail (private E-Mail-Adresse)
    :param smtp_user: Benutzername fuer den SMTP-Login
    :param smtp_pass: Passwort fuer den SMTP-Login
    """
    subject = "Neue Formular-Eingabe"
    body = f"E-Mail-Adresse: {sender_email}\nKommentar:\n{comment}"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    
    try:
        # Beispiel: SMTP-Server von Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Fehler beim Versenden der E-Mail:", e)
        return False

def main():
    st.title("Kontaktformular")
    
    # Formularblock
    with st.form("contact_form"):
        email = st.text_input("Deine E-Mail-Adresse")
        comment = st.text_area("Kommentar")
        submitted = st.form_submit_button("Senden")
        
        if submitted:
            # Hier muessen die echten Login-Daten eingetragen werden
            smtp_user = "sarahhotz48@gmail.com"
            smtp_pass = "dnxl qhxj zorq ndof"
            recipient_email = "sarahhotz48@gmail.com"
            
            success = send_email(email, comment, recipient_email, smtp_user, smtp_pass)
            
            if success:
                st.success("Vielen Dank! Deine Nachricht wurde erfolgreich gesendet.")
            else:
                st.error("Fehler beim Versenden der Nachricht. Bitte versuche es spaeter erneut.")

if __name__ == "__main__":
    main()

