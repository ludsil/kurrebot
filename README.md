**VIRTUALENV**

Fixar dependencies, skapat med virtualenv men tror inte man behöver det, endast source scriptet som finns vanligtvis.

Aktivera environment:

``` source kurrebot_env/bin/activate ```

Du använder ```deactivate``` för att gå ut.


OBS TESTA OM DET FUNKAR ATT TRANSFERA DEPENDENCIES


**SLACK API**

När du fixar ny server:

1. Nya slack token och slack signing secret
2. *OAuth & Permissions* ge rättigheter att läsa, *chat:write*. *chat:history* borde läggas till här auto efter steg 3.
3. Ge rätt url, och sätt upp så den läser. Detta är under *Event Subscriptions*, och sedan eventet *message.channels*


**SHEETS API**

Nytt kurredokument:

1. Gå in på google cloud platform, console.
2. Service Accounts -> skapa ett konto (eller använd befintligt)
3. lägg till service accountets mail i dokumentet
4. Gå in på service account -> ha/generera nyckel -> ladda ner som json till projekt (kanske att man måste göra ny för att få möjlighet att ladda ner, oklart)
5. pip3 install gspread (om venv inte funkar)

OBS APIer som används från cloud platform är:
* sheets.googleapis.com
* drive.googleapis.com

gspread dokumentation: https://docs.gspread.org/en/latest/user-guide.html#updating-cells 

**Tutorial jag gick efter :)))**

SLACK API: https://www.youtube.com/watch?v=KJ5bFv-IRFM&list=PLzMcBGfZo4-kqyzTzJWCV6lyK-ZMYECDc
GOOGLE SHEETS API: https://www.youtube.com/watch?v=bu5wXjz2KvU