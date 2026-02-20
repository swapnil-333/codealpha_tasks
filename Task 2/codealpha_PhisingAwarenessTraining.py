import time
import random

score = 0

phishing_cases = [
    {
        "msg": "Bank Alert: Your account is suspended. Click to verify immediately.",
        "type": "phishing"
    },
    {
        "msg": "Microsoft: Unusual sign-in activity detected on your account.",
        "type": "legit"
    },
    {
        "msg": "Congratulations! You won a free smartphone. Claim now!",
        "type": "phishing"
    },
    {
        "msg": "Amazon: Your package has been delivered successfully.",
        "type": "legit"
    },
    {
        "msg": "PayPal Security: Verify your identity to avoid account limitation.",
        "type": "phishing"
    }
]

def banner():
    print("\n==============================")
    print("  PHISHING AWARENESS TRAINING ")
    print("==============================\n")

def education():
    print("📘 What is Phishing?")
    print("Phishing is a cyber attack where fake messages trick users into sharing sensitive information.\n")

    print("🚩 Warning Signs:")
    print("- Urgent requests")
    print("- Unknown senders")
    print("- Fake links")
    print("- Requests for passwords/OTP\n")

def quiz():
    global score
    random.shuffle(phishing_cases)

    for i, case in enumerate(phishing_cases, 1):
        print(f"\nScenario {i}:")
        print(case["msg"])
        answer = input("Is this phishing or legit? ").lower()

        if answer == case["type"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! This was", case["type"])

def summary():
    print("\n========= TRAINING RESULT =========")
    print(f"Score: {score}/{len(phishing_cases)}")

    if score == len(phishing_cases):
        print("🏆 Excellent awareness level!")
    elif score >= 3:
        print("👍 Good — stay cautious online!")
    else:
        print("⚠ You need more cybersecurity awareness training.")

def main():
    banner()
    education()
    quiz()
    summary()

main()