import requests
from tkinter import*
import webbrowser
from os import path
from PIL import ImageTk,Image

def writeHTML(datajson,entry1, entry2):
    ofile = open("darksky.html", "w")
    ofile.write("<h1>" + datajson['timezone'] + "</h1>")
    ofile.write("<p1>" + datajson['currently']['summary'] + "</p1>")
    ofile.write("<p2>" + datajson['minutely']['data']['precipType'] + "</p2>")
    ofile.write("<link rel='stylesheet' href='https://unpkg.com/leaflet@1.4.0/dist/leaflet.css'/>")
    ofile.write("<script src='https://unpkg.com/leaflet@1.4.0/dist/leaflet.js'></script>")
    ofile.write("<div id='map' style='width:100%; height:500'></div>")
    ofile.write("<script>")
    ofile.write("map = new L.Map('map');")
    ofile.write("osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';")
    ofile.write("osmAttrib='OpenStreetMap';")
    ofile.write("osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 20, attribution: osmAttrib});")
    ofile.write("map.setView(new L.LatLng(" + entry1 + "," + entry2 + "),13);")
    ofile.write("map.addLayer(osm);")
    ofile.write("</script>")
    ofile.close()

def getAPI():
    myrequest = requests.get("https://api.darksky.net/forecast/a66a8c56aa21d5a6a7b28ae5f5bd97fc/"+entry1.get() + "," + entry2.get()) #requests data from a server online
    datajson = myrequest.json()
    writeHTML(datajson,entry1.get(), entry2.get())
    

root = Tk()
root.title("DarkSky Launcher")
root.geometry("800x400")
root.configure(background = "#6c848c") 

topframe = Frame(root,bg="#38352e",height="40")
topframe.pack(fill=X)

imgframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
imgframe.pack(fill=None, expand=False)
canvas = Canvas(imgframe,height=150,width=200)
canvas.grid(row=0,column=0)
l1 = Label(imgframe,text="Welcome to the DarkSky Launcher! To proceed, please follow the directions below.",fg="black")
l1.grid(row=0,column=1)
myimage = Image.open("darksky.jpeg")
myimage = myimage.resize((200, 150), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
canvas.create_image(0, 0, image=myimg, anchor = NW)

l2 = Label(root,text = "1. Enter lattitude and longitude into the boxes,respectively.", fg = "black")
l2.pack()
l3 = Label(root,text = "2. Press 'submit' and run the program.", fg = "black")
l3.pack() 

entry1 = Entry(root)
entry1.pack()
entry2 = Entry(root)
entry2.pack()

button1 = Button(root, text = "submit",command = getAPI)
button1.pack()

