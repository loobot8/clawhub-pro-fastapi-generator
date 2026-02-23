# ClawHub Pro: Gumroad Setup Guide

This guide provides everything you need to set up the three core ClawHub Pro products on Gumroad in under 30 minutes.

---

## 🛠️ Global Product Settings
For **all** products, ensure these settings are configured:

1.  **Custom Fields:**
    *   Add a required field: `GitHub Username`
    *   Type: `Text`
2.  **Redirect after purchase:** `https://clawhub.pro/welcome` (or your chosen onboarding page)
3.  **Webhook Setup:** (See the Webhook section at the bottom)

---

## 📦 Product 1: FastAPI Agent Generator
**Price:** $49

### Description
> **Generate Production-Ready FastAPI Agents in Seconds.**
> 
> Stop writing boilerplate. The FastAPI Agent Generator builds the scaffolding for high-performance, AI-native APIs. It handles Pydantic schemas, Dependency Injection, and JWT auth out of the box.
>
> **Features:**
> - Full CRUD scaffolding for any data model.
> - Built-in LangChain integration for agentic workflows.
> - Auto-generated OpenAPI (Swagger) documentation.
> - Optimized for Docker and cloud deployment.
> 
> *Includes 1 year of updates and private GitHub repository access.*

### Pricing Justification
*   **Time Saved:** Replaces ~8 hours of manual coding/setup ($400+ value).
*   **Best Practice:** Ensures architectural consistency across your microservices.
*   **Maintenance:** One-time cost for a tool that scales with your business.

---

## 📦 Product 2: OpenClaw Skill Builder
**Price:** $29

### Description
> **The Essential Toolkit for Custom OpenClaw Skills.**
> 
> Extend your OpenClaw agent with professional-grade skills. This kit includes templates, testing suites, and deployment scripts to make your agent truly your own.
>
> **What’s Inside:**
> - Starter templates for `web_search`, `browser_control`, and `local_execution`.
> - Mock testing framework to debug without burning tokens.
> - CLI tool for rapid skill scaffolding.
> - Comprehensive "Claw-Native" development guide.
>
> *Empower your agent to do more. Fast.*

### Pricing Justification
*   **Entry Point:** Priced for individual developers and hobbyists.
*   **Learning Curve:** Flattens the learning curve for the OpenClaw SDK.
*   **Community:** Access to a dedicated "Builders" Discord channel.

---

## 📦 Product 3: Ultimate Deployment Kit
**Price:** $99

### Description
> **Go Live with Confidence. One Command Deployment.**
> 
> The Ultimate Deployment Kit is for the serious builder. Take your OpenClaw setup from localhost to a secure, scalable production environment.
>
> **Enterprise-Ready Infrastructure:**
> - **Terraform/Pulumi Templates:** AWS, GCP, and DigitalOcean support.
> - **CI/CD Pipelines:** GitHub Actions for automated testing and deployment.
> - **Monitoring Dashboard:** Pre-configured Grafana and Prometheus alerts.
> - **Security Hardening:** Nginx reverse proxy with automated Let’s Encrypt SSL.
>
> *Don't let deployment be your bottleneck. Build, ship, and scale.*

### Pricing Justification
*   **Peace of Mind:** Professional-grade security and uptime configurations.
*   **Scale:** Handles the infrastructure complexity so you don't have to hire a DevOps engineer.
*   **ROI:** Saves days of infrastructure troubleshooting and configuration.

---

## 📧 Delivery Email Template
Set this as the "Receipt" message for all products:

**Subject:** Welcome to ClawHub Pro - {product_name} 🚀

**Body:**
> Hi there!
>
> Thank you for purchasing the **{product_name}**. You've just leveled up your agentic workflow.
>
> **How to access your purchase:**
> 1. **GitHub Access:** We are currently processing your access to the private repository. If you provided your GitHub username (**{GitHub Username}**) during checkout, you will receive an invitation within 5-10 minutes.
> 2. **Documentation:** You can find the QuickStart guide here: [https://docs.clawhub.pro/welcome](https://docs.clawhub.pro/welcome)
> 3. **Support:** Join our private Discord for priority support: [Join Discord](https://discord.gg/yourlink)
>
> If you have any issues or didn't receive your GitHub invite, please reply to this email or reach out to support@clawhub.pro.
>
> Happy Building!
> — The ClawHub Team

---

## ⚡ Webhook Setup (Actionable)
To automate GitHub invites and access management:

1.  Go to your **Gumroad Settings** > **Advanced**.
2.  In the **Ping** field, enter your automation URL (e.g., via Make.com, Zapier, or your own FastAPI backend):
    `https://api.clawhub.pro/webhooks/gumroad`
3.  **Data Structure to Handle:**
    ```json
    {
      "email": "buyer@example.com",
      "seller_id": "...",
      "product_id": "...",
      "custom_fields": {
        "GitHub Username": "loobot"
      },
      "sale_id": "..."
    }
    ```
4.  **Verification:** Gumroad sends a `POST` request. Ensure your endpoint validates the `license_key` or `sale_id` against the Gumroad API before granting repository access.

---

### ✅ 30-Minute Checklist
- [ ] Create 3 Products (Classic type).
- [ ] Paste Descriptions & Prices.
- [ ] Add `GitHub Username` Custom Field (Required).
- [ ] Paste Receipt Email Template.
- [ ] Set Redirect URL.
- [ ] Add Webhook Ping URL.
