import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "7958954191"

API = f"https://api.telegram.org/bot{TOKEN}"


def send_alert(message):

    keyboard = {
        "inline_keyboard": [
            [
                {"text": "🔍 Scan Again", "callback_data": "scan"},
                {"text": "🧹 Safe Cleanup", "callback_data": "cleanup"}
            ],
            [
                {"text": "📄 Log Analysis", "callback_data": "logs"}
            ]
        ]
    }

    response = requests.post(
        f"{API}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message,
            "reply_markup": str(keyboard).replace("'", '"')
        },
        timeout=10
    )

    if response.ok:
        print("✅ Alert sent!")
    else:
        print("❌ Failed to send alert.")


def find_large_logs():

    print("🔎 Searching for large log files...")

    results = []

    for root, dirs, files in os.walk("D:\\"):

        for file in files:

            if not file.lower().endswith(".log"):
                continue

            path = os.path.join(root, file)

            try:
                size = os.path.getsize(path)

                # Consider logs larger than 10 MB
                if size >= 10 * 1024 * 1024:
                    results.append((path, size))

            except (PermissionError, OSError):
                continue

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:5]


def format_size(size):

    if size >= 1024 ** 3:
        return f"{size / (1024 ** 3):.2f} GB"

    if size >= 1024 ** 2:
        return f"{size / (1024 ** 2):.2f} MB"

    return f"{size / 1024:.2f} KB"


def handle_buttons():

    print("🤖 Button listener started...")

    offset = None

    while True:

        response = requests.get(
            f"{API}/getUpdates",
            params={
                "offset": offset,
                "timeout": 20
            },
            timeout=30
        )

        data = response.json()

        for update in data.get("result", []):

            offset = update["update_id"] + 1

            if "callback_query" not in update:
                continue

            callback = update["callback_query"]

            callback_id = callback["id"]
            action = callback["data"]
            chat_id = callback["message"]["chat"]["id"]

            requests.post(
                f"{API}/answerCallbackQuery",
                data={
                    "callback_query_id": callback_id
                }
            )

            # SCAN
            if action == "scan":

                message = (
                    "🔍 SCAN REQUESTED\n\n"
                    "Fresh storage scan requested.\n"
                    "No files will be deleted.\n\n"
                    "🛡️ Safe monitoring mode"
                )

            # SAFE CLEANUP
            elif action == "cleanup":

                message = (
                    "🧹 SAFE CLEANUP\n\n"
                    "Cleanup request received.\n\n"
                    "⚠️ DiskAlert will only consider "
                    "verified safe cache/log candidates.\n\n"
                    "🚫 Database files and system binaries "
                    "will never be touched."
                )

            # LOG ANALYSIS
            elif action == "logs":

                print("📄 Starting log analysis...")

                logs = find_large_logs()

                if not logs:

                    message = (
                        "📄 LOG ANALYSIS\n\n"
                        "No log files larger than 10 MB "
                        "were found on D:.\n\n"
                        "✅ No action required."
                    )

                else:

                    message = (
                        "📄 LOG ANALYSIS\n\n"
                        "Large log files detected:\n\n"
                    )

                    for index, (path, size) in enumerate(logs, 1):

                        message += (
                            f"{index}. {os.path.basename(path)}\n"
                            f"   📦 {format_size(size)}\n"
                            f"   📍 {path}\n\n"
                        )

                    message += (
                        "⚠️ Review these files before cleanup.\n"
                        "🛡️ No files were deleted."
                    )

            else:

                message = "Unknown action."

            requests.post(
                f"{API}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": message
                },
                timeout=10
            )

            print(f"✅ Button clicked: {action}")


if __name__ == "__main__":

    print("================================")
    print("   DISKALERT TELEGRAM BOT")
    print("================================")

    handle_buttons()