# FastAPI Pro Generator - Customer Delivery

## Automated Delivery Email Template (Gumroad)

**Subject:** Your ClawHub Pro FastAPI Generator Access

```
Hi {buyer_name},

Thanks for purchasing the FastAPI Production Generator! 🚀

Here's everything you need:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 INSTANT ACCESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **GitHub Repository Access**
   I'll manually add your GitHub username to the private repo within 24 hours.
   
   Please reply with your GitHub username: _______________
   
   Repo URL (once added): https://github.com/loobot8/clawhub-pro-fastapi-generator

2. **Documentation**
   Full docs in the repo README.md
   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 QUICK START
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Once you have access:

# Clone the repo
git clone https://github.com/loobot8/clawhub-pro-fastapi-generator.git
cd clawhub-pro-fastapi-generator

# Generate your first app
python3 generators/fastapi-pro-generator/scripts/generate.py \
  --name my-api \
  --features auth,db \
  --output ~/projects

# Done! You now have a production-ready FastAPI app

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 WHAT'S INCLUDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Production code generator
✅ Auth (JWT + RBAC)
✅ Database (async SQLAlchemy)
✅ Redis caching
✅ Stripe integration
✅ Docker + CI/CD
✅ Test suite structure
✅ Lifetime updates
✅ Priority email support

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🆘 SUPPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Questions? Just reply to this email.

I typically respond within 24 hours.

GitHub Issues: https://github.com/loobot8/clawhub-pro-fastapi-generator/issues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Happy building!

– OpenClaw Team
hey@clawhubpro.com

P.S. Built something cool with this? Share it with me! I love seeing what people create.
```

---

## Manual Delivery Process (First 10 Customers)

### When Gumroad notifies of sale:

1. **Get customer info**
   - Email from Gumroad notification
   - Check if they provided GitHub username in purchase form

2. **Send welcome email** (copy from template above)

3. **GitHub access**
   ```bash
   # Add collaborator to repo
   gh api repos/loobot8/clawhub-pro-fastapi-generator/collaborators/{username} \
     --method PUT \
     -f permission=pull
   ```

4. **Follow up in 48h** if no GitHub username provided

5. **Log in spreadsheet**
   - Date
   - Customer email
   - GitHub username
   - Status (pending/granted)
   - Notes

---

## Automated Delivery (After 10 sales)

### Option 1: Gumroad Workflow + GitHub API

```python
# webhook_handler.py
import hmac
import hashlib
from flask import Flask, request
import requests
import os

app = Flask(__name__)

GUMROAD_WEBHOOK_SECRET = os.getenv("GUMROAD_WEBHOOK_SECRET")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "loobot8/clawhub-pro-fastapi-generator"

@app.route("/gumroad-webhook", methods=["POST"])
def handle_purchase():
    # Verify Gumroad signature
    signature = request.headers.get("X-Gumroad-Signature")
    body = request.get_data()
    
    expected = hmac.new(
        GUMROAD_WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    
    if signature != expected:
        return "Invalid signature", 401
    
    data = request.json
    
    if data.get("sale"):
        buyer_email = data["sale"]["email"]
        buyer_name = data["sale"]["full_name"]
        github_username = data["sale"].get("custom_fields", {}).get("github_username")
        
        if github_username:
            # Add to GitHub repo
            grant_access(github_username)
            
            # Send confirmation email via Gumroad API
            send_confirmation(buyer_email, github_username)
        else:
            # Send email requesting GitHub username
            send_github_request(buyer_email, buyer_name)
    
    return "OK", 200

def grant_access(username):
    url = f"https://api.github.com/repos/{REPO}/collaborators/{username}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    requests.put(url, headers=headers, json={"permission": "pull"})

def send_confirmation(email, github_username):
    # Use Gumroad API or email service
    pass

if __name__ == "__main__":
    app.run(port=5000)
```

Deploy this webhook handler on:
- Railway (free tier)
- Fly.io
- Vercel (serverless)

### Option 2: Zapier (No Code)

1. Trigger: Gumroad → New Sale
2. Filter: Check if GitHub username provided
3. Action: HTTP Request to GitHub API (add collaborator)
4. Action: Email via Gmail/SendGrid (confirmation)

---

## License Key System (Future Enhancement)

For now: GitHub access IS the license key.

Future: Generate unique keys, store in database, validate in CLI.

---

## Refund Policy

30-day money-back guarantee, no questions asked.

Process:
1. Refund via Gumroad
2. Revoke GitHub access
3. Send exit survey (optional)

---

## Support Channels

1. **Email** (primary): hey@clawhubpro.com
2. **GitHub Issues** (bugs/features)
3. **Discord** (future: create #clawhub-pro channel in OpenClaw Discord)

Response SLA:
- Bug reports: 24 hours
- Feature requests: 48 hours
- General questions: 48 hours

---

## Customer Success Metrics

Track:
- Time from purchase to first generation
- Number of apps generated per customer
- Feature usage (which features are most popular)
- Support tickets per customer
- NPS score

Survey after 7 days:
"What did you build with ClawHub Pro?"
"What would make this 10x better?"
"Would you recommend to a colleague?"

---

**Status:** Manual delivery for MVP, automate after 10 sales
