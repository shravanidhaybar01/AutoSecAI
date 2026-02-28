from ai.basic_ai import analyze
from security.basic_scan import scan

def main():
    target = "demo_target"
    issues = scan(target)
    risk = analyze(issues)
    print("Target:", target)
    print("Issues:", issues)
    print("Risk:", risk)

if __name__ == "__main__":
    main()
