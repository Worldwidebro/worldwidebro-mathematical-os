import { useState, useEffect } from 'react'
import axios from 'axios'
import './index.css'

export default function App() {
  const [activeTab, setActiveTab] = useState('overview')
  const [ventures, setVentures] = useState([])
  const [loading, setLoading] = useState(false)
  const [status, setStatus] = useState('Ready')
  const [results, setResults] = useState([])
  const [startTime, setStartTime] = useState(null)

  // Step 1: Test Smithery Tool Router
  const testToolRouter = async () => {
    setLoading(true)
    setStartTime(Date.now())
    setStatus('Testing Tool Router on localhost:9002...')
    try {
      const res = await axios.post('/mcp/execute', {
        tool: 'github_create_repo',
        args: { name: 'test-venture-1', private: true }
      })
      const duration = Date.now() - startTime
      setResults([...results, {
        step: 'Step 1',
        tool: 'github_create_repo',
        result: res.data,
        timestamp: new Date().toLocaleTimeString(),
        duration: `${duration}ms`
      }])
      setStatus('✅ Tool Router works!')
    } catch (err) {
      setStatus(`❌ Tool Router error: ${err.message}`)
    }
    setLoading(false)
  }

  // Step 2: Test Temporal Workflow
  const testWorkflow = async () => {
    setLoading(true)
    setStartTime(Date.now())
    setStatus('Testing Temporal Workflow on localhost:7233...')
    try {
      const res = await axios.post('/temporal/workflows', {
        workflowId: 'venture-launch-1',
        workflowType: 'launchVenture',
        input: { ventureId: 'test-venture-1' }
      })
      const duration = Date.now() - startTime
      setResults([...results, {
        step: 'Step 2',
        tool: 'temporal_workflow',
        result: res.data,
        timestamp: new Date().toLocaleTimeString(),
        duration: `${duration}ms`
      }])
      setStatus('✅ Temporal Workflow works!')
    } catch (err) {
      setStatus(`❌ Temporal error: ${err.message}`)
    }
    setLoading(false)
  }

  // Step 3: Fetch from local Supabase (via tool router)
  const fetchVentures = async () => {
    setLoading(true)
    setStartTime(Date.now())
    setStatus('Fetching ventures from Supabase via MCP...')
    try {
      const res = await axios.post('/mcp/execute', {
        tool: 'supabase_query',
        args: {
          query: 'SELECT * FROM business_ventures LIMIT 10',
          table: 'business_ventures'
        }
      })
      const duration = Date.now() - startTime
      setVentures(res.data)
      setResults([...results, {
        step: 'Step 3',
        tool: 'supabase_query',
        result: { ventures_loaded: res.data.length },
        timestamp: new Date().toLocaleTimeString(),
        duration: `${duration}ms`
      }])
      setStatus(`✅ Loaded ${res.data.length} ventures`)
    } catch (err) {
      setStatus(`❌ Supabase error: ${err.message}`)
    }
    setLoading(false)
  }

  // Step 4: Launch test venture
  const launchTestVenture = async () => {
    setLoading(true)
    setStartTime(Date.now())
    setStatus('Launching test venture with full MCP orchestration...')
    try {
      const res = await axios.post('/mcp/execute', {
        tool: 'launch_venture_workflow',
        args: {
          ventureId: 'test-venture-' + Date.now(),
          steps: ['legal', 'stripe', 'github', 'database']
        }
      })
      const duration = Date.now() - startTime
      setResults([...results, {
        step: 'Step 4',
        tool: 'launch_venture',
        result: res.data,
        timestamp: new Date().toLocaleTimeString(),
        duration: `${duration}ms`
      }])
      setStatus('✅ Venture launch orchestration complete!')
    } catch (err) {
      setStatus(`❌ Launch error: ${err.message}`)
    }
    setLoading(false)
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>🚀 MCP Dashboard</h1>
          <p>Local MCP Testing — Zero deployment cost</p>
        </div>
        <div className="status-indicator">
          <span className={loading ? 'pulsing' : 'active'}></span>
          {status}
        </div>
      </header>

      <div className="container">
        <nav className="tabs">
          <button
            className={`tab ${activeTab === 'overview' ? 'active' : ''}`}
            onClick={() => setActiveTab('overview')}
          >
            Overview
          </button>
          <button
            className={`tab ${activeTab === 'step1' ? 'active' : ''}`}
            onClick={() => setActiveTab('step1')}
          >
            Step 1: Tool Router
          </button>
          <button
            className={`tab ${activeTab === 'step2' ? 'active' : ''}`}
            onClick={() => setActiveTab('step2')}
          >
            Step 2: Temporal
          </button>
          <button
            className={`tab ${activeTab === 'step3' ? 'active' : ''}`}
            onClick={() => setActiveTab('step3')}
          >
            Step 3: Ventures
          </button>
          <button
            className={`tab ${activeTab === 'step4' ? 'active' : ''}`}
            onClick={() => setActiveTab('step4')}
          >
            Step 4: Launch
          </button>
          <button
            className={`tab ${activeTab === 'results' ? 'active' : ''}`}
            onClick={() => setActiveTab('results')}
          >
            Results ({results.length})
          </button>
        </nav>

        {/* Overview Tab */}
        {activeTab === 'overview' && (
          <section className="tab-content">
            <h2>Getting Started</h2>
            <div className="cards-grid">
              <div className="info-card">
                <h3>📍 Step 1: Tool Router</h3>
                <p>Tests Smithery MCP tool routing on localhost:9002</p>
                <button onClick={testToolRouter} disabled={loading} className="primary-btn">
                  Test Tool Router
                </button>
              </div>
              <div className="info-card">
                <h3>⚙️ Step 2: Temporal Workflow</h3>
                <p>Tests venture launch workflow on localhost:7233</p>
                <button onClick={testWorkflow} disabled={loading} className="primary-btn">
                  Test Workflow
                </button>
              </div>
              <div className="info-card">
                <h3>📊 Step 3: Fetch Ventures</h3>
                <p>Loads 10 sample ventures from Supabase</p>
                <button onClick={fetchVentures} disabled={loading} className="primary-btn">
                  Fetch Ventures
                </button>
              </div>
              <div className="info-card">
                <h3>🚀 Step 4: Launch Venture</h3>
                <p>Full orchestration with all MCPs working together</p>
                <button onClick={launchTestVenture} disabled={loading} className="launch-btn">
                  Launch Test Venture
                </button>
              </div>
            </div>
            <div className="info-box">
              <strong>Mode:</strong> Local Testing (no Convex, no Vercel)
            </div>
          </section>
        )}

        {/* Step 1 Tab */}
        {activeTab === 'step1' && (
          <section className="tab-content">
            <h2>Step 1: Tool Router Test</h2>
            <p>Tests tool routing to Smithery MCPs on localhost:9002</p>
            <button onClick={testToolRouter} disabled={loading} className="primary-btn">
              {loading ? 'Testing...' : 'Run Step 1'}
            </button>
            {results.filter(r => r.step === 'Step 1').length > 0 && (
              <div className="result-box">
                <h4>✅ Step 1 Result</h4>
                <pre>{JSON.stringify(results.filter(r => r.step === 'Step 1')[0], null, 2)}</pre>
              </div>
            )}
          </section>
        )}

        {/* Step 2 Tab */}
        {activeTab === 'step2' && (
          <section className="tab-content">
            <h2>Step 2: Temporal Workflow Test</h2>
            <p>Tests workflow orchestration on localhost:7233</p>
            <button onClick={testWorkflow} disabled={loading} className="primary-btn">
              {loading ? 'Testing...' : 'Run Step 2'}
            </button>
            {results.filter(r => r.step === 'Step 2').length > 0 && (
              <div className="result-box">
                <h4>✅ Step 2 Result</h4>
                <pre>{JSON.stringify(results.filter(r => r.step === 'Step 2')[0], null, 2)}</pre>
              </div>
            )}
          </section>
        )}

        {/* Step 3 Tab */}
        {activeTab === 'step3' && (
          <section className="tab-content">
            <h2>Step 3: Fetch Ventures</h2>
            <p>Loads ventures from Supabase via MCP tool router</p>
            <button onClick={fetchVentures} disabled={loading} className="primary-btn">
              {loading ? 'Fetching...' : 'Fetch Ventures'}
            </button>
            {ventures.length > 0 && (
              <div className="ventures-table">
                <h3>Ventures Loaded ({ventures.length})</h3>
                <table>
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Sector</th>
                      <th>Status</th>
                      <th>Health</th>
                    </tr>
                  </thead>
                  <tbody>
                    {ventures.map(v => (
                      <tr key={v.id}>
                        <td>{v.name}</td>
                        <td>{v.sector}</td>
                        <td>{v.status}</td>
                        <td>{v.health_score}%</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </section>
        )}

        {/* Step 4 Tab */}
        {activeTab === 'step4' && (
          <section className="tab-content">
            <h2>Step 4: Launch Test Venture</h2>
            <p>Full MCP orchestration with all components working together</p>
            <button onClick={launchTestVenture} disabled={loading} className="launch-btn">
              {loading ? 'Launching...' : 'Launch Test Venture'}
            </button>
            {results.filter(r => r.step === 'Step 4').length > 0 && (
              <div className="result-box">
                <h4>✅ Step 4 Result</h4>
                <pre>{JSON.stringify(results.filter(r => r.step === 'Step 4')[0], null, 2)}</pre>
              </div>
            )}
          </section>
        )}

        {/* Results Tab */}
        {activeTab === 'results' && (
          <section className="tab-content">
            <h2>Execution Results</h2>
            {results.length === 0 ? (
              <div className="empty-state">
                <p>No results yet. Run the steps above to see results.</p>
              </div>
            ) : (
              <div className="results-list">
                {results.map((r, i) => (
                  <div key={i} className="result-item">
                    <div className="result-header">
                      <h4>{r.step} — {r.tool}</h4>
                      <span className="result-time">{r.timestamp} ({r.duration})</span>
                    </div>
                    <pre>{JSON.stringify(r.result, null, 2)}</pre>
                  </div>
                ))}
              </div>
            )}
          </section>
        )}
      </div>
    </div>
  )
}
