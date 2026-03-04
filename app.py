from ai.basic_ai import analyze
from security.basic_scan import scan
from automation.auto_action import auto_action

def main():
    target = "demo_target"
    issues = scan(target)
    risk = analyze(issues)
    action = auto_action(risk)
    print("Action:", action)
    print("Target:", target)
    print("Issues:", issues)
    print("Risk:", risk)

if __name__ == "__main__":
    main()
