import discord
from discord.ext import commands
import random
from Rilevatore import get_class
intents = discord.Intents.default()
intents.message_content = True
problema = False
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print("scrivi $aiuto se serve aiuto per i comandi")

@bot.command()
async def test(ctx):
    await ctx.send("Hello, and goodbye")

@bot.command()
async def problem(ctx):
    global problema
    await ctx.send("dimmi, cosa vuoi sapere?")
    problema = True

@bot.command()
async def Incendi(ctx):
    global problema
    if problema == True:
        await ctx.send("il cambiamento climatico, con la persistente siccità e le temperature estreme durante i mesi estivi, amplifica e aggrava chiaramente il rischio di incendi. Queste situazioni portano a condizioni estreme di pericolo di incendio che facilitano l'accensione e la diffusione di grandi incendi")
        problema = False
    elif problema == False:
        await ctx.send("Error")

@bot.command()
async def Desertificazione(ctx):
    global problema
    if problema == True:
        await ctx.send("La desertificazione è il processo di trasformazione di terre aride, semi aride o umide in zone desertiche incoltivabili, causato da un aumento delle temperature o da una diminuzione di produttività all'interno di quel territorio")
        problema = False
    elif problema == False:
        await ctx.send("Error")

@bot.command()
async def Deforestazione(ctx):
    global problema
    if problema == True:
        await ctx.send("La deforestazione è la continua rimozione di foreste e di boschi per ottenere materiali come legno o altre piante. Più che una causa questo e uno dei motivi del riscaldamento globale. 1 per i gas che vengono dispersi nell'atmosfera per tagliare gli alberi. 2 perchè con meno alberi c'è più CO2")
        problema = False
    elif problema == False:
        await ctx.send("Error")

@bot.command()
async def Tempeste(ctx):
    global problema
    if problema == True:
        await ctx.send("Temperature più alte e calde comportano a un cambiamento dei modelli metereologici. Questo comporta tempeste più forti, più durature, più violente e ad alluvioni, che comportano la distruzione di case o città")
        problema = False
    elif problema == False:
        await ctx.send("Error")

@bot.command()
async def Temperature(ctx):
    global problema
    if problema == True:
        await ctx.send("Con l'aumentare delle temperature, causate da gas serra e da prodotti che aumentano il cosiddetto 'buco nell'ozono', negli ultimi anni lo scioglimento dei ghiacciai è aumentato esponenzialmente, eliminando l'habitat di alcune specie animali, come orsi polari o pinguini  ")
        problema = False
    elif problema == False:
        await ctx.send("Error")

@bot.command()
async def Random(ctx):
    global problema
    x = random.randint(1,5)
    if problema == True:
        if x == 1:
            await ctx.send("il cambiamento climatico, con la persistente siccità e le temperature estreme durante i mesi estivi, amplifica e aggrava chiaramente il rischio di incendi. Queste situazioni portano a condizioni estreme di pericolo di incendio che facilitano l'accensione e la diffusione di grandi incendi")
        elif x == 2:
            await ctx.send("Con l'aumentare delle temperature, causate da gas serra e da prodotti che aumentano il cosiddetto 'buco nell'ozono', negli ultimi anni lo scioglimento dei ghiacciai è aumentato esponenzialmente, eliminando l'habitat di alcune specie animali, come orsi polari o pinguini  ")
        elif x == 3:
            await ctx.send("La desertificazione è il processo di trasformazione di terre aride, semi aride o umide in zone desertiche incoltivabili, causato da un aumento delle temperature o da una diminuzione di produttività all'interno di quel territorio")
        elif x == 4:
            await ctx.send("La deforestazione è la continua rimozione di foreste e di boschi per ottenere materiali come legno o altre piante. Più che una causa questo e uno dei motivi del riscaldamento globale. 1 per i gas che vengono dispersi nell'atmosfera per tagliare gli alberi. 2 perchè con meno alberi c'è più CO2")
        elif x == 5:
            await ctx.send("Temperature più alte e calde comportano a un cambiamento dei modelli metereologici. Questo comporta tempeste più forti, più durature, più violente e ad alluvioni, che comportano la distruzione di case o città")           
        problema = False
    elif problema == False:
        await ctx.send("Error")

@bot.command()
async def rileva(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{file_name}')
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Hai dimenticato di caricare l'immagine")
@bot.command()
async def aiuto(ctx):
    await ctx.send("$test, $rileva --> Carica un immagine riguardante il riscaldamento e vedrai!, $consiglio, dopo consiglio -> $Desertificazione, $Incendi, $Tempeste, $Temperature, $Deforestazione, $Random")

    
bot.run("")
