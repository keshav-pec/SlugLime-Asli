import React from "react";
import { Link } from "react-router-dom";
import { Search } from "lucide-react";

export default function Home() {
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
        {/* empty content area for now - real feed will be added later */}
        <div style={{minHeight:'30vh'}}></div>

        <Link to="/submit" className="fab" aria-label="create">
          <div className="fab-inner">+</div>
        </Link>
      </main>
    </div>
  );
}
