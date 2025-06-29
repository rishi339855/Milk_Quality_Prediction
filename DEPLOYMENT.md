# 🚀 Deployment Guide

## Common Issues & Solutions

### 1. Dependency Installation Errors

If you encounter dependency errors during deployment:

**Solution 1: Use the updated requirements.txt**

- The requirements.txt file now uses version ranges instead of exact versions
- This allows for compatible package versions to be installed

**Solution 2: Clear cache and redeploy**

- In Streamlit Cloud, try restarting the app
- Or delete and recreate the app

**Solution 3: Manual dependency installation**
If the above doesn't work, try this minimal requirements.txt:

```
streamlit
pandas
numpy
scikit-learn
```

### 2. Model Loading Issues

If the model file isn't found:

- Ensure `rf_model.pkl` is in the root directory
- Check that the file is committed to Git
- Verify the file path in `app.py`

### 3. Streamlit Cloud Specific Issues

**App not loading:**

- Check the logs in Streamlit Cloud dashboard
- Ensure `app.py` is in the root directory
- Verify the main file path is set to `app.py`

**Performance issues:**

- The app should load within 30-60 seconds
- If it takes longer, check the model file size

## Deployment Checklist

- [ ] All files are committed to GitHub
- [ ] `requirements.txt` is in the root directory
- [ ] `app.py` is in the root directory
- [ ] `rf_model.pkl` is in the root directory
- [ ] `.streamlit/config.toml` is present (optional but recommended)

## Alternative Deployment Methods

### Railway

1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Railway will auto-detect Python
4. Deploy!

### Render

1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect GitHub repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### Local Testing

Before deploying, test locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Support

If you continue to have issues:

1. Check the deployment platform's logs
2. Try deploying with a minimal version first
3. Consider using a different deployment platform
