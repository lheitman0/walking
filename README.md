# Walk More - Streamlit App

A beautiful, minimalist app encouraging people to walk more with an interactive Lorenz attractor animation.

## Features

- **Interactive Home Page**: Features a mesmerizing Lorenz attractor animation with a powerful message about walking
- **Simple Message**: "Please walk more. I'm begging you. A long aimless walk with no headphones will solve your problems I promise. What do you find when you only look for yourself?"
- **Read Page**: Links to walking-related articles and research
- **Responsive Design**: Works on desktop and mobile devices

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app locally**:
   ```bash
   streamlit run app.py
   ```

3. **Access the app**:
   Open your browser and go to `http://localhost:8501`

## Deployment to Streamlit Cloud

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the main file path to `app.py`
   - Click "Deploy"

## File Structure

```
walking/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── README.md             # This file
└── deploy.sh             # Deployment helper script
```

## Usage

1. **Home Page**: Experience the interactive Lorenz attractor animation with the walking message
2. **Read Page**: Explore walking-related articles and research by clicking "Read"

## Technologies Used

- **Streamlit**: Web app framework
- **Three.js**: 3D animation (Lorenz attractor)
- **Custom CSS**: Styling with the Chomsky font and dark theme

## Notes

- The app maintains a beautiful, minimalist design
- The Lorenz attractor animation runs in the browser using Three.js
- The message is displayed prominently with elegant typography
- The app is fully responsive and works on mobile devices
- No external APIs required - completely self-contained
