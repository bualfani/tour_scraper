import requests
from bs4 import BeautifulSoup
import smtplib

# Website URL to scrape for tour dates
url = "https://www.example.com/tours"

# Email parameters
sender_email = "your_email@example.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"

# Email message
subject = "New tour dates available"
body = "New tour dates have been announced on the band's website: " + url

# Scrape website for tour dates
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tour_dates = soup.find_all("div", {"class": "tour-date"})

# Check if there are new tour dates
if len(tour_dates) > 0:
    # Send email notification
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(sender_email, recipient_email, message.encode("utf-8"))
        print("Email sent.")
else:
    print("No new tour dates found.")