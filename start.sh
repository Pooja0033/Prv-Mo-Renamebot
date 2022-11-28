if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MyBotzz/PYRO-RENAME-BOT.git /RENAMERBOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RENAMERRBOT
fi
cd /RENAMERBOT
pip3 install -U -r requirements.txt
echo "Starting ...."
python3 bot.py
