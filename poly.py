#GUI for text to speech converter
#using tkinter
import tkinter as tk
import os
import sys
import boto3
from tempfile import gettempdir 
from contextlib import closing
#creating a window
root=tk.Tk()
root.geometry("400x240")
root.title("Text to Speech Converter Using Amazon Polly")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
    aws_mg_con=boto3.session.Session(profile_name="User_name")
    client=aws_mg_con.client(service_name="polly",region_name="us-east-1")
    result=textExample.get("1.0","end")
    print(result)
    response=client.synthesize_speech(Text=result,OutputFormat='mp3',Engine='standard',VoiceId='Aditi')
    print(response)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not find the AudioStream")
        sys.exit(-1)
    if sys.platform=='win32':
        os.startfile(output)
btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()

root.mainloop()
