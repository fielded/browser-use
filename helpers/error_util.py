import os
from datetime import datetime

def log_error_to_markdown(error, context="" , filename="agent_error_log.md"):
    markdown_dir = "agent_logs"
    os.makedirs(markdown_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    filepath = os.path.join(markdown_dir, filename)

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"## ❌ Error at {timestamp}\n")
        if context:
            f.write(f"**Context:** {context}\n\n")
        f.write(f"**Error Message:**\n```\n{error}\n```\n\n")

    print(f"📄 Error logged to {filepath}")
