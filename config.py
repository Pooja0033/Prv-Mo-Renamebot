import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "10303160")

API_HASH = os.environ.get("API_HASH", "a479b881a19ec6ddb64ed90f834488e8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5954355727:AAHx_hgzg3OetXN8jHhaZODSOhTVt05JOQQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Prv_35") 

DB_NAME = os.environ.get("DB_NAME","Prv")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://YO:YO@cluster0.4j0kwrm.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/ckXcvHY/file-171.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1484847208').split()]

PORT = os.environ.get("PORT", "8080")
