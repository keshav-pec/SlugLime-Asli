import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function Newspaper(){
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchNews();
  }, []);

  const fetchNews = async () => {
    try {
      setLoading(true);
      // Using NewsAPI - fetching top headlines
      const response = await fetch(
        'https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey=4e3c5a0d8f8d4d25b8c8d5e5f5e5f5e5'
      );
      
      if (!response.ok) {
        throw new Error('API error');
      }
      
      const data = await response.json();
      
      if (data.status === 'ok' && data.articles) {
        const articlesWithImages = data.articles.filter(
          article => article.urlToImage && article.title !== '[Removed]'
        );
        setNews(articlesWithImages.length > 0 ? articlesWithImages : getSampleNews());
      } else {
        setNews(getSampleNews());
      }
    } catch (err) {
      console.error('Error fetching news:', err);
      setNews(getSampleNews());
    } finally {
      setLoading(false);
    }
  };

  const getSampleNews = () => [
    {
      title: "Major Breakthrough in Renewable Energy",
      description: "Scientists announce revolutionary solar panel design",
      urlToImage: "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800",
      source: { name: "Tech Today" }
    },
    {
      title: "Global Markets React to Policy Changes",
      description: "Stock markets show mixed reactions",
      urlToImage: "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800",
      source: { name: "Financial Times" }
    },
    {
      title: "Medical Research Offers New Hope",
      description: "Treatment shows promising results",
      urlToImage: "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800",
      source: { name: "Health News" }
    },
    {
      title: "AI Collaboration Announced",
      description: "Tech companies form alliance",
      urlToImage: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",
      source: { name: "Tech Wire" }
    },
    {
      title: "Space Exploration Milestone",
      description: "Private company launches mission",
      urlToImage: "https://images.unsplash.com/photo-1516849841032-87cbac4d88f7?w=800",
      source: { name: "Space Today" }
    }
  ];

  return (
    <div className="newspaper-page container" style={{paddingTop:'1.5rem'}}>
      <header style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h2 style={{margin:0,fontSize:'2rem'}}>Today</h2>
        <Link to="/" style={{fontSize:'1.25rem'}}>✕</Link>
      </header>

      {loading ? (
        <div style={{textAlign: 'center', padding: '3rem', color: '#666'}}>
          <div style={{
            width: '40px',
            height: '40px',
            border: '3px solid #e5e7eb',
            borderTop: '3px solid #111',
            borderRadius: '50%',
            margin: '0 auto 1rem',
            animation: 'spin 1s linear infinite'
          }}></div>
        </div>
      ) : (
        <div style={{marginTop:'1rem'}}>
          {news[0] && (
            <a 
              href="#"
              className="card" 
              style={{padding:'1rem', marginBottom:'1rem', display: 'block', textDecoration: 'none', color: 'inherit'}}
            >
              <div style={{
                height:220, 
                background: news[0].urlToImage ? `url(${news[0].urlToImage}) center/cover` : '#ddd', 
                borderRadius:8
              }}></div>
              <h3 style={{marginTop:'.75rem', fontWeight: 700}}>From: {news[0].source.name}</h3>
              <p style={{color:'#444', fontWeight: 400}}>{news[0].title}</p>
            </a>
          )}

          <div className="mag-grid" style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'1rem'}}>
            {news.slice(1, 5).map((article, index) => (
              <a
                key={index}
                href="#"
                className="card" 
                style={{padding:'1rem', display: 'block', textDecoration: 'none', color: 'inherit'}}
              >
                <div style={{
                  height: index === 3 ? 220 : 120, 
                  background: article.urlToImage ? `url(${article.urlToImage}) center/cover` : '#ddd', 
                  borderRadius:8
                }}></div>
                <h4 style={{marginTop:'.5rem', fontWeight: 700, fontSize: '0.95rem', margin: '.5rem 0 .25rem 0'}}>{article.source.name}</h4>
                <p style={{margin: 0, fontWeight: 400, color: '#444', fontSize: '0.9rem'}}>{article.description || article.title}</p>
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
