from fastapi import FastAPI            #import fastaoi
import os                                #import opreating system
from dotenv import load_dotenv          #

from models import TicketCreate,Ticket        #import modelfile
from services import AIService   #import google genai


load_dotenv()

#if os.getenv()



ticket_db=[]
aiservice = AIService()


app= FastAPI(title="AI APP")                              #class

@app.get("/health")
def health():
    return{"msg":"backend is running"}

@app.post("/tickets")
def tickets(ticket:TicketCreate):
    
    tickets_id = len(ticket_db) +1 
    
    prompt=f"""
you are a support agent,given a problem by user you should answer it politely
,clearly and consisely.

user query:
title:{ticket.title}
description:{ticket.description}    
    
    """
    response=aiservice.generate_reply(prompt)
    
    new_ticket= Ticket(
        title=ticket.title,
        description=ticket.description,
        id=tickets_id,
        ai_reply=response
        )
    

    ticket_db.append(new_ticket)
         
    return {
        "msg":"ticket created successfully",
        "ticket":new_ticket
        }
    
@app.get("/tickets")
def tickets():
    return ticket_db

