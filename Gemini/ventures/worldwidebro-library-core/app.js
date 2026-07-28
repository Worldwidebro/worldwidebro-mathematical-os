// Toast helper forwarding to parent window if inside an iframe, otherwise fallback to local logging
const Toast = {
  info(title, msg) {
    if (window.parent && window.parent.Toast) {
      window.parent.Toast.info(title, msg);
    } else {
      console.log(`[Toast Info] ${title}: ${msg}`);
    }
  },
  success(title, msg) {
    if (window.parent && window.parent.Toast) {
      window.parent.Toast.success(title, msg);
    } else {
      console.log(`[Toast Success] ${title}: ${msg}`);
    }
  },
  error(title, msg) {
    if (window.parent && window.parent.Toast) {
      window.parent.Toast.error(title, msg);
    } else {
      console.log(`[Toast Error] ${title}: ${msg}`);
    }
  }
};

// Helper function to escape HTML to prevent XSS
function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}

// Controller logic
const LibraryOS = {
  currentView: 'dashboard',
  switchView(viewName) {
    document.querySelectorAll('.lo-view').forEach(v => v.classList.remove('active'));
    document.querySelectorAll('.lo-sidebar-item').forEach(s => s.classList.remove('active'));
    
    const targetView = document.getElementById('lo-view-' + viewName);
    const targetBtn = document.querySelector(`[data-lo-view="${viewName}"]`);
    if (targetView) targetView.classList.add('active');
    if (targetBtn) targetBtn.classList.add('active');
    
    this.currentView = viewName;
    if (viewName === 'analytics') setTimeout(() => this.initAnalyticsCharts(), 100);
    if (viewName === 'finance') setTimeout(() => this.initFinanceCharts(), 100);
  },
  
  sendAiMessage(msg) {
    if (!msg.trim()) return;
    const input = document.getElementById('lo-aiInput');
    if (input) input.value = '';
    
    const chatMessages = document.getElementById('lo-chatMessages');
    if (!chatMessages) return;
    
    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble flex gap-3 justify-end';
    userBubble.innerHTML = `
      <div class="glass-light rounded-2xl rounded-tr-sm p-4 max-w-2xl text-xs">
        <p class="text-xs text-gray-200">${escapeHtml(msg)}</p>
      </div>
      <div class="w-8 h-8 rounded-lg gradient-bg flex items-center justify-center flex-shrink-0 text-xs font-bold text-white">
        EM
      </div>
    `;
    chatMessages.appendChild(userBubble);
    
    const typingBubble = document.createElement('div');
    typingBubble.className = 'chat-bubble flex gap-3';
    typingBubble.id = 'lo-typing-indicator';
    typingBubble.innerHTML = `
      <div class="w-8 h-8 rounded-lg gradient-purple flex items-center justify-center flex-shrink-0">
        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
      </div>
      <div class="glass-light rounded-2xl rounded-tl-sm p-3">
        <div class="flex gap-1">
          <div class="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce" style="animation-delay: 0ms"></div>
          <div class="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce" style="animation-delay: 150ms"></div>
          <div class="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce" style="animation-delay: 300ms"></div>
        </div>
      </div>
    `;
    chatMessages.appendChild(typingBubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    setTimeout(() => {
      typingBubble.remove();
      const responses = {
        'Find books on Roman architecture published after 2018': `I found <strong>12 books</strong> on Roman architecture published after 2018. Here are the top matches:\n\n📚 <strong>"The Architecture of Knowledge"</strong> by E. Mansfield (2024) — Available, 12 copies\n📚 <strong>"Architecture Monograph"</strong> by L. Mies (2023) — Available, 6 copies\n📚 <strong>"Roman Engineering Marvels"</strong> by P. Vitruvius Jr. (2022) — 2 copies available\n\nWould you like me to place holds on any of these, or generate a detailed comparison?`,
        'What are the top 5 most borrowed books this month?': `Here are the <strong>top 5 most borrowed books</strong> this month:\n\n🥇 <strong>"The Architecture of Knowledge"</strong> — 247 borrows\n🥈 <strong>"Farhns: Beyond Stars"</strong> — 198 borrows\n🥉 <strong>"Contemporary Visions"</strong> — 176 borrows\n4️⃣ <strong>"Botanica Antiqua"</strong> — 142 borrows\n5️⃣ <strong>"Breightial Chronicles"</strong> — 128 borrows\n\nTotal circulation is up <strong>15.7%</strong> compared to last month.`,
        'Show me overdue items and suggest actions': `You currently have <strong>47 overdue items</strong>. Here's my analysis:\n\n⚠️ <strong>3 items require immediate action:</strong>\n• Marcus Johnson — "Botanica Antiqua" (9 days overdue)\n• Jennifer Lopez — "Digital Privacy" (12 days overdue)\n• Robert Taylor — "Climate Science" (15 days overdue)\n\n<strong>Suggested actions:</strong>\n1. Send automated reminders to all 47 members\n2. Apply late fees ($0.25/day) — estimated $847 total\n3. For items >14 days overdue, consider lost item protocol\n\nWould you like me to send reminders now?`
      };
      
      const response = responses[msg] || `I've processed your request. Based on the Worldwidebro Library Core database, I found relevant information that matches your query. The system has analyzed 24,581 catalog items and can provide detailed insights on circulation, member activity, and collection management.\n\nWould you like me to dive deeper into any specific aspect?`;
      
      const aiBubble = document.createElement('div');
      aiBubble.className = 'chat-bubble flex gap-3 text-xs';
      aiBubble.innerHTML = `
        <div class="w-8 h-8 rounded-lg gradient-purple flex items-center justify-center flex-shrink-0">
          <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
        </div>
        <div class="glass-light rounded-2xl rounded-tl-sm p-4 max-w-2xl">
          <p class="text-sm text-gray-200 whitespace-pre-line">${response}</p>
        </div>
      `;
      chatMessages.appendChild(aiBubble);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 1200);
  },
  
  initDashboardCharts() {
    const ctx1 = document.getElementById('lo-circulationChart');
    if (ctx1) {
      if (ctx1.chart) ctx1.chart.destroy();
      ctx1.chart = new Chart(ctx1, {
        type: 'line',
        data: {
          labels: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          datasets: [{
            label: 'Borrowed',
            data: [1800, 2100, 2400, 2200, 1900, 2300, 2600, 2800, 2500, 2700, 2900, 2847],
            borderColor: '#f59e0b',
            backgroundColor: 'rgba(245, 158, 11, 0.1)',
            tension: 0.4,
            fill: true
          }, {
            label: 'Returned',
            data: [1700, 2000, 2300, 2100, 1800, 2200, 2500, 2700, 2400, 2600, 2800, 2750],
            borderColor: '#8b5cf6',
            backgroundColor: 'rgba(139, 92, 246, 0.1)',
            tension: 0.4,
            fill: true
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: '#9ca3af' } } },
          scales: {
            x: { ticks: { color: '#6b7280' }, grid: { color: 'rgba(255,255,255,0.05)' } },
            y: { ticks: { color: '#6b7280' }, grid: { color: 'rgba(255,255,255,0.05)' } }
          }
        }
      });
    }
    
    const ctx2 = document.getElementById('lo-collectionChart');
    if (ctx2) {
      if (ctx2.chart) ctx2.chart.destroy();
      ctx2.chart = new Chart(ctx2, {
        type: 'doughnut',
        data: {
          labels: ['Print Books', 'Digital', 'Audio', 'Other'],
          datasets: [{
            data: [62, 24, 9, 5],
            backgroundColor: ['#f59e0b', '#8b5cf6', '#3b82f6', '#10b981'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '70%',
          plugins: { legend: { display: false } }
        }
      });
    }
  },
  
  initAnalyticsCharts() {
    const ctx1 = document.getElementById('lo-branchChart');
    if (ctx1) {
      if (ctx1.chart) ctx1.chart.destroy();
      ctx1.chart = new Chart(ctx1, {
        type: 'bar',
        data: {
          labels: ['Central', 'Westside', 'University', 'Eastside', 'North'],
          datasets: [{
            label: 'Borrows',
            data: [2847, 1421, 1983, 892, 1247],
            backgroundColor: ['#f59e0b', '#8b5cf6', '#3b82f6', '#10b981', '#f43f5e'],
            borderRadius: 8
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { ticks: { color: '#6b7280' }, grid: { display: false } },
            y: { ticks: { color: '#6b7280' }, grid: { color: 'rgba(255,255,255,0.05)' } }
          }
        }
      });
    }
    
    const ctx2 = document.getElementById('lo-memberChart');
    if (ctx2) {
      if (ctx2.chart) ctx2.chart.destroy();
      ctx2.chart = new Chart(ctx2, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          datasets: [{
            label: 'New Members',
            data: [89, 102, 124, 98, 147, 118, 127],
            borderColor: '#10b981',
            backgroundColor: 'rgba(16, 185, 129, 0.1)',
            tension: 0.4,
            fill: true
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: '#9ca3af' } } },
          scales: {
            x: { ticks: { color: '#6b7280' }, grid: { display: false } },
            y: { ticks: { color: '#6b7280' }, grid: { color: 'rgba(255,255,255,0.05)' } }
          }
        }
      });
    }
  },
  
  initFinanceCharts() {
    const ctx = document.getElementById('lo-revenueChart');
    if (ctx) {
      if (ctx.chart) ctx.chart.destroy();
      ctx.chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['Memberships', 'Fines', 'Donations', 'Grants', 'Services', 'Events'],
          datasets: [{
            data: [42, 18, 22, 12, 4, 2],
            backgroundColor: ['#f59e0b', '#f43f5e', '#8b5cf6', '#3b82f6', '#10b981', '#ec4899'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '65%',
          plugins: { legend: { position: 'bottom', labels: { color: '#9ca3af', padding: 15 } } }
        }
      });
    }
  }
};

// Start application and render charts immediately
document.addEventListener('DOMContentLoaded', () => {
  LibraryOS.initDashboardCharts();
});
