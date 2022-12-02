if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Pooja0033/Prv-Mo-Renamebot.git /Prv-Mo-Renamebot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Prv-Mo-Renamebot
fi
cd /Prv-Mo-Renamebot
pip3 install -U -r requirements.txt
echo "Starting ...."
python3 bot.py
