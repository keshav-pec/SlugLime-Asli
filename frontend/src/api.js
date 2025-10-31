// Use environment variable or default to localhost:5000
const API = import.meta.env.VITE_API_URL || "http://localhost:5000";

export async function createReport(formData) {
  try {
    const r = await fetch(`${API}/api/v1/reports`, {
      method: "POST",
      body: formData
      // Note: Do NOT set Content-Type header when sending FormData
      // Browser will automatically set it with the correct boundary
    });
    if (!r.ok) {
      // Try to get error details from response
      const errText = await r.text();
      throw new Error(`Create failed: ${r.status} - ${errText}`);
    }
    return r.json();
  } catch (error) {
    if (error.message.includes('fetch')) {
      throw new Error('Cannot connect to server. Make sure the backend is running on http://localhost:5000');
    }
    throw error;
  }
}

export async function fetchReport(ticket, code) {
  try {
    const r = await fetch(`${API}/api/v1/reports/${ticket}?code=${encodeURIComponent(code)}`);
    if (!r.ok) throw new Error(`Fetch failed: ${r.status}`);
    return r.json();
  } catch (error) {
    if (error.message.includes('fetch')) {
      throw new Error('Cannot connect to server. Make sure the backend is running on http://localhost:5000');
    }
    throw error;
  }
}

export async function postMessage(ticket, code, body) {
  try {
    const r = await fetch(`${API}/api/v1/reports/${ticket}/messages?code=${encodeURIComponent(code)}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ body })
    });
    if (!r.ok) throw new Error(`Message failed: ${r.status}`);
    return r.json();
  } catch (error) {
    if (error.message.includes('fetch')) {
      throw new Error('Cannot connect to server. Make sure the backend is running on http://localhost:5000');
    }
    throw error;
  }
}

export async function fetchPublicReports() {
  try {
    const r = await fetch(`${API}/api/v1/reports/public`);
    if (!r.ok) throw new Error(`Fetch reports failed: ${r.status}`);
    return r.json();
  } catch (error) {
    if (error.message.includes('fetch')) {
      throw new Error('Cannot connect to server. Make sure the backend is running on http://localhost:5000');
    }
    throw error;
  }
}