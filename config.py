from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv(12380656"))
API_HASH = getenv("d927c13beaaf5110f25c505b7c071273")

BOT_TOKEN = getenv("6724745201:AAEfXNpIpgz8m707TnYZZulNQb4XLDlgi68", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "20000"))

OWNER_ID = int(getenv("6460424107"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5470d1047f4e484b60d0.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c5470d1047f4e484b60d0.jpg")

SESSION = getenv("BQAGiCpKPp-ih0GIbtxw8S90sW3NwJjKPBhWlnarGsP3qA7TUC1tOuWtSXTjsopYJUuDEcjs858lLQ78asuKeLd0FTYpWO1s5p0x0qxWOTJjcLDoLTxiiNC6FNkBqaXgLWsbahoRVgoTuckZImjSD4YDhAx7JyFAMfJDmR6rUc6NmlM5QFiPmVjZHhRBHqrKQrbUS22gPI43Zy0wgHzslpC-gnAgs3BGnflcQ2A3k_acqBHwmHdfcqkuvCHG6pO5Yt0qbZiUz3AODGavUmNsPH4c0adK7kFxEL6e8EHjG0l_f3K44LnOFXtdUlSbXdYEY6DDseZnXUdFWZq1iFqL34uwAAAAAYbc1s0A", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/upscbpscgk")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/quizbys")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6460424107").split()))


FAILED = "https://telegra.ph/file/c5470d1047f4e484b60d0.jpg"
