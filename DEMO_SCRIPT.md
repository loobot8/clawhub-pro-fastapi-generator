# FastAPI Generator - Demo Video Script

> **Duration:** ~60 seconds  
> **Target:** Developers building AI/full-stack apps  
> **Key Message:** Stop rebuilding plumbing. Ship faster.

---

## 🎬 HOOK (0:00-0:05)

**[Screen: VS Code with messy project structure]**

**VOICE OVER:**  
*"It's just a FastAPI backend and a Next.js frontend."*

**[Cut to: Developer frustrated, 48 hours later]**

*"Why are CORS, streaming, auth, and deployment all fighting each other?"*

---

## 💢 PROBLEM STATEMENT (0:05-0:15)

**[Screen: Split view - checklist appearing one by one]**

**VOICE OVER:**  
*"Building AI apps means getting the boring stuff right:"*

- ✅ Database setup
- ✅ Token streaming  
- ✅ Background jobs
- ✅ Tracing & observability
- ✅ CORS & auth
- ✅ Deployment-ready structure

**[All items check off simultaneously]**

*"That's two weeks of plumbing... before you write a single AI feature."*

---

## 🚀 LIVE DEMO WALKTHROUGH (0:15-0:50)

### Generate Command (0:15-0:20)

**[Screen: Terminal]**

**VOICE OVER:**  
*"FastAPI Generator fixes this. One command:"*

**[Type command]**
```bash
npx fastapi-generator create my-ai-app
```

**[Shows interactive prompts flying by]**
- Project name: `my-ai-app`
- Template: `AI Full-Stack (LangChain)`
- Database: `PostgreSQL`
- Auth: `JWT`

---

### Show Output Structure (0:20-0:30)

**[Screen: File explorer expanding]**

**VOICE OVER:**  
*"You get a production-ready structure:"*

**[Highlight folders as they're mentioned]**
```
my-ai-app/
├── backend/          # FastAPI + SQLModel
│   ├── api/          # Organized endpoints
│   ├── agents/       # AI agent templates
│   ├── streaming/    # SSE & WebSocket ready
│   └── jobs/         # Background tasks
├── frontend/         # Next.js 14
└── docker-compose.yml # One-command deploy
```

---

### Highlight Key Features (0:30-0:40)

**[Screen: Code editor showing highlighted sections]**

**VOICE OVER:**  
*"Streaming endpoints, agent tools, and tracing—already wired up."*

**[Quick cuts showing:]**
1. **Streaming endpoint** - `/api/chat/stream` (SSE code visible)
2. **Agent integration** - `create_task()` tool function
3. **Observability** - `trace_id` in responses

---

### Run the Generated App (0:40-0:45)

**[Screen: Terminal]**

**VOICE OVER:**  
*"Start everything with one command:"*

**[Type and execute]**
```bash
docker-compose up
```

**[Shows logs flying by, then "Ready" messages]**

```
✓ Database migrated
✓ Backend running on :8000
✓ Frontend running on :3000
```

---

### Show /docs Endpoint (0:45-0:50)

**[Screen: Browser opening to http://localhost:8000/docs]**

**VOICE OVER:**  
*"Interactive API docs. Streaming chat. RAG endpoints. Ready to ship."*

**[Show Swagger UI with endpoints listed:]**
- `POST /api/chat/stream` - Chat with SSE
- `POST /api/tasks` - Create task
- `GET /api/tasks/{id}/trace` - Get trace logs

**[Click "Try it out" on one endpoint - shows it works]**

---

## 📢 CALL TO ACTION (0:50-0:60)

**[Screen: Terminal with final command]**

**VOICE OVER:**  
*"Stop rebuilding auth and CORS. Start building features."*

**[Text appears on screen:]**

```bash
npx fastapi-generator create your-app
```

**[Logo/URL appears:]**

**github.com/yourusername/fastapi-generator**

*"Ship AI apps fast."*

**[Fade to black]**

---

## 🎥 BONUS: Terminal Command Sequence for Screen Recording

Copy-paste this sequence for a smooth recording session:

```bash
# SCENE 1: Setup (Hook/Problem)
# [Show messy project first - pre-recorded or screenshot]

# SCENE 2: Generate Command
npx fastapi-generator create demo-ai-app
# Select options:
# - Template: AI Full-Stack (LangChain)
# - Database: PostgreSQL
# - Auth: JWT

# SCENE 3: Show Structure
cd demo-ai-app
tree -L 2 -I 'node_modules|__pycache__|.venv'
# OR use: ls -la && ls -la backend/ && ls -la frontend/

# SCENE 4: Highlight Key Files (quick cat/bat preview)
bat backend/api/chat.py    # Show streaming endpoint
bat backend/tools.py       # Show agent tools
bat backend/models.py      # Show response models with trace_id

# SCENE 5: Run the App
docker-compose up -d
# Wait for services...
docker-compose logs -f --tail=20

# SCENE 6: Show API Docs in Browser
# Open browser to: http://localhost:8000/docs
# Navigate through Swagger UI
# Execute a POST /api/chat/stream request

# SCENE 7: Cleanup (off-camera)
docker-compose down
cd .. && rm -rf demo-ai-app
```

---

## 🎬 Director's Notes

**Pacing:**
- **Fast cuts** during problem statement (0:05-0:15)
- **Smooth, confident** during demo (0:15-0:50)
- **Punchy** for CTA (0:50-0:60)

**Visuals:**
- Use **syntax highlighting** for code snippets
- **Zoom in** on key file/folder names
- **Highlight** (yellow/green overlay) important lines of code

**Audio:**
- **Upbeat background music** (low volume)
- **Confident, friendly** voiceover tone
- **Pause** briefly (0.5s) before the final CTA

**Typography on Screen:**
- Commands: `Fira Code` or `JetBrains Mono`
- Headings: Bold, sans-serif
- CTA: Large, centered, high contrast

---

## 🎯 Key Pain Points to Emphasize

1. **"Two weeks of plumbing"** - The time tax developers pay
2. **"CORS, auth, streaming fighting each other"** - Integration hell
3. **"Production-ready structure"** - Not a toy, not a tutorial - real code
4. **"Already wired up"** - Zero boilerplate pain
5. **"One command to start"** - Developer happiness

---

**END OF SCRIPT**

*Total estimated length: 58-62 seconds (depending on delivery speed)*
