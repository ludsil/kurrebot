```
      ..                                                                ..                     s    
< .z@8"`                                                          . uW8"                      :8    
 !@88E           x.    .        .u    .      .u    .              `t888              u.      .88    
 '888E   u     .@88k  z88u    .d88B :@8c   .d88B :@8c       .u     8888   .    ...ue888b    :888ooo 
  888E u@8NL  ~"8888 ^8888   ="8888f8888r ="8888f8888r   ud8888.   9888.z88N   888R Y888r -*8888888 
  888E`"88*"    8888  888R     4888>'88"    4888>'88"  :888'8888.  9888  888E  888R I888>   8888    
  888E .dN.     8888  888R     4888> '      4888> '    d888 '88%"  9888  888E  888R I888>   8888    
  888E~8888     8888  888R     4888>        4888>      8888.+"     9888  888E  888R I888>   8888    
  888E '888&    8888 ,888B .  .d888L .+    .d888L .+   8888L       9888  888E u8888cJ888   .8888Lu= 
  888E  9888.  "8888Y 8888"   ^"8888*"     ^"8888*"    '8888c. .+ .8888  888"  "*888*P"    ^%888*   
'"888*" 4888"   `Y"   'YP        "Y"          "Y"       "88888%    `%888*%"      'Y"         'Y"    
   ""    ""                                               "YP'        "`                            
```                                                                                               
                                                                                                    
# Beskrivning

Bot som fixar bet. Idén är att användaren som vill skapa ett kurrebet skriver ett sådant på formatet:

```
Testbet 15
KID kommer avnjuta flest baxbollar i år
```

Där ny rad är obligatorisk, och 15 är antalet kurre som gamblas om. Övriga användare som vill delta kan sedan reagera med ✔ och ❌ om de är för respektive mot bettet, och de läggs automatiskt in i kurredokument. Än så länge måste resultat på bet läggas in manuellt senare, men bottens syfte är främst att underlätta skapande och deltagande.

# Setup

## virtualenv

Dbs mappen kurrebot_virtualenv i deps. Fixar dependencies, skapat med virtualenv men tror inte man behöver det, endast source scriptet som finns vanligtvis. Lägger även requirements.txt i deps som man kan installera ifrån med ```pip install -r requirements.txt```.

Aktivera environment:

``` source deps/kurrebot_env/bin/activate ```

Du använder ```deactivate``` för att gå ut.


## Slack API

När du fixar ny server:

1. Nya slack token och slack signing secret, lägg i .env fil, se bot.py hur det funkar.
2. Ge rätt url till servern du hostar botten på, och subscriba till rätt bot events. Detta är under *Event Subscriptions*, och sedan events *message.channels* och *reaction_added*.
3. *OAuth & Permissions* ge rättigheter till client API, vissa av dessa kan läggas till automatiskt efter steg två. De som ska vara med är iallafall:
    * channels:history
    * chat:write
    * reactions:read
    * users.profile.read

För att skapa själva slack appen kan det vara värt att följa början på tutorial bifogat längst ner.

## Sheets API

Nytt kurredokument:

1. Gå in på google cloud platform, console.
2. Service Accounts -> skapa ett konto (eller använd befintligt)
3. lägg till service accountets mail i dokumentet
4. Gå in på service account -> ha/generera nyckel -> ladda ner som json till projekt (kanske att man måste göra ny för att få möjlighet att ladda ner, oklart)
5. pip3 install gspread (om virtualenv inte funkar)

OBS APIer som används från cloud platform är:
* sheets.googleapis.com
* drive.googleapis.com

gspread dokumentation: https://docs.gspread.org/en/latest/user-guide.html#updating-cells 

## Tutorial jag gick efter :)))**

SLACK API: https://www.youtube.com/watch?v=KJ5bFv-IRFM&list=PLzMcBGfZo4-kqyzTzJWCV6lyK-ZMYECDc
GOOGLE SHEETS API: https://www.youtube.com/watch?v=bu5wXjz2KvU