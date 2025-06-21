import requests
import json
import time

WEBHOOK_URL = "https://himanshu1199.app.n8n.cloud/webhook-test/ghostchecker"  

# ✅ Load the transcript
def load_transcript():
    try:
        with open("sample_500_lines_transcript.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("❌ transcript file not found. Please download and place 'sample_500_lines_transcript.txt' next to this script.")
        exit()

# ✅ Trigger n8n workflow with transcript
def trigger_workflow(transcript):
    print("📤 Sending transcript to GhostChecker AI via n8n webhook...")
    payload = {"text": transcript}

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
    except requests.exceptions.RequestException as e:
        print("🚨 Network error:", e)
        return

    if response.status_code == 200:
        print("✅ Successfully triggered the workflow.")
        try:
            result = response.json()
            print("\n📋 AI Classification Result:")
            print(json.dumps(result, indent=2))
        except:
            print("📝 No structured JSON response. Possibly logged to Google Sheets only.")
            print(response.text)
    else:
        print(f"❌ Failed with status code {response.status_code}")
        print("Error:", response.text)

# ✅ Run the full demo
def run_demo():
    print("🎬 Starting GhostChecker AI Demo...\n")
    time.sleep(1)
    transcript = load_transcript()
    print("📄 Loaded 500-line transcript.\n")
    print(transcript[:1000] + "\n... [truncated] ...\n")  # Show a preview
    time.sleep(2)
    trigger_workflow(transcript)
    print("\n✅ Done. Check Google Sheet for final logged attendance.")

# 🚀 Main
if __name__ == "__main__":
    run_demo()
