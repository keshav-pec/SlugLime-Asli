import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Search, MessageCircle, Heart, Share2, MoreHorizontal } from "lucide-react";
import { fetchPublicReports } from "../api";

export default function Home() {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadReports();
  }, []);

  const loadReports = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await fetchPublicReports();
      setReports(data.reports || []);
    } catch (err) {
      console.error("Error fetching reports:", err);
      setError(err.message || "Failed to load reports");
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return "just now";
    if (diffMins < 60) return `${diffMins}m`;
    if (diffHours < 24) return `${diffHours}h`;
    if (diffDays < 7) return `${diffDays}d`;
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  };

  const getCategoryBadge = (category) => {
    const styles = {
      corruption: { bg: '#fee2e2', color: '#dc2626', text: '🚨 Corruption' },
      fraud: { bg: '#fed7aa', color: '#ea580c', text: '⚠️ Fraud' },
      harassment: { bg: '#e9d5ff', color: '#9333ea', text: '🛑 Harassment' },
      safety: { bg: '#fef3c7', color: '#d97706', text: '⚡ Safety' },
      other: { bg: '#e5e7eb', color: '#6b7280', text: '📢 Other' }
    };
    const style = styles[category?.toLowerCase()] || styles.other;
    return style;
  };
  return (
    <div className="home-page">
      <header className="container page-header" style={{paddingTop: 'clamp(0.75rem, 2vw, 1.5rem)', paddingBottom: 'clamp(0.75rem, 2vw, 1.5rem)'}}>
        <hr style={{border:'0',borderTop:'1px solid #ddd',margin:'clamp(0.5rem, 2vw, 1rem) 0'}} />
        <h1 style={{
          fontSize:'clamp(2.5rem, 10vw, 5rem)',
          margin:'clamp(0.5rem, 2vw, 1rem) 0',
          textAlign:'center',
          fontWeight:800,
          color:'#111',
          lineHeight:1
        }}>slugLime</h1>
        <div style={{
          display:'flex',
          justifyContent:'center',
          alignItems:'center',
          gap:'clamp(0.75rem, 2vw, 1rem)',
          marginTop:'clamp(1rem, 3vw, 1.75rem)',
          flexWrap:'wrap'
        }}>
          <Link to="/search" aria-label="search" title="Search" style={{
            display:'inline-flex',
            alignItems:'center',
            justifyContent:'center',
            width:'clamp(40px, 10vw, 44px)',
            height:'clamp(40px, 10vw, 44px)',
            borderRadius:'50%',
            border:'1px solid #ddd',
            background:'#fff',
            flexShrink:0
          }}>
            <Search color="#111" size={20} />
          </Link>

          <div className="segmented-control" role="tablist" aria-label="content-type">
            <Link to="/newspaper" className="seg-btn active">newspaper</Link>
          </div>
        </div>
        <hr style={{border:'0',borderTop:'1px solid #ddd',margin:'clamp(1rem, 3vw, 1.75rem) 0 0 0'}} />
      </header>

      <main className="container" style={{
        minHeight:'calc(100vh - 400px)',
        position:'relative',
        paddingBottom:'clamp(4rem, 10vh, 6rem)'
      }}>
        {/* Twitter-like Feed */}
        <div style={{
          maxWidth: '600px',
          margin: '0 auto',
          background: '#fff'
        }}>
          {loading && (
            <div style={{textAlign: 'center', padding: '3rem', color: '#666'}}>
              <div style={{
                width: '40px',
                height: '40px',
                border: '3px solid #e5e7eb',
                borderTop: '3px solid #06b6d4',
                borderRadius: '50%',
                margin: '0 auto 1rem',
                animation: 'spin 1s linear infinite'
              }}></div>
              Loading reports...
            </div>
          )}

          {error && (
            <div style={{
              padding: '1.5rem',
              margin: '1rem',
              background: '#fee2e2',
              borderRadius: '0.75rem',
              color: '#dc2626',
              textAlign: 'center'
            }}>
              <p style={{margin: 0}}>⚠️ {error}</p>
              <button 
                onClick={loadReports}
                style={{
                  marginTop: '1rem',
                  padding: '0.5rem 1rem',
                  background: '#dc2626',
                  color: '#fff',
                  border: 'none',
                  borderRadius: '0.5rem',
                  cursor: 'pointer'
                }}
              >
                Try Again
              </button>
            </div>
          )}

          {!loading && !error && reports.length === 0 && (
            <div style={{textAlign: 'center', padding: '3rem', color: '#666'}}>
              <p style={{fontSize: '1.25rem', marginBottom: '1rem'}}>No reports yet</p>
              <p style={{color: '#9ca3af'}}>Be the first to blow the whistle!</p>
              <Link 
                to="/submit" 
                className="btn btn-primary" 
                style={{marginTop: '1.5rem', display: 'inline-block'}}
              >
                Submit Report
              </Link>
            </div>
          )}

          {!loading && !error && reports.map((report) => {
            const badge = getCategoryBadge(report.category);
            return (
              <article 
                key={report.id}
                style={{
                  borderBottom: '1px solid #e5e7eb',
                  padding: 'clamp(1rem, 3vw, 1.25rem)',
                  transition: 'background 0.2s',
                  cursor: 'pointer'
                }}
                onMouseEnter={(e) => e.currentTarget.style.background = '#f9fafb'}
                onMouseLeave={(e) => e.currentTarget.style.background = '#fff'}
              >
                {/* Header */}
                <div style={{display: 'flex', gap: '0.75rem', marginBottom: '0.75rem'}}>
                  {/* Avatar */}
                  <div style={{
                    width: '40px',
                    height: '40px',
                    borderRadius: '50%',
                    background: 'linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 'bold',
                    fontSize: '1.25rem',
                    color: '#000',
                    flexShrink: 0
                  }}>
                    W
                  </div>

                  {/* Author Info */}
                  <div style={{flex: 1, minWidth: 0}}>
                    <div style={{display: 'flex', alignItems: 'center', gap: '0.5rem', flexWrap: 'wrap'}}>
                      <span style={{fontWeight: 700, color: '#111', fontSize: '0.9375rem'}}>
                        {report.author.name}
                      </span>
                      {report.author.verified && (
                        <span style={{color: '#1d9bf0'}}>✓</span>
                      )}
                      <span style={{color: '#6b7280', fontSize: '0.875rem'}}>
                        · {formatDate(report.created_at)}
                      </span>
                    </div>
                    
                    {/* Category Badge */}
                    {report.category && (
                      <span style={{
                        display: 'inline-block',
                        marginTop: '0.25rem',
                        padding: '0.125rem 0.5rem',
                        borderRadius: '0.375rem',
                        fontSize: '0.75rem',
                        fontWeight: 600,
                        background: badge.bg,
                        color: badge.color
                      }}>
                        {badge.text}
                      </span>
                    )}
                  </div>

                  {/* More Options */}
                  <button style={{
                    background: 'none',
                    border: 'none',
                    color: '#6b7280',
                    cursor: 'pointer',
                    padding: '0.25rem',
                    borderRadius: '50%',
                    width: '32px',
                    height: '32px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    <MoreHorizontal size={18} />
                  </button>
                </div>

                {/* Content */}
                <div style={{marginBottom: '0.75rem', paddingLeft: '3rem'}}>
                  <h3 style={{
                    fontSize: 'clamp(1rem, 2.5vw, 1.0625rem)',
                    fontWeight: 700,
                    color: '#111',
                    margin: '0 0 0.5rem 0',
                    lineHeight: 1.4
                  }}>
                    {report.title}
                  </h3>
                  <p style={{
                    color: '#374151',
                    fontSize: 'clamp(0.875rem, 2vw, 0.9375rem)',
                    lineHeight: 1.5,
                    margin: 0,
                    whiteSpace: 'pre-wrap',
                    wordBreak: 'break-word'
                  }}>
                    {report.body}
                  </p>
                </div>

                {/* Actions */}
                <div style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  maxWidth: '425px',
                  paddingLeft: '3rem',
                  color: '#6b7280',
                  fontSize: '0.875rem'
                }}>
                  <button style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    background: 'none',
                    border: 'none',
                    color: '#6b7280',
                    cursor: 'pointer',
                    padding: '0.375rem 0.625rem',
                    borderRadius: '0.5rem',
                    transition: 'all 0.2s'
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(29, 155, 240, 0.1)';
                    e.currentTarget.style.color = '#1d9bf0';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'transparent';
                    e.currentTarget.style.color = '#6b7280';
                  }}>
                    <MessageCircle size={18} />
                    <span>{report.comment_count || 0}</span>
                  </button>

                  <button style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    background: 'none',
                    border: 'none',
                    color: '#6b7280',
                    cursor: 'pointer',
                    padding: '0.375rem 0.625rem',
                    borderRadius: '0.5rem',
                    transition: 'all 0.2s'
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(239, 68, 68, 0.1)';
                    e.currentTarget.style.color = '#ef4444';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'transparent';
                    e.currentTarget.style.color = '#6b7280';
                  }}>
                    <Heart size={18} />
                    <span>{report.like_count || 0}</span>
                  </button>

                  <button style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    background: 'none',
                    border: 'none',
                    color: '#6b7280',
                    cursor: 'pointer',
                    padding: '0.375rem 0.625rem',
                    borderRadius: '0.5rem',
                    transition: 'all 0.2s'
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(34, 197, 94, 0.1)';
                    e.currentTarget.style.color = '#22c55e';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'transparent';
                    e.currentTarget.style.color = '#6b7280';
                  }}>
                    <Share2 size={18} />
                  </button>
                </div>

                {/* Ticket Info */}
                <div style={{
                  paddingLeft: '3rem',
                  marginTop: '0.75rem',
                  fontSize: '0.75rem',
                  color: '#9ca3af'
                }}>
                  Ticket: <code style={{
                    background: '#f3f4f6',
                    padding: '0.125rem 0.375rem',
                    borderRadius: '0.25rem',
                    fontFamily: 'monospace'
                  }}>{report.ticket}</code>
                </div>
              </article>
            );
          })}
        </div>

        <Link to="/submit" className="fab" aria-label="create">
          <div className="fab-inner">+</div>
        </Link>
      </main>
    </div>
  );
}
