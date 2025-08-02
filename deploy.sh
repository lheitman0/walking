#!/bin/bash

echo "🚶 Walk More - Streamlit App Deployment"
echo "========================================"

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "❌ Error: requirements.txt not found!"
    exit 1
fi

# Check if app.py exists
if [ ! -f app.py ]; then
    echo "❌ Error: app.py not found!"
    exit 1
fi

echo "✅ All files present"
echo ""
echo "📋 Next steps for deployment:"
echo "1. Push your code to GitHub:"
echo "   git add ."
echo "   git commit -m 'Initial commit'"
echo "   git push origin main"
echo ""
echo "2. Deploy on Streamlit Cloud:"
echo "   - Go to https://share.streamlit.io"
echo "   - Sign in with GitHub"
echo "   - Click 'New app'"
echo "   - Select your repository"
echo "   - Set main file path to: app.py"
echo "   - Click 'Deploy'"
echo ""
echo "🎉 Your app will be live at a URL like: https://your-app-name.streamlit.app"
echo ""
echo "✨ No API keys or environment variables needed - the app is completely self-contained!" 