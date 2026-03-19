# Anime Power Rankings

A Streamlit app creating a continuous Elo-based tournament for anime, tailored for action and fantasy fans like Cody! It features a list of popular action, fantasy, and level-up style anime similar to *Solo Leveling*.

## Running Locally

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deploying to Streamlit Community Cloud

1. Initialize Git in this directory, commit your files, and push to a new GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   # Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub info
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **New App**, select your newly created GitHub repository, and make sure the `Main file path` is set to `app.py`.
4. Click **Deploy!**

Anytime you make changes locally, simply run these commands to continuously repush and update your live app:
```bash
git add .
git commit -m "Update app"
git push
```
Streamlit Cloud will automatically detect the changes on GitHub and update your live app!
