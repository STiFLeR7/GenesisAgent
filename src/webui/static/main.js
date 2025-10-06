// main.js — React frontend; assumes endpoints:
// POST /chat            -> { prompt_sent, reply, conversation_count }
// GET  /api/top?limit=N -> { ideas: [{content,score}, ...] }
// GET  /api/history     -> { history: [...] }

const { useState, useEffect, useRef } = React;

function LogoSVG({ size = 64 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
      <rect width="96" height="96" rx="16" fill="url(#g)" />
      <defs>
        <linearGradient id="g" x1="0" x2="1">
          <stop offset="0" stopColor="#4fb3ff" stopOpacity="0.09" />
          <stop offset="1" stopColor="#40e0d0" stopOpacity="0.06" />
        </linearGradient>
      </defs>
      <g transform="translate(20,18)">
        <polygon points="16,0 40,8 48,32 32,48 8,40 0,16" fill="#071a2a" opacity="0.8" />
        <circle cx="24" cy="24" r="10" fill="#012431" />
        <rect x="16" y="20" width="16" height="8" rx="3" fill="#7fd9ff" />
        <circle cx="20" cy="24" r="1.8" fill="#012831" />
        <circle cx="28" cy="24" r="1.8" fill="#012831" />
      </g>
    </svg>
  );
}

function App() {
  const [prompt, setPrompt] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [top, setTop] = useState([]);
  const mounted = useRef(false);

  // fetch top and history once and then every 6s
  useEffect(() => {
    mounted.current = true;

    async function fetchAll() {
      try {
        const [topRes, histRes] = await Promise.all([
          fetch("/api/top?limit=6").then(r => r.ok ? r.json() : { ideas: [] }),
          fetch("/api/history").then(r => r.ok ? r.json() : { history: [] })
        ]);
        if (!mounted.current) return;
        setTop(topRes.ideas || []);
        setHistory((histRes.history || []).slice().reverse()); // most recent first
      } catch (err) {
        // silent for now
      }
    }

    fetchAll();
    const t = setInterval(fetchAll, 6000);
    return () => { mounted.current = false; clearInterval(t); };
  }, []);

  async function handleSend(e) {
    if (e) e.preventDefault();
    const userPrompt = prompt.trim();
    if (!userPrompt) return;
    setLoading(true);
    setReply("");

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Cache-Control": "no-store"
        },
        body: JSON.stringify({ prompt: userPrompt }),
      });

      const data = await res.json();
      const promptFromServer = data.prompt_sent || userPrompt;
      setReply(data.reply || `No reply (server echoed: ${promptFromServer})`);

      // refresh lists after call
      const [topRes, histRes] = await Promise.all([
        fetch("/api/top?limit=6").then(r => r.ok ? r.json() : { ideas: [] }),
        fetch("/api/history").then(r => r.ok ? r.json() : { history: [] })
      ]);
      setTop(topRes.ideas || []);
      setHistory((histRes.history || []).slice().reverse());

      // clear input after successful send
      setPrompt("");
    } catch (err) {
      setReply("Error: Unable to reach GenesisAgent backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container-app">
      <div className="card-app">
        <div className="header">
          <div className="logo" aria-hidden><LogoSVG size={72} /></div>
          <div>
            <h1 className="brand">GENESISAGENT</h1>
            <div className="sub">v2.0.0 · Localhost Cognitive Chat</div>
          </div>
        </div>

        <div className="main-grid">
          <div className="left">
            <form className="input-row" onSubmit={handleSend}>
              <input
                id="prompt"
                placeholder="Ask GenesisAgent..."
                value={prompt}
                onChange={e => setPrompt(e.target.value)}
                aria-label="Prompt"
                autoComplete="off"
              />
              <button type="submit" className="btn btn-send" disabled={loading}>
                {loading ? "Thinking..." : "Send"}
              </button>
            </form>

            <div className="response" role="status" aria-live="polite">
              {reply ? (<div dangerouslySetInnerHTML={{__html: reply.replace(/\n/g, "<br/>")}} />)
                     : (<div className="small">Responses appear here.</div>)}
            </div>

            <div className="lower-row">
              <div>
                <div className="small" style={{marginBottom:8}}>Recent prompts</div>
                <div className="badge-list" aria-hidden>
                  {history.length === 0 && <div className="badge-item">No recent prompts</div>}
                  {history.map((h, i) => (
                    <div key={i} className="badge-item" title={h.prompt}>
                      {h.prompt.length > 38 ? h.prompt.slice(0,38) + "…" : h.prompt}
                    </div>
                  ))}
                </div>
              </div>

              <div style={{textAlign:'right'}}>
                <div className="small" style={{marginBottom:8}}>Session</div>
                <div className="small">Interactions: {history.length}</div>
              </div>
            </div>
          </div>

          <aside className="right" aria-label="Top ideas panel">
            <h5>Top ideas</h5>
            <div className="top-list">
              {top.length === 0 && <div className="small">No ideas yet — ask the agent.</div>}
              {top.map((t, i) => (
                <div key={i} className="top-item" title={`${t.content} — score: ${t.score}`}>
                  <div className="top-title">{t.content}</div>
                  <div className="small">{Number(t.score).toFixed(3)}</div>
                </div>
              ))}
            </div>
          </aside>
        </div>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
