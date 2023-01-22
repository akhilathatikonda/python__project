import tkinter as tk
from PIL import Image,ImageTk
import requests

root=tk.Tk()
root.title("Weather App")
root.geometry("600x500")

def format_response(weather):
    try:
        city=weather["name"]
        condition=weather["weather"][0]["description"]
        temp=weather["main"]["temp"]
        final_str="City:%s\nCondition:%s\nTemperature:%s"%(city,condition,temp)
    except:
        final_str="There was a problem in getting inforamtion"
    return final_str   

def get_weather(city):
    weather_key="0fecc68658de6ebc1257a738a307885b"
    url="https://api.openweathermap.org/data/2.5/weather"
    params={"APPID":weather_key,"q":city,"units":"imperial"}
    response=requests.get(url,params)
    weather=response.json()
    
    '''print(weather["name"])
    print(weather["weather"][0]["description"])
    print(weather["main"]["temp"])'''

    result["text"]=format_response(weather)

    icon_name=weather["weather"][0]["icon"]
    open_image(icon_name)

def open_image(icon_name):
    size=int(frame2.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open("./img/"+icon_name+".png").resize((size,size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0,anchor="nw",image=img)
    weather_icon.image=img
    
      
    


img=Image.open("C:/Users/akhil/OneDrive/Documents/New folder/bg.webp")
img=img.resize((600,500),Image.LANCZOS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading=tk.Label(bg_lbl,text="Weather report!!!",fg="red",bg="sky blue",font=("times new roman",16,"bold"))
heading.place(x=100,y=18)

frame1=tk.Frame(bg_lbl,bg="sky blue",bd=5)
frame1.place(x=100,y=50,width=450,height=50)

txt1=tk.Entry(frame1,font=("times new roman",25,"bold"),width=17)
txt1.grid(row=0,column=0,sticky="W")

btn1=tk.Button(frame1,text="get weather",fg="green",font=("times new roman",16,"bold"),command=lambda:get_weather(txt1.get()))
btn1.grid(row=0,column=1,padx=10)

frame2=tk.Frame(bg_lbl,bg="sky blue",bd=5)
frame2.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame2,font=40,bg="white",justify="left",anchor="nw")
result.place(relwidth=1,relheight=1)

weather_icon=tk.Canvas(result,tg="white",bd=0,heightlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)
root.mainloop()
