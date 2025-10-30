import React from 'react';
import { Link } from 'react-router-dom';

export default function Search() {
  return (
    <div className="search-page container" style={{paddingTop: '1.5rem', maxWidth: '100%', boxSizing: 'border-box'}}>
      <div style={{display:'flex',alignItems:'center',gap:'clamp(0.5rem, 2vw, 1rem)', width: '100%', maxWidth: '100%'}}>
        <Link to="/" aria-label="back" style={{flexShrink: 0}}>←</Link>
        <input className="form-input" placeholder="Search stories, authors, newsletters..." style={{flex:1, minWidth: 0}} />
        <button className="btn btn-ghost" style={{marginLeft:'.5rem', flexShrink: 0}}>Clear</button>
      </div>

      <div style={{marginTop:'1.25rem'}}>
        <div className="card" style={{padding:'1rem', marginBottom:'1rem'}}>
          <div style={{height:180, background:'#ddd', borderRadius:8}}></div>
        </div>

        <hr style={{border:'0',borderTop:'3px solid #000'}} />

        <div className="card" style={{padding:'1rem', marginTop:'1rem'}}>
          <div style={{height:220, background:'#ddd', borderRadius:8}}></div>
        </div>
      </div>
    </div>
  )
}
