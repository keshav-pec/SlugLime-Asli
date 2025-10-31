# Frontend - React SPA# React + Vite



The frontend for SlugLime, built with React and Vite for a fast, modern user experience.This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.



## 🚀 Quick StartCurrently, two official plugins are available:



### Installation- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh

- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

1. **Install dependencies**:

   ```bash## React Compiler

   npm install

   ```The React Compiler is not enabled on this template. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).



2. **Start development server**:## Expanding the ESLint configuration

   ```bash

   npm run devIf you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

   ```
   
   The app will be available at `http://localhost:5173`

3. **Build for production**:
   ```bash
   npm run build
   ```

4. **Preview production build**:
   ```bash
   npm run preview
   ```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Navbar.jsx       # Main navigation
│   │   ├── Footer.jsx       # Site footer
│   │   └── BrandLogo.jsx    # Logo component
│   ├── pages/               # Page components (routes)
│   │   ├── Home.jsx         # Main feed (social + reports)
│   │   ├── Submit.jsx       # Anonymous whistleblower submission
│   │   ├── Status.jsx       # Report tracking & messages
│   │   ├── About.jsx        # About page
│   │   ├── Contact.jsx      # Contact page
│   │   ├── Search.jsx       # Search functionality
│   │   ├── Newspaper.jsx    # News view
│   │   ├── Newsletter.jsx   # Newsletter
│   │   └── NotFound.jsx     # 404 page
│   ├── assets/              # Static assets (images, etc.)
│   ├── api.js               # API client functions
│   ├── App.jsx              # Main app component with routing
│   ├── App.css              # Component-specific styles
│   ├── index.css            # Base styles
│   ├── theme.css            # Theme and custom styles
│   └── main.jsx             # Entry point
├── public/                  # Static files
├── index.html               # HTML template
├── vite.config.js           # Vite configuration
├── eslint.config.js         # ESLint configuration
└── package.json             # Dependencies and scripts
```

## 🎨 Features

### Pages

- **Home** (`/`) - Main feed combining social posts and public whistleblower reports
- **Submit** (`/submit`) - Anonymous whistleblower submission form with file upload
- **Status** (`/status`) - Track reports by ticket and access code
- **About** (`/about`) - About SlugLime
- **Contact** (`/contact`) - Contact information

### Components

- **Navbar** - Responsive navigation with links to all pages
- **Footer** - Site footer with branding
- **BrandLogo** - Reusable logo component

### Styling

- Custom CSS with CSS variables for theming
- Responsive design for mobile and desktop
- Modern UI with smooth animations and transitions

## 🔧 Configuration

### API Endpoint

The backend API URL is configured in `src/api.js`:

```javascript
const API = "http://localhost:5000";
```

For production, update this to your production API URL or use an environment variable:

```javascript
const API = import.meta.env.VITE_API_URL || "http://localhost:5000";
```

Then create `.env`:
```env
VITE_API_URL=https://api.yourdomain.com
```

### Vite Configuration

`vite.config.js` includes:
- React plugin with Fast Refresh
- Development server settings
- Build optimizations

## 📦 Dependencies

### Core
- **React 18** - UI library
- **React DOM 18** - React renderer
- **React Router DOM 7** - Client-side routing

### UI & Icons
- **Lucide React** - Icon library with 1000+ icons

### Build Tools
- **Vite 6** - Fast build tool and dev server
- **@vitejs/plugin-react** - React plugin for Vite

### Development
- **ESLint** - Code linting
- **@eslint/js** - ESLint JavaScript plugin

## 🛠️ Scripts

```bash
# Start development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build locally
npm run preview

# Run ESLint
npm run lint
```

## 🌐 API Integration

The `api.js` file provides functions for all backend endpoints:

### Report Functions
```javascript
import { createReport, fetchReport, postMessage } from './api';

// Create anonymous report
const result = await createReport(formData);
// Returns: { ticket, access_code }

// Fetch report by ticket
const report = await fetchReport(ticket, accessCode);

// Post message to report
await postMessage(ticket, accessCode, messageBody);
```

### Usage Example

```jsx
import { createReport } from '../api';

async function handleSubmit() {
  const formData = new FormData();
  formData.append('title', 'Report Title');
  formData.append('body', 'Report content');
  formData.append('file_0', fileObject);
  
  const result = await createReport(formData);
  console.log('Ticket:', result.ticket);
  console.log('Access Code:', result.access_code);
}
```

## 🎨 Styling Guide

### CSS Variables

Theme variables are defined in `theme.css`:

```css
:root {
  --primary-color: #your-color;
  --background-color: #your-color;
  --text-color: #your-color;
  /* ... more variables */
}
```

### Component Styling

- Use semantic class names
- Keep styles modular and component-specific
- Use CSS variables for consistent theming

## 🚀 Production Build

### Build Process

1. **Run build**:
   ```bash
   npm run build
   ```
   
   This creates optimized files in the `dist/` folder.

2. **Test production build locally**:
   ```bash
   npm run preview
   ```

### Deployment

#### Static Hosting (Netlify, Vercel, etc.)

1. Build the project: `npm run build`
2. Deploy the `dist/` folder
3. Configure redirects for client-side routing:

   **Netlify** - Create `public/_redirects`:
   ```
   /*    /index.html   200
   ```

   **Vercel** - Create `vercel.json`:
   ```json
   {
     "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
   }
   ```

#### Self-Hosted (Nginx)

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /path/to/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

## 🧪 Development Tips

### Hot Module Replacement (HMR)

Vite provides fast HMR out of the box. Changes to React components are reflected instantly without losing component state.

### Browser DevTools

Use React DevTools extension for debugging:
- Component tree inspection
- Props and state examination
- Performance profiling

### API Development

When the backend is running on a different port, CORS is already configured. The backend accepts requests from `http://localhost:5173` by default.

## 🔍 Troubleshooting

### API Connection Issues

If you see "Failed to fetch" errors:
1. Ensure backend is running on `http://localhost:5000`
2. Check CORS configuration in backend
3. Verify API URL in `src/api.js`

### Build Issues

Clear cache and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Port Already in Use

Change the dev server port in `vite.config.js`:
```javascript
export default {
  server: {
    port: 3000  // or any available port
  }
}
```

## 📝 Code Style

- Use functional components with hooks
- Keep components small and focused
- Use meaningful variable and function names
- Add comments for complex logic
- Follow React best practices

## 🤝 Contributing

When contributing to the frontend:

1. Follow existing code style and patterns
2. Test on multiple browsers
3. Ensure responsive design works
4. Update this README if adding new features
5. Run `npm run lint` before committing

## 📄 License

MIT License - See root LICENSE file for details.
