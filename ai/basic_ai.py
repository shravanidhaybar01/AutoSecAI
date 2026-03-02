def analyze(data):
    if "open_port" in data:
        return "medium risk"
    return "low risk"
