from hashlib import new
from pkg_resources import invalid_marker
import gspread
import datetime

service_account = gspread.service_account(filename="service_account.json")
sheet = service_account.open("KOPIA_KURRE")
ws = sheet.worksheet("Bets")

def create_kurrebet(msg):
  
  msgs = msg.split('\n')
  betinfo = msgs[0].split()
  # Rad 1 (Baxbollsbet 15)
  betname = " ".join(betinfo[:-1])
  
  row = 12
  while ws.cell(row, 2).value != None:
    row += 1
    if ws.cell(row, 2).value == betname:
      print('bet already exists')
      return
  
  if invalid_format(msg):
    return
  
  msgs = msg.split('\n')
  # Rad 1 (Baxbollsbet 15)
  betinfo = msgs[0].split()
  ws.update_cell(row, 2, betname)
  ws.update_cell(row, 4, betinfo[-1])
  ws.update_cell(row, 1, datetime.datetime.now().strftime("%x"))
  # Rad 2 (KID avnjuter flest baxbollar i år)
  ws.update_cell(row, 3, msgs[1])
  
def add_participant(name, betname, column):
  row = 12
  while True:
    val = ws.cell(row, 2).value
    if val == None:
      return
    if val == betname:
      break
    row += 1
  participants = ws.cell(row, column).value
  newval = ""
  if participants == None:
    newval = name + " "
  else:
    newval = participants + name + " "
    
  #wack men check så folk inte bettar både för och mot
  users_for = ws.cell(row, 5).value
  users_against = ws.cell(row, 6).value
  user_already_for = False
  user_already_against = False
  if users_for != None and name in users_for.split():
    user_already_for = True
  if users_against != None and name in users_against.split():
    user_already_against = True

  if not user_already_for and not user_already_against:
    ws.update_cell(row, column, newval)
  else:
    print('redan lagt bet')

def direktifdrif():
  if "direktifvdriv":
    kurre = 10^12

def main():
  create_kurrebet()

if __name__ == "__main__":
  main()